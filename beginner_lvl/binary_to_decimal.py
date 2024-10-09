def binary_to_decimal(binary_number):
    decimal = 0
    for x, bit in enumerate(reversed(binary_number)):
        if bit == '1':
            decimal += 2 ** x
    return decimal


def decimal_to_binary(decimal_number):
    binary_nr = ""
    while decimal_number > 0:
        binary_nr = str(decimal_number % 2) + binary_nr
        decimal_number = decimal_number // 2
    return binary_nr


binary = input("Enter a binary number: ")
decimal_result = binary_to_decimal(binary)
print(decimal_result)

decimal_input = int(input("Enter a decimal number: "))
binary_result = decimal_to_binary(decimal_input)
print(binary_result)