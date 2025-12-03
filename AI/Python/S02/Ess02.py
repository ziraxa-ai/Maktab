# MC 
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "EVEN")
    else:
        print(i)


# if i % 2:
#range(n) -> 0
# int() -> age

# Ess 1 
n = int(input("Enter a number: "))

while n > 0:
    print(n)
    n -= 1

print("FINISHED!")

# Ess 2
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum is:", total)

# Ess 3

username = "taha"
password = "1234"

attempts = 3

while attempts > 0:
    user = input("Username: ")
    pwd = input("Password: ")

    if user == username and pwd == password:
        print("Login Successful!")
        break
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("Account Locked!")

#تمام کدهای این جلسه را در پوشه Week-1 در GitHub آپلود کنید.
# در README توضیح دهید هر کد چه کاری انجام می‌دهد.
# یک Screenshot از خروجی برنامه در Repo بگذارید.
# یک پست LinkedIn درباره اینکه "حل حلقه‌ها اولین قدم مهندسی AI است" منتشر کنید.
