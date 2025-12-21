import os

while True:
    file_path = input("Enter the file path: ")


    with open(f"{file_path}.txt", 'r') as file:
        content = file.read()
        print("File Content:")
        print(content)

    choice = input("1)search a word or phrase\n2)exit\nEnter your choice: \n "\
                   "2) Count words and characters\n" \
                   "3) Count frequency of a word\n  " \
                   "4) Count frequency of a character\n" \
                   "0) Exit\n"
                   "Choose an option (0-4):")
    
    #SEARCH

    if choice == '1':
        os.system("cls")
        
