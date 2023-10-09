# a = input('enter nr 1')
# b = input('enter nr 2')
# if a > b:
#     print(a+b)
# else:
#     print(a*b)
# a = 50
# b = int(input('enter nr:'))
# if b>=a:
#     print(b)
# else:
#     print(a)

# a = int(input('enter nr a: '))
# b = int(input('enter nr b: '))
# c = int(input('enter nr c: '))
# d = int(input('enter nr d: '))
# if a < b and b < c:
#     print(f"first condition met: {b}")
# elif a > c:
#     print(f" second condition met:{a}")
# else:
#     print(f"third condition met. First number:{a},second number:{b}, third number:{c}, fourth number:{d}")

# name = input("enter your name: ")
# last_name = input ("enter your last name: ")
# age = int(input("enter your age: "))
# if age >= 21:
#     print( f"you can enter casino:{age}")
# else: 
#     print("you cant enter casino")

# name = input("enter your nam: ")
# privileged_user = ["Andrius", "Tomas", "Povilas"]
# if name in privileged_user:
#     print("Sveiki atvykę ")
# else:
#     print("closed")

# a = "+"
# b = input("nter betka: ")

# if b == a:
#     print("betkas")

print("calculator: ")
a = int(input("enter your first number: "))
c = input("enter simbol: ")
b = int(input("enter your second number: "))

if c == "+":
    print(a+b)
if c == "-":
    print(a-b)
if c == "*":
    print(a*b)
if c == "/":
    print(a/b)

