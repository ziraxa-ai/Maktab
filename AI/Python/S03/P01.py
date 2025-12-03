#project 
import os


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
    "7. Exit \n"
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
                product["id"] = product_id
                product["name"] = product_name
                product["category"] = product_category
                product["quantity"] = product_quantity
                product["price"] = product_price
                products.append(product)

                more = input("Add another product? (yes/no): ")
                if more == "yes":
                    continue

                else:
                    print("Invalid input. Returning to main menu.")
                    break

    elif more == "2":
        if len(products) == 0:
            print("No products available to calculate average price.")
        
        else:
            total_price = 0 
            for product in products:
                total_price += product["price"]
            average_price = total_price / len(products)
            print("Average price of products:", average_price)

        # else:
        #     total_price = sum(product["price"] for product in products)
        #     average_price = total_price / len(products)
        #     print("Average price of products:", average_price)

    elif more == "3":
        sorted_prices = int(input("Enter the price you want to sort by:"))
        sort_by = input("Sort by price ascending or descending? (a.less , b.more): ")

        if sort_by == "a":
            for product in products:
                if product["price"] <= sorted_prices:
                    print(product)

        elif sort_by == "b":
            for product in products:
                if product["price"] >= sorted_prices:
                    print(product)
        
        else:
            print("Invalid input. Please enter a or b.")

    elif more == "4":
        if len(products) == 0:
            print("No products available.")
        
        else:
            choice = input("Do you want to see the cheapest or most expensive product? (c.cheapest , m.most expensive): ")

            if choice == "c":
                cheapest = products[0]
                for product in products:
                    if product["price"] < cheapest["price"]:
                        cheapest = product
                print("Cheapest product:", cheapest)

            elif choice == "m":
                most_expensive = products[0]
                for product in products:
                    if product["price"] > most_expensive["price"]:
                        most_expensive = product
                print("Most expensive product:", most_expensive)

            else:
                print("Invalid input. Please enter c or m.")

    elif more == "5":
        if len(products) == 0:
            print("No products available.")
        
        else:
            order = input("Sort products by price ascending or descending? (a.ascending , d.descending): ")

            if order == "a":
                print("Products sorted by price (ascending):")
                for product in products:
                    if product["price"] < sorted_prices:
                        print(product)

            

            elif order == "d":
                print("Products sorted by price (descending):")
                for product in products:
                    if product["price"] > sorted_prices:
                        print(product)

            else:
                print("Invalid input. Please enter a or d.")
        

    elif more == "6":
        if len(products) == 0:
            print("No products available.")
        
        else:
            print("All products:")
            for product in products:
                print(product)

    elif more == "7":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid selection. Please try again.")