separator = "-"*100
print(separator,"\n")

number_first = float(input("input a number: "))
number_second = float(input("input another number: "))

operation = input("""Write the desired operation: """)
operation = operation.lower()

result = 0

if operation == "sum":
    result = number_first + number_second
elif operation == "minus":
    result = number_first - number_second
elif operation == "multiplication":
    result = number_first * number_second
elif operation == "division":
    try:
        result = number_first / number_second
    except ZeroDivisionError:
        print("Error: division by zero.")
        result = "indefined"

print("your result is:",result)