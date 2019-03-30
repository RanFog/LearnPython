year = input("Введите год: ")
year = int(year)
print(year)
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap)

import calendar
print (calendar.isleap(1980))