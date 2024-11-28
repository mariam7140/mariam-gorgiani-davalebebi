import json

user_max_quantity = {}
user_total_purchase = {}
product_sales = {}
total_cost = 0
total_quantity = 0
purchase_count = 0

with open("data.txt", "r") as data_file:
    for line in data_file:
        user_name, product_name, amount, price = line.strip().split(",")
        amount = int(amount)
        price = int(price)

        purchase_cost = amount * price
        total_cost += purchase_cost
        total_quantity += amount
        purchase_count += 1

        if user_name not in user_max_quantity or amount > user_max_quantity[user_name]:
            user_max_quantity[user_name] = amount

        user_total_purchase[user_name] = user_total_purchase.get(product_name, 0) + amount

max_quantity = max(user_max_quantity.values())
users_max_quantity = [user for user, quantity in user_max_quantity.items() if quantity == max_quantity]

max_purchase_amount = max(user_total_purchase.values())
users_max_purchase = [user for user, total in user_total_purchase.items() if total == max_purchase_amount]

max_product_sales = max(product_sales.values())
most_sold_products = [product for product, quantity in product_sales.items() if quantity == max_product_sales]

average_cost = total_cost / purchase_count
average_quantity = total_quantity / purchase_count

stats = {
    "user_max_quantity": users_max_quantity,
    "user_max_purchase_amount": users_max_purchase,
    "average_purchase_cost": round(average_cost, 2),
    "average_purchase_quantity": round(average_quantity, 2),
    "most_sold_products": most_sold_products,
}

with open("stats.json", "w") as stats_file:
    json.dump(stats, stats_file, indent=4, ensure_ascii=False)

print("Statistics have been written to stats.json.")

# ამ ორ დავალებაში რეალურად ვერ ვამოწმებ სწორად გავაკეთე თუ არა, იმიტომ, რომ კოდს როცა ვუშვებ, მეუბნება, რომ data.txt ფაილი არ არსებობს
# ჩატ გპტს ვკითხე და მაგის მიხედვით დავამატე data.txt ფაილი ამ დავალების ფოლდერში მაგრამ მაინც არ კითხულობს
# შეიძლება, რომ txt გაფართოების ფაილს ვერ კითხულობს ჩემი vscode და რამე უნდა დავაინსტალირო?
# მადლობაა <3333
