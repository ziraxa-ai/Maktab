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



#EX 05


print("Welcome to contact list .")

contact_name = input("Enter contact name: ")
contact_family = input("Enter contact family: ")
contact_age = int(input("Enter contact age: "))

while 
    license = input("View profile? (yes/no): ")
