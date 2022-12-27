def f(days: dict) -> str:
    day_num = input("Enter day's num: ")
    if day_num not in "0123456789":
        raise TypeError("You should enter integer number [1-7].")

    day_num = int(day_num)
    if day_num not in days.keys():
        raise ValueError("Week has only 7 days!")

    return f"{day_num} is {days[day_num]}"


def main():
    week_days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    print(f(week_days))


if __name__ == "__main__":
    main()
