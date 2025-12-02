import os
import csv

print("Welcome to the store management program.")

password = "admin"

for i in range(3):
    user_password = input("Enter password: ")

    if user_password == password:
        print("Access Granted!")
        break
    else:
        print("Access Denied!")

products = []

while True:
    os.system('cls')
    more = input("How can I help you?\n " \
    "1. Add a new product \n" \
    "2. Calculate the average price of products.\n" \
    "3. Sort by price... and print \n" \
    "4. Print the cheapest or most expensive product \n" \
    "5. Print the products in order of expensive to cheap or cheap to expensive \n" \
    "6. Show all products \n" \
    "7. Exit \n" \
    "Select the code (1, 2, 3, 4, 5, 6, 7): ")

    if more == "1":
        while True:
            os.system('cls')
            product = {}
            product_id = input("Enter product ID: ")
            product_name = input("Enter product name: ")
            product_category = input("Enter product category: ")
            product_quantity = int(input("Enter product quantity: "))
            product_price = float(input("Enter product price: "))

            if product_id == "" or product_name == "" or product_category == "" or product_price <= 0 or product_quantity < 0:
                print("Invalid product details. Please try again.")
                continue

            else:
                with open('products.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Name", "Category", "Quantity", "Price"]) if os.stat('products.csv').st_size == 0 else None
                    writer.writerow([product_id, product_name, product_category, product_quantity, product_price]) 
                more = input("Add another product? (yes/no): ")
                if more == "yes": 
                    continue
                else:
                    print("Returning to main menu.")
                    break


    elif more == "2":
        os.system('cls')
        total_price = 0
        count = 0
        with open('products.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                total_price +=  float(row[4])
                count += 1

        if count > 0:
            average_price = total_price / count
            print(f"The average price of products is: {average_price:.2f}")

        else:
            print("No products available to calculate average price.")
        input("Press Enter to return to main menu.")

    elif more == "3":
        os.system('cls')
        with open('products.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            products = [row for row in reader]

        if products:
            products.sort(key=lambda x: float(x[4]))
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Quantity: {product[3]}, Price: {product[4]}")
        else:
            print("No products available.")
        input("Press Enter to return to main menu.")


    elif more == "4":
        pass

    elif more == "5":
        pass

    elif more == "6":
        if len(products) == 0:
            print("No products available.")
        
        else:
            products = []
            os.system('cls')
            with open('products.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    products.append(row)
            if len(products) > 0:
                for product in products:
                    print(f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Quantity: {product[3]}, Price: {product[4]}")
            
            else:
                print("No products available.")
            input("Press Enter to return to main menu.")
