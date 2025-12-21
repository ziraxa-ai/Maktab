
import csv
import os


# print("Welcome To the store management program")

# password = "admin"

# for i in range(3):
#     user_password = input("Enter password: ")

#     if user_password == password:
#         print("Access Granted!")
#         break
#     else:
#         print("Access Denied!")


products = []

while True:
    os.system('cls')
    more = input("How can I help you?\n " \
    "1. Add a new product \n" \
    "2. Inventory and asset review\n" \
    "3. Sort  \n" \
    "4. edit and delete\n" \
    "5. Show all products \n" \
    "6. Exit \n" \
    "Select the code (1, 2, 3, 4, 5, 6): ")




    if more == "1":
        while True:
            os.system("cls")
            product_name = input("Enter product name: ")
            product_category = input("Enter product category: ")
            product_quantity = int(input("Enter product quantity: "))


            # price
            while True :
                os.system("cls")
                product_price = int(input("Enter product price(More than 3 pieces!!!): "))
                if product_price: 
                    product_price_str = str(product_price)

                    if len(product_price_str) > 3 :
                        break

                else:
                    continue


            # country
            while True:
                os.system("cls")
                product_country = input("Enter the country of manufacture?(a.China b. Iran)")

                if product_country == "a":
                    product_country = "China"
                    break

                elif product_country == "b":
                    product_country = "Iran"
                    break

                else:
                    continue


            if   product_name == "" or product_category == "" or product_quantity < 0:
                print("Invalid product details. Please try again.")
                continue

            else:
                # ID
                price_str = str(product_price)
                
                first_three = ""
                for character in price_str[:3]:
                    first_three += character

                reverse_three = ""
                for character in first_three:
                    reverse_three = character + reverse_three

                product_ID = product_category[0]+ product_country[:2]+product_name[0]+reverse_three


                # add file  csv

                with open('products.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Name", "Category", "Quantity", "Price", "Country"]) if os.stat('products.csv').st_size == 0 else None
                    writer.writerow([product_ID, product_name, product_category, product_quantity, product_price, product_country]) 

                another = input("Add another product? (yes/no): ")

                if another == "yes": 
                    continue

                else:
                    print("Returning to main menu.")
                    break


    elif more == "2":
        while True:
            os.system("cls")
            another = input("From the options\n" \
            "a.Average\n" \
            "b.Most expensive and Cheapest\n" \
            "c.Sum of products and prices (asset)\n" \
            "d.Sales status (chart)\n" \
            "e.Chatbot\n" \
            "Select the desired option(a, b, c, d, e):")

            if another == "a":

                with open("products.csv", mode='r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                        total_price += float(row[4])
                        count += 1

                if count > 0:
                    average_price = total_price / count
                    print(f"The average price of products is: {average_price:.2f}")

                else:
                    input("No products available. \N"\
                    "Press Enter to return to main menu.")

            elif another == "b":


                    if len(products) > 0:
                        cheapest_product = products[0]
                        most_expensive_product = products[0]

                        for p in products:
                            price = float(p[4])

                            if price < float(cheapest_product[4]):
                                cheapest_product = p

                            if price > float(most_expensive_product[4]):
                                most_expensive_product = p

                        print(f"Cheapest Product: ID: {cheapest_product[0]}, Name: {cheapest_product[1]}, Category: {cheapest_product[2]}, Quantity: {cheapest_product[3]}, Price: {cheapest_product[4]}")
                        print(f"Most Expensive Product: ID: {most_expensive_product[0]}, Name: {most_expensive_product[1]}, Category: {most_expensive_product[2]}, Quantity: {most_expensive_product[3]}, Price: {most_expensive_product[4]}")

                    else:
                        input("NO products available.\n"
                            "press Enter to return to main menu .")
            
            elif another == "c":
                os.system("cls")
                products = []

                with open ("products.csv", mode="r") as file:
                    reader = reader(file)
                    next(reader)

                    sum_quantity = 0
                    sum_prices = 0
                    for row in reader:
                        products.append(row)

                    for product in products:
                        sum_quantity += product[3]
                        sum_prices += product[4]

                    print(f"Total price of products: {sum_prices}")
                    print(f"Total number of products: {sum_quantity}")

            elif another == "d":
                pass

            elif another == "e":
                pass


            else:
                        input("Please choose between (a, b, c, d, e, f) \n"\
        "Press Enter to return to main menu.")                


    elif more == "3":
        os.system("cls")

        products = []
        with open("products.csv", mode="r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                products.append(row)

        while True:
            another = input("a. High to Low \n" \
            "b. Low to High\n" \
            "c. By Price\n" \
            "d. By name")
            
            if another == "a":
                while True:
                    os.system("cls")

                    for i in range(len(products)):
                        for j in range(i + 1, len(products)):
                            if float(products[i][4]) < float(products[j][4]):
                                products[i], products[j] = products[j], products[i]

                    print("Products sorted from high to low price:")
                    for product in products:
                        print(product)

                    break

            elif another == "b":
                while True:
                    os.system("cls")

                    for i in range(len(products)):
                        for j in range(i + 1, len(products)):
                            # مقایسه قیمت‌ها
                            if float(products[i][4]) > float(products[j][4]):
                                # جابه‌جایی محصولات
                                products[i], products[j] = products[j], products[i]

                    print("Products sorted from low to high price:")
                    for product in products:
                        print(product)

                    break

            elif another == "c":
                while True:
                    sort_price = input("Enter the price to sort by: ")
                    os.system("cls")
                    filtered_products = [product for product in products if float(product[4]) == float(sort_price)]
                    print(f"Products with price {sort_price}:")
                    for product in filtered_products:
                        print(product)  

            elif another == "d":
                sort_name = input("Enter the name to sort by: ")
                while True:
                    os.system("cls")
                    for product in products:
                        for i in range(len(products)):
                            if products[i][1] == product[1]:
                                print(product)
                    break   

            else:
                input("Please choose between (a, b, c, d)\n"\
        "Press Enter to return to main menu.")


    elif more == "4":
        products = []
        with open("products.csv", mode="r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                products.append(row)
        while True:
            another = input("a. Edit product\n" \
            "b. Delete product\n" \
            "c. View product details\n")

            if another == "a":
                product_id = input("Enter product ID to edit: ")
                for product in products:
                    if product[0] == product_id:
                        new_name = input("Enter new product name: ")
                        new_price = input("Enter new product price: ")
                        new_quantity = input("Enter new product quantity: ")
                        product[1] = new_name
                        product[4] = new_price
                        product[3] = new_quantity
                        print("Product updated successfully.")
                        break
                else:
                    print("Product not found.")

            elif another == "b":
                product_id = input("Enter product ID to delete: ")
                for product in products:
                    if product[0] == product_id:
                        products.remove(product)
                        print("Product deleted successfully.")
                        break
                else:
                    print("Product not found.")

            elif another == "c":
                product_id = input("Enter product ID to view details: ")
                for product in products:
                    if product[0] == product_id:
                        print("Product Details:")
                        print(f"ID: {product[0]}")
                        print(f"Name: {product[1]}")
                        print(f"Price: {product[4]}")
                        print(f"Quantity: {product[3]}")
                        break
                else:
                    print("Product not found.")

            else:
                input("Please choose between (a, b, c)\n"\
        "Press Enter to return to main menu.")


    elif more == "5":
        os.system("cls")
        products = []
        with open("products.csv", mode="r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                products.append(row)

        print("All Products:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Quantity: {product[3]}, Price: {product[4]}, Country: {product[5]}")

        input("Press Enter to return to main menu.")


    elif more == "6":
        print("Exiting the program. Goodbye!")
        break


    else:
        input("Please choose between (1-7)\n"\
        "Press Enter to return to main menu.")
