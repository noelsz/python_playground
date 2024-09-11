print("Select operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("\nEnter your choice: "))
number_A = float(input("First number: "))
number_B = float(input("Second number: "))

if choice == 1:
    print(f"{number_A} + {number_B} = {number_A + number_B}")
elif choice == 2:
    print(f"{number_A} - {number_B} = {number_A - number_B}")
elif choice == 3:
    print(f"{number_A} * {number_B} = {number_A * number_B}")
elif choice == 4:
    print(f"{number_A} / {number_B} = {number_A / number_B}") if number_B != 0 else print("Error, you were trying to divide with 0")
else:
    print("Invalid Input")

