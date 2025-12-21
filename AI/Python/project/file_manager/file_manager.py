import os

while True:
    file_path = input("Enter the file path: ")

    with open(f"{file_path}.txt", "r") as file:
        content = file.read()
        print("File Content:")
        print(content)

    choice = input(
        "1)search a word or phrase\n2)exit\nEnter your choice: \n "
        "2) Count words and characters\n"
        "3) Count frequency of a word\n  "
        "4) Count frequency of a character\n"
        "0) Exit\n"
        "Choose an option (0-4):"
    )

    # SEARCH

    if choice == "1":
        os.system("cls")

        query = input("Enter word or phrase to search: ")

        count = content.lower().count(query.lower())
        lines = content.split("\n")
        line_numbers = []

        i = 0

        while i < len(lines):
            if query.lower() in lines[i].lower():
                line_numbers.append(i + 1)
            i += 1

            print("occurrences:", count)
            print("line numbers:", line_numbers)

    # COUNT 
    elif choice == "2":
        os.system("cls")

        chars_with_spaces = len(content)
        chars_without_spaces = len(content.replace(" ", "").replace("\n", ""))
        normalized = content.lower()

        symbols = [".", ",", "!", "?", ";", ":", "-", "_", "(", ")", "[", "]", "{", "}", "\"", "'"]
        for symbol in symbols:
            normalized = normalized.replace(symbol, "")

        while "  " in normalized:
            normalized = normalized.replace("  ", " ")

        words = normalized.split(" ")
        words_count = len(words)

        print("words:", words_count)
        print("characters (with spaces):", chars_with_spaces)
        print("characters (without spaces):", chars_without_spaces)
    
    # FREQUENCY OF WORD
    elif choice == "3":
        os.system("cls")

        target = input("Enter a word :").lower()
        