# Ess 01

import os


with open("note.txt", "w") as file:
    for i in range(5):
        note = input(f"Enter note {i+1}: ")
        file.write(note + "\n")

os.system("cls")

with open("note.txt", "r") as file:
    content = file.read()
    print("Notes entered:")
    print(content)

# Ess 02

import os
import csv


while True:
    os.system("cls")
    more = input("Choose an option (1-4)" \
    "\n 1. Add Contact" \
    "\n 2. View Contacts" \
    "\n 3. Search Contact" \
    "\n 4. Delete Contact" \
    "\n 5. Edit Contact" \
    "\n 6. Exit" \
    "\n Your choice: ")

    if more == "1":
        while True:
            os.system('cls')
            contact_name = input("Enter contact name: ")
            contact_phone = input("Enter contact phone number: ")
            contact_email = input("Enter contact email: ")

            if contact_name == "" or contact_phone == "" or contact_email == "":
                print("All fields are required. Please enter the contact details again.")
                continue

            with open('contacts.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Phone", "Email"]) if os.stat('contacts.csv').st_size == 0 else None
                writer.writerow([contact_name, contact_phone, contact_email])

            another = input("Add another contact? (y/n): ")
            if another != 'y':
                break

    elif more == "2":
        os.system("cls")
        rows = []
        with open('contacts.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        for row in rows:
            print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
        input("Press Enter to return to main menu.")

    elif more == "3":   
        os.system("cls")
        rows = []
        with open('contacts.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        for row in rows:
            print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
        input("Press Enter to return to main menu.")

        another = input("Do you want to find using (a.name, b.number, c.email)? (a/b/c): ")
        if another == "a":
            name_search = input("Enter the name to search: ")
            found = False
            for row in rows:
                if row[0] == name_search:
                    print(f"Found Contact - Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
                    found = True
            if not found:
                print("Contact not found.")
            input("Press Enter to return to main menu.")

        elif another == "b":
            number_search = input("Enter the phone number to search: ")
            found = False
            for row in rows:
                if row[1] == number_search:
                    print(f"Found Contact - Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
                    found = True
            if not found:
                print("Contact not found.")
            input("Press Enter to return to main menu.")

        elif another == "c":
            email_search = input("Enter the email to search: ")
            found = False
            for row in rows:
                if row[2] == email_search:
                    print(f"Found Contact - Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
                    found = True
            if not found:
                print("Contact not found.")
            input("Press Enter to return to main menu.")

        
    elif more == "4":
        os.system("cls")
        contacts = []
        with open('contacts.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
        for row in contacts:
            print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
        delete_name = input("Enter the name of the contact to delete: ")
        for row in contacts:
            if row[0] == delete_name:
                print(f"Deleting Contact - Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
                contacts.remove(row)
                break
        with open('contacts.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Phone", "Email"])
            writer.writerows(contacts)
        input("Press Enter to return to main menu.")

    elif more == "5":
        os.system("cls")
        rows = []
        with open('contacts.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        for row in rows:
            print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
        input("Press Enter to return to main menu.")

        another = input("Do you want to find using (a.name, b.number, c.email)? (a/b/c): ")

        if another == "a":
            name_search = input("Enter the name to edit: ")
            for i, row in enumerate(rows):
                if row[0] == name_search:
                    new_name = input("Enter new name: ")
                    new_phone = input("Enter new phone number: ")
                    new_email = input("Enter new email: ")
                    rows[i] = [new_name, new_phone, new_email]
                    print("Contact updated.")
                    break
            with open('contacts.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Phone", "Email"])
                writer.writerows(rows)
            input("Press Enter to return to main menu.")
        
        elif another == "b":    
            number_search = input("Enter the phone number to edit: ")
            for i, row in enumerate(rows):
                if row[1] == number_search:
                    new_name = input("Enter new name: ")
                    new_phone = input("Enter new phone number: ")
                    new_email = input("Enter new email: ")
                    rows[i] = [new_name, new_phone, new_email]
                    print("Contact updated.")
                    break
            with open('contacts.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Phone", "Email"])
                writer.writerows(rows)
            input("Press Enter to return to main menu.")
        
        elif another == "c":
            email_search = input("Enter the email to edit: ")
            for i, row in enumerate(rows):
                if row[2] == email_search:
                    new_name = input("Enter new name: ")
                    new_phone = input("Enter new phone number: ")
                    new_email = input("Enter new email: ")
                    rows[i] = [new_name, new_phone, new_email]
                    print("Contact updated.")
                    break
            with open('contacts.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Phone", "Email"])
                writer.writerows(rows)
            input("Press Enter to return to main menu.")

    elif more == "6":
        print("Exiting the program.")
        break


# Ess 03

# A program that takes a .txt file and tells it the number of characters and lines at the level of elementary and beginner children


file_path = input("Enter the path of the text file: ")

with open(file_path, 'r') as file:
    text = file.read()
    num_characters = 0
    num_lines = 0

    for char in text:
        num_characters += 1
    
    for line in text.splitlines(): # splitlines -> Separate the text of a .txt file line by line.
        num_lines += 1

# num_characters = len(text)
# num_lines = text.count('\n') + 1

print(f"Number of characters: {num_characters}")
print(f"Number of lines: {num_lines}")