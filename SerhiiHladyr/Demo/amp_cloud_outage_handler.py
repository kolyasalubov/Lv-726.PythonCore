#!/usr/bin/env python3.9
import argparse
import hashlib
import itertools
import logging
import os
import requests
import speedtest
import time
import urllib3
from datetime import datetime,timedelta

parser = argparse.ArgumentParser(description='Switch Amp Cloud Region via cli')
parser.add_argument('-r', '--region', help='[Required] Amp Cloud Region.', default=None, required=False)
args = parser.parse_args()
print(f'\nHey, you have choosen: {args.region}')

test_org_id = os.environ.get("AMP_CONNECTION_KEEPALIVE_ORG_ID")
test_tx_id = os.environ.get("AMP_CONNECTION_KEEPALIVE_TXN_ID")
amp_url = "https://localhost:8443/v2/{0}/cloudlookup/{1}".format(test_org_id, test_tx_id)
amp_clouds_failover_list_os = os.environ.get("AMP_CLOUD_FAILOVER_LIST").split(",")
dc = os.environ.get("QQ_DATACENTER")

logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp" : "%(asctime)s","level" : "%(levelname)s","service" : "amp_cloud_outage_handler","message":"%(message)s"}'
)

def read_amp_cloud_file_to_print():
    try:
        with open('/opt/amp-scanner/tmp/amp_cloud.env','r') as cloud_file :
            amp = cloud_file.readline()
            cloud_file.close()
            return amp
    except Exception as e:
        logging.exception("Ooops! The file amp_cloud.env will be created one loop cycle later ;)")
        return True

# Switch to another default Amp Cloud from command line
print(f'\nThe default list of Amp Clouds is next: {amp_clouds_failover_list_os}')
print(f'\nThe current primary Amp Cloud Env is next: {read_amp_cloud_file_to_print()}')
print(f'\nThe next primary Amp Region will be as --region={args.region}')

def amp_clouds_failover_list(region):
    nam = 'NAM=cloud.nam.amp.cloud.com'
    eu = 'EU=cloud.eu.amp.cloud.com'
    apjc = 'APJC=cloud.apjc.amp.cloud.com'
    amp_clouds_failover_list = os.environ.get("AMP_CLOUD_FAILOVER_LIST").split(",")
    if (region):
        if (region=='NAM'):
            amp_clouds_failover_list = [nam, eu, apjc]
            return amp_clouds_failover_list
        elif (region=='EU'):
            amp_clouds_failover_list = [eu, nam, apjc]
            return amp_clouds_failover_list
        elif (region=='APJC'):
            amp_clouds_failover_list = [apjc, nam, eu]
            return amp_clouds_failover_list
        else:
            return amp_clouds_failover_list
    else:
        return amp_clouds_failover_list
print(f'\nYou are switching to the next list of Amp Clouds: {amp_clouds_failover_list(args.region)}')

def check_amp_cloud_availability():
    try:
        logging.info("Attempt to reach out to Amp Cloud via localhost:8443")
        urllib3.disable_warnings()
        sha256 = hashlib.sha256().hexdigest()
        headers = {"X-SIG-Sha256": sha256}
        #! Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised
        # See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
        result = requests.get(url=amp_url, headers=headers, timeout=20, verify=False)
        if result.status_code != 200:
            logging.error("Error happened during Amp Cloud health check")
            return False
        return True
    except requests.exceptions.Timeout :
        logging.exception("Cannot curl cloudlookup endpoint, cannot determine AMP cloud availability")
        return False
    except Exception as e:
        logging.exception("Cannot curl cloudlookup endpoint, cannot determine AMP cloud availability")
        return True

def check_network_latency():
    try:
        logging.info("Start Network Latency checking via speedtest")
        threads = None
        # default timeout = 10 sec
        speed_test = speedtest.Speedtest()
        # get result in bit/s and convert to mbits/s
        latency_result = speed_test.download(threads=threads) * 0.000001
        logging.info(f'Network Latency is {int(latency_result)} Mbit/s')

        # Writing Network Latency to file
        file_path = "/tmp/latency.txt"
        print (f'\nWriting Network Latency into linux file: {file_path}\n')
        with open(file_path, 'w') as f:
            f.write(str(int(latency_result)))
            f.close()

        print(f'\nSpeedtest successful or not ? isinstance() =  {isinstance(latency_result, (int, float))}\n')
        if not isinstance(latency_result, (int, float)):
            print(f'\nSpeedtest successful or not ? isinstance() =  {isinstance(latency_result, (int, float))}\n')
            raise Exception('Speedtest-cli failure.')
        return int(latency_result)
    except Exception as e:
        logging.exception("Cannot speedtest, cannot measure network Latency. %s", e)

def restart_application():
    os.system('supervisorctl stop amp:amp-scanner')
    os.system('supervisorctl stop amp:beakerd')
    os.system('supervisorctl stop amp:stunnel')
    os.system('supervisorctl start amp:stunnel')
    os.system('supervisorctl start amp:beakerd')
    os.system('supervisorctl start amp:amp-scanner')

def write_amp_cloud_to_file(amp_cloud,amp_region):
    with open('/opt/amp-scanner/tmp/amp_cloud.env','w') as cloud_file :
        cloud_file.write("export AMP_CLOUD={0}\n".format(amp_cloud))
        cloud_file.write("export AMP_REGION={0}".format(amp_region))

for cloud in itertools.cycle(amp_clouds_failover_list(args.region)):
    amp_region,amp_cloud = cloud.split('=')
    write_amp_cloud_to_file(amp_cloud,amp_region)
    logging.warning("Re-starting amp-scanner with the new region {0} and cloud {1}.".format(amp_region,amp_cloud))
    restart_application()
    first_failure_time = None
    while True:
        latency_result = check_network_latency()
        logging.info("while True: Initial Network Latency is {0} Mbit/s".format(latency_result))
        if latency_result and latency_result < 100:
            logging.warning("Network Latency is CRITICAL - {0}Mbit/s! Waiting for additional 25 sec before Amp Cloud checking".format(latency_result))
            time.sleep(25)
        logging.info("Waiting for regular 15 sec before Amp Cloud Availability checking")
        time.sleep(15) # Frequency
        result = check_amp_cloud_availability()
        logging.info("Amp cloud is available: {0}".format(result))
        if not result:
            if first_failure_time is None :
                first_failure_time = datetime.now()
                logging.error("!!!!!!!!!! FAILURE_TIME {0} - connecting to {1}".format(first_failure_time,amp_cloud))
            if (datetime.now() - timedelta(minutes = 1)) > first_failure_time :
                # The next message is used by DD log-based monitor "AMP Cloud Failover detected"
                logging.warning("Waited for 1 min. Application restarting due to failure with Amp: {0}".format(amp_cloud))
                break
        else:
            first_failure_time = None