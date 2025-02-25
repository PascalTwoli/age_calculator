from datetime import date
from dateutil.relativedelta import relativedelta

# get todays date
today = date.today()
print (today)

# get user input
try:
    birth_year = int(input("Enter your birth year (YYYY): "))
    birth_month = int(input("Enter your birth month (MM): "))
    birth_day = int(input("Enter your birht day (DD): "))

    # create birth date object
    birth_date = date(birth_year, birth_month, birth_day)

    age_diff = relativedelta(today, birth_date)

    print(f"\nYour current age is {age_diff.years} Years, {age_diff.months} Months, {age_diff.days} Days")

except ValueError: 
    print ("Invalid input! Please enter valid numbers for year, month and day")
except: 
    print("An error occured! Please enter a valid birth date")
