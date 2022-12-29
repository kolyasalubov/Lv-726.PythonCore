def the_day_of_the_week():
    try:
        day = int(input("Write number of the day: "))
        if day <= 0 or day >= 7:
            print("Please enter number from 1 to 7")

    except ValueError:
        print("Please write an integer number: ")
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

the_day_of_the_week()