print("1. Number Classifier")
print("2. Grade Calculator")
print("3. Login Check")
print("4. Largest of Three Numbers")

choice = int(input("Enter choice (1-4): "))

if choice == 1:
    num = int(input("Enter a number: "))

    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif choice == 2:
    score = int(input("Enter score: "))

    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

elif choice == 3:
    stored_password = "python123"
    password = input("Enter password: ")

    if password == stored_password:
        print("Login Successful")
    else:
        print("Incorrect Password")

elif choice == 4:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    if a >= b and a >= c:
        print("Largest:", a)
    elif b >= a and b >= c:
        print("Largest:", b)
    else:
        print("Largest:", c)

else:
    print("Invalid Choice")