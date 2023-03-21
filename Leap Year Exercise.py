year = int(input("Type a year to know if it is a Leap year or not: "))


if year / 4 == 0:
    if year / 100 == 0:
        if year / 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is not a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")
