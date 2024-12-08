import json

# json ფაილის წაკითხვა
with open("homework_1_markets.json", "r") as stores_file:
    stores_data = json.load(stores_file)

with open("homework_1_recipes.json", "r") as recipes_file:
    recipes_data = json.load(recipes_file)

# user ვკითხოთ რომელი კერძის მომზადება უნდა
print("Available dishes:")
for dish in recipes_data.keys():
    print("- " + dish)

dish_name = input("Enter the name of the dish you want to prepare: ")

# არის თუ არა კერძი რეცეპტებში
if dish_name not in recipes_data:
    print("Sorry, this dish is not available.")
else:
    # არჩეული კერძის ინგრედიენტების "მოგროვება"
    required_ingredients = recipes_data[dish_name]["ingredients"]

    # რომელ მაღაზიაშია ინგრედიენტები
    stores_needed = []
    missing_ingredients = []

    for ingredient in required_ingredients:
        found_in_store = False  # არის თუ არა ინგრედიენტი ხელმისაწვდომი მაღაზიაში
        for store, products in stores_data.items():
            if ingredient in products:
                found_in_store = True
                if store not in stores_needed:
                    stores_needed.append(store)
                break  # თუ ინგრედიენტი ვიპოვეთ, სხვა მაღაზიებში ძიების შეწყვეტა
        if not found_in_store:
            missing_ingredients.append(ingredient)

    # შედეგის დაპრინტვა
    if missing_ingredients:
        print(f"Sorry, you can't prepare '{dish_name}' because the following ingredients are missing:")
        print(", ".join(missing_ingredients))
    else:
        print(f"To prepare '{dish_name}', you need to visit the following stores:")
        print(", ".join(stores_needed))
