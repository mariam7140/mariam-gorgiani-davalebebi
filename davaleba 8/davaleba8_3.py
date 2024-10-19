from datetime import datetime

input_date = input("Please enter date: ")  

corrected_date = datetime.fromisoformat(input_date)

year = corrected_date.year
month = corrected_date.month
day = corrected_date.day
hour = corrected_date.hour
minute = corrected_date.minute
second = corrected_date.second
timezone = corrected_date.tzinfo


print(f"{day}-{month}-{year} {hour}:{minute}:{second} {timezone}")