# datetime მოდული

import datetime

# მიიღოს დაბადების წელი, თვე, დღე

year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month (number): "))
day = int(input("Enter your birth day (number): "))

# მონაცემი datetime-ით გარდაქმნას თარიღად

birthday = datetime.date(year, month, day)

# თარიღიდან მიიღოს კვირის დღე
# %A დირექტივით დაწეროს სრული კვირის დღე

weekday = birthday.strftime("%A")

# დაბეჭდოს მომხმარებლის დაბადების კვირის დღე

print("you were born on", weekday)