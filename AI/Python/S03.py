# EX 01
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

# EX 02
score = [19, 25, 12, 8, 30, 15, 27, 5, 10, 18]
names = ["Ali", "Sara", "Reza", "Neda", "Hassan", "Mina", "Omid", "Lila", "Kian", "Tina"]

print(score)
print(names)

# EX 03

print(names[0])
print(names[-1])

# EX 04

for name in names:
    print(name)

# EX 05

names.append("Zahra")
names.remove("Reza")
names.extend(["Sara", "Reza"]) # -> اضافه چندین مقدار به لیست
names.insert(1, "Mina") # -> اضافه کردن مقدار در ایندکس مشخص    
names.pop()      # آخرین
names.pop(2)     # اندیس مشخص
names.clear()
names.index("Sara") # -> پیدا کردن ایندکس مقدار مشخص
names.count("Sara") # -> تعداد تکرار مقدار مشخص
names.sort()                 # صعودی
names.sort(reverse=True)     # نزولی
names.reverse()
new_names = names.copy()
len(names)
names[1:4] # -> از ایندکس 1 تا 3
names[::2]  # -> گام دو

# EX 06
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])   # Output: 6

# EX 07

person = {
    "name": "Taha",
    "age": 23,
    "skill": "AI"
}

# EX 08

print(person["name"])      # Output: Taha
print(person.get("age"))   # Output: 23
person["city"] = "Tehran"
person.update({"age": 26})
person.update(job="Engineer")
person.items() # -> کلید و مقدار
person.values() # -> فقط مقادیر
person.keys()   # -> فقط کلیدها
person.pop("skill") # -> حذف کلید و مقدار
person.clear()  # -> پاک کردن کل دیکشنری
person.setdefault("country", "Iran") # -> اگر کلید وجود نداشت اضافه کن
p2 = person.copy()


# EX 09
print("Welcome to contact list .")

password = "1234"
names = []
families = []
ages = []

for i in range(3):
    user_password = input("Enter password: ")

    if user_password == password:
        print("Access Granted!")
        break
    else:
        print("Access Denied!")

while True:
    name = input("Enter contact name: ")
    family = input("Enter contact family: ")
    age = int(input("Enter contact age: "))


    if name != "" and family != "" and age >= 0:
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



