import datetime
from datetime import timedelta

def get_year():
    year = input("Enter the  year\n")
    try:
        val = int(year)
        if val > 0:
            if len(str(val)) == 4:
                return val
            else:
                print("Enter four digits for year")
                return get_year()
                
    except ValueError:
        print("This is not a Number.\nPlease enter a valid Number")
        return get_year()
        


def get_month():
    month = input("Enter a Month\n")
    try:
        val = int(month)
        if (val > 0 and val <= 12):
            return val
        else:
            print("Enter a digit between 1 and 12")
            return get_month()
    except ValueError:
        print("This is not a Number.\nPlease enter a valid Number")
        return get_month()
        

def get_day(month_value):
    
    month_value = int(month_value)

    day = input("Enter a Day\n")
    val = int(day)
    
    if (val > 0 and val <= 30) and (month_value in [4, 6, 9, 11]): # and (val < 31):
        print("Day is: ", val)
        
    elif (val > 0 and val <= 28) and (month_value == 2):
        print("Day is: ", val)
        
    elif (val > 0 and val <= 31) and (month_value in [1, 3, 5, 7, 8, 10, 12]):
        print("Day is: ", val)
    else:
        print("Day is out of range for this month")
        return get_day(month_value)

    return val


def get_date_format():
    
    print("Now getting first year...")
    first_year = get_year()
    first_month = get_month()
    first_day = get_day(first_month)
    print(f"You selected: {first_year}/{first_month}/{first_day}")
    date_one = datetime.date(int(first_year), int(first_month), int(first_day))

    
    print("\n Now getting second year... \n")
    second_year = get_year()
    second_month = get_month()
    second_day = get_day(second_month)
    print(f"You selected: {second_year}/{second_month}/{second_day}")
    
    date_two = datetime.date(int(second_year), int(second_month), int(second_day))
    
    return date_one, date_two

def date_difference():
    date_one, date_two = get_date_format()
    
    if date_two > date_one:
        print("\n Date one cannot be subtracted from date two. Try Again \n")
        return date_difference()
        
    else:
        return (date_one - date_two).days

        
days = date_difference()
print("Difference in days is:", days)