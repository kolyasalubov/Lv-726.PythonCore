def week_day(num):
    if num == 1:
        return 'Monday'
    elif num == 2:
        return 'Tuesday'
    elif num == 3:
        return 'Wednesday'
    elif num == 4:
        return 'Thursday'
    elif num == 5:
        return 'Friday'
    elif num == 6:
        return 'Saturday'
    elif num == 7:
        return 'Sunday'

try:
    day = int(input("Enter the day of the week: "))
    if day <= 0 or day >= 8:
        raise ValueError("This should be number between 1 to 7.")
    print(f"{day} is {week_day(day)}")
except ValueError as e:
    print(f"Enter the correct data. {e}")
