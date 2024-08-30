check_leap_year = 2024
y = check_leap_year

if (y%400==0) or (y%4==0 and y%100!=0):
    print("it is leap year",check_leap_year)
else:
    print("oh oh sorry, it's not aleap year")
