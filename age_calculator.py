# age_calculator.py

import datetime

current_year = datetime.datetime.now().year
current_month =  datetime.datetime.now().month
current_day = datetime.datetime.now().day
# age =  current_year - int(birth_year)
print ("current year ", current_year)
print ("current month", current_month)
print ("current date", current_day)

today_as_number = float(current_year) + float(current_month/12) + float(current_day/365)
print("Today: ", today_as_number)

birth_year = input ("Enter your birth year: ")
birth_month = input ("Enter your birth month: ")
birth_day =  input ("Enter your birth day: ")

print ("birth date: ", birth_day, "/",birth_month, "/", birth_year)


birth_date_number = float(birth_year) + (float(birth_month)/12) + (float(birth_day)/365)
print ("Birth_day: ", birth_date_number)

age_number = today_as_number - birth_date_number
print ("Age number: ", age_number)

# getting the age in years, days and months

years = int(age_number)
print ("years: ",years)
months_fraction = age_number - years
print ("months fraction: ", months_fraction)
months_decimal = months_fraction * 12
print ("months decimal: ", months_decimal)
months = int(months_decimal)
print ("months: ", months)
days_fraction = months_decimal - months
print ("days fraction: ", days_fraction)
days_decimal = days_fraction * 30
print ("days fraction: ", days_decimal)
days = int (days_decimal)
print ("days : ", days)
print ("Your  current age is: ", years, " Years, ", months, " Months, ", days, " Days")