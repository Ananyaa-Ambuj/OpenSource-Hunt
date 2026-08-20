def is_leap_year(year):
    if year % 4 == 0:
        return True

    return False


def days_in_month(month, year):
    days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return days.get(month, 0)


def is_valid_date(day, month, year):
    max_days = days_in_month(month, year)

    return day > 0 and day <= max_days


def main():
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))

    if is_valid_date(day, month, year):
        print("Valid date")
    else:
        print("Invalid date")


if __name__ == "__main__":
    main()