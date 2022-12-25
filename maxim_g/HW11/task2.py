

def check_week_day(day):
    week_days = {
                1: 'Monday',
                2: 'Tuesday',
                3: 'Wednesday',
                4: 'Thursday',
                5: 'Friday',
                6: 'Saturday',
                7: 'Sunday'
                }
    try:
        if type(day) == str:
            raise ValueError
        week_day = week_days[day]
        print(f'Your entered number is equivalent to **{week_day}** the days of the week.')
    except KeyError:
        print(f'The number you entered does not match more than one or seven')
    except ValueError:
        print('You entered the wrong shell data type is string')


check_week_day(3)
check_week_day(9)
check_week_day("hello")
