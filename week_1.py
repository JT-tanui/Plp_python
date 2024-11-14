a = input("Enter the first number: ")
b = input("Enter the second number: ")

if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    sign = input("A. +\n"
                 "B. -\n"
                 "C. *\n"
                 "D. /\n"
                 "Your choice: ").lower()
    if sign == "a":
        result = a + b
        print("Sum is:", result)
    elif sign == "b":
        result = a - b
        print("Subtraction is:", result)
    elif sign == "c":
        result = a * b
        print("Multiplication is:", result)
    elif sign == "d":
        if b != 0:
            result = a / b
            print("Division is:", result)
        else:
            print("Error: Cannot divide by zero.")
else:
    print("Enter a valid whole number")
