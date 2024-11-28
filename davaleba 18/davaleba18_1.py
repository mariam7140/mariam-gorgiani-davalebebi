import os
print("Current working directory:", os.getcwd())

# data.txt წაკითხვა და შესყიდვების კატეგორიებად დაყოფა

with open("data.txt", "r") as data_file, \
    open ("small.txt", "w") as small_file, \
    open ("high.txt", "w") as high_file:

    for line in data_file: # დატა ფაილის თითოეული ხაზის წაკითხვა
        user_name, product_name, amount, price = line.strip().split(",") # დავწრმუნდეთ რომ მძიმით არის მონაცემები გამოყოფილი
        amount = int(amount)
        price = int(price)

        if price < 10:
            small_file.write(line)
        else:
            high_file.write(line) 