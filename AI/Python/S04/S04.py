# EX 01

# نوشتن در فایل 

file = open("note.txt", "w")
file.write("Hello World!")
file.write("\nWelcome to Python programming.")
file.close()

# خواندن فایل
file = open("note.txt", "r")
content = file.read()
print(content)
file.close()

# افزودن متن جدید
file = open("note.txt", "a")
file.write("\nThis is an additional line.")
file.close()

# خواندن + نوشتن

file = open("note.txt", "r+")
content = file.read()
file.write("\nThis is an additional line.")
file.close()
print(content)

# باز کردن فایل در حالت باینری

file = open("note.txt", "rb")
content = file.read()
print(content)
file.close()

#  ادامه در فایل Study04.md

# EX 02 , 03 , 04

# Write Mode
with open("note.txt", "w") as f:
    f.write("Hello World!")
    f.write("\nWelcome to Python programming.")


# Read Mode
with open("note.txt", "r") as f:
    content = f.read()
    print(content)  

# Append Mode
with open("note.txt", "a") as f:
    f.write("\nThis is an additional line.")


# EX 05


import csv

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "field"])
    writer.writerow(["Taha", 23, "AI"])
    writer.writerow(["Sara", 21, "ML"])

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# EX 06

#Ess 01 

import csv
import os


while True:
    more = input("Choose an option:\n1. Add Product\n2. Sort products by price\n3. show product \n4. Exit\nEnter your choice: ")

    if more == "1":
        while True:
            os.system('cls')
            product_name = input("Enter product name: ")
            product_category = input("Enter product category: ")
            product_price = float(input("Enter product price: "))

            with open("products.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                product_id = sum(1 for row in open('products.csv'))  # Simple way to generate product ID
                writer.writerow(["ID", "Name", "Category", "Price"]) if os.stat('products.csv').st_size == 0 else None
                writer.writerow([product_id, product_name, product_category, product_price])
            another = input("Add another product? (yes/no): ")
            if another == "yes":
                continue
            else:
                print("Returning to main menu.")
                break

    elif more == "2":
        os.system("cls")
        products = []
        with open("products.csv", mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                products.append(row)
        if products:
            # Sort products by price (ascending)
            for i in range(len(products) - 1):
                for j in range(0, len(products) - i - 1):
                    if float(products[j][3]) > float(products[j + 1][3]):
                        products[j], products[j + 1] = products[j + 1], products[j]
            print("Products sorted by price:")
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Price: {product[3]}")
        else:
            print("No products available.")
        input("Press Enter to return to main menu.")

    elif more == "3":
        os.system("cls")
        products = []
        with open("products.csv", mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                products.append(row)
        if products:
            # Sort products by price (ascending)
            for i in range(len(products) - 1):
                for j in range(0, len(products) - i - 1):
                    if float(products[j][3]) > float(products[j + 1][3]):
                        products[j], products[j + 1] = products[j + 1], products[j]
            print("Products sorted by price:")
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Price: {product[3]}")
        else:
            print("No products available.")
        input("Press Enter to return to main menu.")
    

    elif more == "4":
        print("Exiting the program.")
        break