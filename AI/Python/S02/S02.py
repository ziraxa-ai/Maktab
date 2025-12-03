#EX 01 

age = int(input("Enter your age: "))

if age  >= 18:
    print("You are an adult.")

else:
    print("You are a minor.")

## EX 02

score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
if score >= 75:
    print("Grade: B")
if score >= 50:
    print("Grade: C")
else:
    print("Grade: F")


# EX 03

score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")


#EX 04


# elif = > اما اگر

# EX 05

print("Welcome to contact list .")

contact_name = input("Enter contact name: ")
contact_family = input("Enter contact family: ")
contact_age = int(input("Enter contact age: "))

license = input("View profile? (yes/no): ")

if license == "yes":
    print("Contact Name:", contact_name)
    print("Contact Family:", contact_family)
    print("Contact Age:", contact_age)

elif license == "no":
    print("Profile viewing canceled.")

else:
    print("Invalid input. Please enter 'yes' or 'no'.")



#EX 06


print("Welcome to contact list .")

contact_name = input("Enter contact name: ")
contact_family = input("Enter contact family: ")
contact_age = int(input("Enter contact age: "))

if contact_name == "":
    print("Contact name is required.")
    contact_name = input("Enter contact name: ")

if contact_family == "":
    print("Contact family is required.")
    contact_family = input("Enter contact family: ")

if contact_age <= 0:
    print("Invalid age. Age must be positive.")
    contact_age = int(input("Enter contact age: "))

else:
    res = input("View profile? (yes/no): ")
    if res == "yes":
        print("Contact Name:", contact_name)
        print("Contact Family:", contact_family)
        print("Contact Age:", contact_age)
    elif res == "no":
        print("Profile viewing canceled.")

    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        res1 = input("View profile? (yes/no): ")

        if res1 == "yes":
            print("Contact Name:", contact_name)
            print("Contact Family:", contact_family)
            print("Contact Age:", contact_age)

        elif res1 == "no":
            print("Profile viewing canceled.")
        
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
# ----------------------------------------------------------------------------------------------

# EX 07

for i in range(1, 6):
    print("Iteration:", i)



# ----------------------------------------------------------------------------------------------
password = ""

while password != "admin123":
    password = input("Enter password: ")

print("Access Granted!")


x = 10
while x > 0:
    print(x)
    x -= 1

# ----------------------------------------------------------------------------------------------
# break, continue , pass
# or , and , not


# EX 08
print("Welcome to contact list .")

password = "1234"

for i in range(3):
    user_password = input("Enter password: ")

    if user_password == password:
        print("Access Granted!")
        break
    else:
        print("Access Denied!")

while True:
    contact_name = input("Enter contact name: ")
    contact_family = input("Enter contact family: ")
    contact_age = int(input("Enter contact age: "))


    if contact_name == "" and contact_family == "" and contact_age <= 0:
        print("Contact name is required.")
        continue

    else:
        break

while True:
    license = input("View profile? (yes/no): ")

    if license == "yes":
        print("Contact Name:", contact_name)
        print("Contact Family:", contact_family)
        print("Contact Age:", contact_age)

    elif license == "no":
        print("Profile viewing canceled.")

    else:
        print("Invalid input. Please enter 'yes' or 'no'.")