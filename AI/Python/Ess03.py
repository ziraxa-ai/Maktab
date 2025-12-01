#Ess 01 

#print("Hello\nWorld") #New line
#print("Hello\tWorld") #Tab


print("Welcome to contact list .")

password = "1234"
contacts = []

for i in range(3):
    user_password = input("Enter password: ")

    if user_password == password:
        print("Access Granted!")
        break
    else:
        print("Access Denied!")

while True:
    contact = {}
    contact_name = input("Enter contact name: ")
    contact_family = input("Enter contact family: ")
    contact_age = int(input("Enter contact age: "))


    if contact_name == "" and contact_family == "" and contact_age <= 0:
        print("Contact name is required.")
        continue
    else:
        contact["name"] = contact_name
        contact["family"] = contact_family  
        contact["age"] = contact_age
        contacts.append(contact)

        more = input("Should I display my contacts(0) or register a new one(1)? ")

        if more == "0":
            print("Displaying contacts:")
            for contact in contacts:
                print(f"Name: {contact['name']}\nFamily: {contact['family']}\nAge: {contact['age']}")
        elif more == "1":
            continue
        else:
            print("Invalid input. Please enter 0 or 1.")

# Ess 02  --------------------------------------------------------

nums = []

for i in range(5):
    n = int(input("Enter a number: "))
    nums.append(n)

largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print("Largest number is:", largest)

# Ess 03 --------------------------------------------------------

score = []

for i in range(5):
    s = float(input("Enter a score: "))
    score.append(s)

avg = sum(score) / len(score)
print("Average score is:", avg)

if avg >= 75:
    print("You passed!")

elif avg >= 50:
    print("Retry exam!")

else:
    print("You failed!")

# Ess 04 --------------------------------------------------------

names = ["Alice", "Bob", "Charlie", "David", "Eva"]

target = input("Enter a name to search: ")

found = False

for name in names:
    if name == target:
        found = True
        break

if found:
    print(f"{target} found in the list.")

else:
    print(f"{target} not found in the list.")

# Ess 05 --------------------------------------------------------

students = []

for i in range(3):
    student = {}
    student_name = input("Enter student name: ")
    student_age = int(input("Enter student age: "))
    student_grade = float(input("Enter student grade: "))

    student["name"] = student_name
    student["age"] = student_age
    student["grade"] = student_grade

    students.append(student)

print("All Students:")
for name in students:
    print(f"Name: {name['name']}")


# Ess 06 --------------------------------------------------------

Data_set = [{
    "id": 1,"price": 100, "category": "Books"},
    {"id": 2,"price": 200, "category": "Electronics"},
    {"id": 3,"price": 150, "category": "Clothing"},
    {"id": 4,"price": 300, "category": "Books"},
    {"id": 5,"price": 250, "category": "Electronics"},
    {"id": 6,"price": 120, "category": "Clothing"},
    {"id": 7,"price": 180, "category": "Books"},
    {"id": 8,"price": 220, "category": "Electronics"},
    {"id": 9,"price": 130, "category": "Clothing"},
    {"id": 10,"price": 170, "category": "Books"}
]

while True:
    res = input("What help can I provide? " \
    "\n 1.Calculate average prices." 
    "\n 2.Find most expensive item."
    "\n 3.Find the cheapest product." 
    "\n 4.Bring me items under 200."
    "\nPlease enter the number of your choice: ")

    if res == "1":
        total_price = 0
        for item in Data_set:
            total_price += item["price"]
        average_price = total_price / len(Data_set)
        print("Average price:", average_price)

    elif res == "2":
        most_expensive = Data_set[0]
        for item in Data_set:
            if item["price"] > most_expensive["price"]:
                most_expensive = item
        print("Most expensive item:", most_expensive)

    elif res == "3":
        cheapest = Data_set[0]
        for item in Data_set:
            if item["price"] < cheapest["price"]:
                cheapest = item
        print("Cheapest item:", cheapest)

    elif res == "4":
        under_200 = []
        for item in Data_set:
            if item["price"] < 200:
                under_200.append(item)
        print("Items under 200:", under_200)

    else:
        print("Invalid selection \n Try again.")
        continue

# Ess 07 --------------------------------------------------------
# همراه با توضیح یاد گیری کنترل پروژه به کمک گیت هاب و اپشن های گیت هاب

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