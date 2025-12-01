
# EX 09--------------------------------------------------------

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
    contact = []
    contact_name = input("Enter contact name: ")
    contact_family = input("Enter contact family: ")
    contact_age = int(input("Enter contact age: "))


    if contact_name == "" and contact_family == "" and contact_age <= 0:
        print("Contact name is required.")
        continue
    else:
        contact.append(contact_name)
        contact.append(contact_family)
        contact.append(contact_age)
        contacts.append(contact)
        more = input("Add another contact? (yes/no): ")
        if more.lower() != "yes":
            break