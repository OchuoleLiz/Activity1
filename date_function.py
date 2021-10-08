import datetime
from datetime import timedelta

def date_difference (date1, date2):
    while True:
        if date2 > date1:
            return "Date one cannot be subtracted from date two"
        else:
            return (date1 - date2).days




while True:
    year_one = input("Enter the first year\n")
    try:
        val = int(year_one)
        if val > 0:
            if len(str(val)) == 4:
                print("Year one is: ", val)
                break;
            else:
                print("Enter four digits for year")
    except ValueError:
        print("This is not a Number.\nPlease enter a valid Number")

while True:
    month_one = input("Enter a Month\n")
    try:
        val = int(month_one)
        if (val > 0 and val <= 12):
            print("Month one is: ", val)
            break;
        else:
            print("Enter a digit between 1 and 12")
    except ValueError:
        print("This is not a Number.\nPlease enter a valid Number")

day_one = input("Enter a Day\n")
val = int(day_one)
if (val > 0 and val <= 31) or (month_one == 4 or 6 or 9 or 11) and (val > 31):
    print("Day is: ", val)
elif (val > 0 and val <= 31) or (month_one == 2) and (val > 28):
    print("Day is: ", val)
else:
    print("Day is out of range for month")

while True:
    year_two = input("Enter second year\n")
    try:
        val = int(year_two)
        if val > 0:
            if len(str(val)) == 4:
                print("Year two is: ", val)
                break;
            else:
                print("Enter four digits for year")
    except ValueError:
        print("This is not a Number.\nPlease enter a valid Number")

while True:
    month_two = input("Enter second month\n")
    try:
        val = int(month_two)
        if (val > 0 and val <= 12):
            print("Month two is: ", val)
            break;
        else:
            print("Enter a digit between 1 and 12")
    except ValueError:
        print("This is not a Number.\nPlease enter a valid Number")

day_two = input("Enter second day\n")
val = int(day_two)
if (val > 0 and val <= 31) or (month_two == 4 or 6 or 9 or 11) and (val > 31):
    print("Day is: ", val)
elif (val > 0 and val <= 31) or (month_two == 2) and (val > 28):
    print("Day is: ", val)
else:
    print("Day is out of range for month")


date_one = datetime.date(int(year_one), int(month_one), int(day_one))
date_two = datetime.date(int(year_two), int(month_two), int(day_two))


result = date_difference(date_one, date_two)
print(result)
