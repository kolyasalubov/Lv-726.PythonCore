class NonExistDayError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)


def days_of_the_week():
    try:
        day = int(input("Enter number of the day :"))
        if day <=1 or day >= 7 :
            raise NonExistDayError("Week have only 7 days , please enter number \
                            from 1 to 7!")
    except ValueError:
        print("Please enter an integer number!")
    else:
        if day == 1:
            print("Monday")
        elif day == 2:
            print("Tuesday")
        elif day == 3:
            print("Wednesday")
        elif day == 4:
            print("Thursday")
        elif day == 5:
            print("Friday") 
        elif day == 6:
            print("Saturday")     
        elif day == 7:
            print("Sunday")      

days_of_the_week()