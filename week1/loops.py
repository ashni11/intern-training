def mainloops():
    
    print("1. Multiplication Table")
    print("2. Sum 1-100")
    print("3. FizzBuzz")
    print("4. Number Guessing Game")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        num = int(input("Enter a number: "))

        for i in range(1, 11):
            print(num,"x",i,"=",num*i)

    elif choice == 2:
        total = 0

        for i in range(1, 101):
            total += i

        print("Sum =", total)

    elif choice == 3:
        for i in range(1, 51):

            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")

            elif i % 3 == 0:
                print("Fizz")

            elif i % 5 == 0:
                print("Buzz")

            else:
                print(i)

    elif choice == 4:
        target = 25

        guess = int(input("Guess the number: "))
    # 5 25
        while guess != target:

            if guess < target:
                print("Higher!")

            else:
                print("Lower!")

            guess = int(input("Try again: "))

        print("Congratulations! You guessed correctly.")

    else:
        print("Invalid choice")