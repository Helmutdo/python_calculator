def Menu():
    print("Welcome to the calculator!")
    print("Please choose an operation:")
    print()
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print()

def Add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Error: division by zero.")
        return "undefined"

def main():
    while True:
        Menu()
        choice = input("Choose an option: ")
        
        if choice == '5':
            print("Exiting the calculator.")
            break
        
        num1 = float(input("Input the first number: "))
        num2 = float(input("Input the second number: "))
        
        if choice == '1':
            result = Add(num1, num2)
        elif choice == '2':
            result = substract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        else:
            print("Invalid choice. Please try again.")
            continue
        
        print(f"\nYour result is: {result}\n")

if __name__ == "__main__":
    main()
# This code is a simple calculator that performs addition, subtraction, multiplication, and division.
# It uses functions to define each operation and a menu for user interaction.
        

