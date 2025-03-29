"""siguiente modelo de calculadora"""

# separador
separator = "-"*100
print(separator,"\n")

# welcome banner
print("Welcome to you console multiplication table calculator")

# variable def
try:
    number_first = int(input("input a number: "))
    number_second = int(input("input another number: "))
except ValueError:
    print("must input a valid number !")

# logic 
for num_1 in range(number_first+1):
    print("for number",num_1)
    for num_2 in range(number_second+1):
        print(f"{num_1} x {num_2} = ", num_1 * num_2 )

print("\nThanks por playing \n")