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