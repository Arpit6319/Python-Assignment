def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: Modulo by zero"

# Main calculator loop
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulus")
    print("0. Exit")

    choice = input("Enter choice (0-6): ")

    if choice == '0':
        print("Exiting calculator...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", exponentiate(num1, num2))
    elif choice == '6':
        print("Result:", modulus(num1, num2))
    else:
        print("Invalid choice. Please enter a valid option.")