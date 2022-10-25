def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("This is a leap year")
            else:
                print("This is not a leap year")
        else:
            print("This is a leap year!")
    else:
        print("This is not a leap year")


is_leap_year(2000)
is_leap_year(2013)
is_leap_year(1500)
