import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI
"""
in this project I used:
- Virtual Enviroment
- Modules, Packages and Classes
- Methods with Parameters
- API
- Decorators
- OOP
- Functions
- GLobal Variables
- F-strings

"""


bot = telebot.TeleBot('5927150339:AAGeCKDjOTkfZOc6qzTvtme2eKHtJJpKXAU')
cg = CoinGeckoAPI()



@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, {message.from_user.first_name} {message.from_user.last_name}'
    q_size = f'Set the size of your investment portfolio. Enter the amount:'
    bot.send_message(message.chat.id, mess)
    bot.send_message(message.chat.id, q_size)


@bot.message_handler()
def get_user_text(message):
    global u_amount
    u_amount = message.text
    if message.text.isdigit() == True:
        u_size = f"Your budget is ${message.text}"
        bot.send_message(message.chat.id,u_size)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button_btc = types.KeyboardButton('BTC')
        button_eth = types.KeyboardButton('ETH')
        button_usdt = types.KeyboardButton('USDT')
        button_bnb = types.KeyboardButton('BNB')
        markup.add(button_btc, button_eth,button_usdt, button_bnb)
        ut = bot.send_message(message.chat.id,'What assets would you like to buy?',reply_markup=markup)
        bot.register_next_step_handler(ut, crypto_choice)
    else:
        bot.send_message(message.chat.id,"Please enter a number:")
        

def crypto_choice(message):
    global new_price , crypto
    if message.text == 'BTC':
        price = cg.get_price(ids='bitcoin', vs_currencies='usd')
        bot.send_message(message.chat.id, f'Bitcoin = {price["bitcoin"]["usd"]}$')
    if message.text == 'ETH':
        price = cg.get_price(ids='ethereum', vs_currencies='usd')
        bot.send_message(message.chat.id, f'Ethereum = {price["ethereum"]["usd"]}$')
    if message.text == 'USDT':
        price = cg.get_price(ids='tether', vs_currencies='usd')
        bot.send_message(message.chat.id, f'Tether = {price["tether"]["usd"]}$')
    if message.text == 'BNB':
        price = cg.get_price(ids='binancecoin', vs_currencies='usd')
        bot.send_message(message.chat.id, f'Binancecoin = {price["binancecoin"]["usd"]}$')
    for k,v in price.items():
        new_price = v['usd'] 
        crypto = k   
    bnb_buy(message)
    
    
def bnb_buy(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    f_option = types.KeyboardButton('25%')
    s_option = types.KeyboardButton('50%')
    t_option = types.KeyboardButton('75%')
    fo_option = types.KeyboardButton('100%')
    markup.add(f_option,s_option,t_option,fo_option)
    bb = bot.send_message(message.chat.id,"For what amount you want to make a purchase?",reply_markup=markup)
    bot.register_next_step_handler(bb, result)


def result(message):    
    if message.text == '25%':
        bot.send_message(message.chat.id, f'You bought {round(((int(u_amount)*0.25)/new_price),2)} {crypto}')
    if message.text == '50%':
        bot.send_message(message.chat.id, f'You bought {round(((int(u_amount)*0.50)/new_price),2)} {crypto}')
    if message.text == '75%':
        bot.send_message(message.chat.id, f'You bought {round(((int(u_amount)*0.75)/new_price),2)} {crypto}')
    if message.text == '100%':
        bot.send_message(message.chat.id, f'You bought {round(((int(u_amount)*1)/new_price),2)} {crypto}')
    last_question(message)


def last_question(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    y_button = types.KeyboardButton('Yes')
    n_button = types.KeyboardButton('No')
    markup.add(y_button, n_button)
    go_main = bot.send_message(message.chat.id,"Would You like to buy more cypto?",reply_markup=markup)
    bot.register_next_step_handler(go_main, last_message)


def last_message(message):
    if message.text == 'Yes':
        bot.send_message(message.chat.id, f'At this point, I must make an important caution: cryptocurrencies\
 remain extremely volatile assets with rapidly changing values. These changes can bring both\
 significant profits and significant financial losses.')
    if message.text == 'No':
        bot.send_message(message.chat.id, f'Thank You for Choosing Us!')


bot.polling(none_stop=True)


