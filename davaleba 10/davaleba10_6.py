from datetime import datetime

def car():
    brand = input("Please enter the car name: ")
    year = input("Please enter the car year: ")

    if not year:
        year = datetime.now().year
    else:
        year = int(year)


    return f"car: {brand}, year: {year}"


print(car())