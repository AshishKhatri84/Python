def hexadecimal_to_octal(hex_str):
    decimal = int(hex_str, 16)  # Convert hexadecimal to decimal
    octal = oct(decimal)  # Convert decimal to octal
    return octal[2:]  # Remove the '0o' prefix

hex_str = '64'
print("Hexadecimal to Octal:", hexadecimal_to_octal(hex_str))  # Output: 144

def octal_to_hexadecimal(octal_str):
    decimal = int(octal_str, 8)  # Convert octal to decimal
    hexadecimal = hex(decimal)  # Convert decimal to hexadecimal
    return hexadecimal[2:]  # Remove the '0x' prefix

octal_str = '144'
print("Octal to Hexadecimal:", octal_to_hexadecimal(octal_str))  # Output: 64

def hexadecimal_to_binary(hex_str):
    decimal = int(hex_str, 16)  # Convert hexadecimal to decimal
    binary = bin(decimal)  # Convert decimal to binary
    return binary[2:]  # Remove the '0b' prefix

hex_str = '64'
print("Hexadecimal to Binary:", hexadecimal_to_binary(hex_str))  # Output: 1100100

def octal_to_binary(octal_str):
    decimal = int(octal_str, 8)  # Convert octal to decimal
    binary = bin(decimal)  # Convert decimal to binary
    return binary[2:]  # Remove the '0b' prefix

octal_str = '144'
print("Octal to Binary:", octal_to_binary(octal_str))  # Output: 1100100

def binary_to_hexadecimal(binary_str):
    decimal = int(binary_str, 2)  # Convert binary to decimal
    hexadecimal = hex(decimal)  # Convert decimal to hexadecimal
    return hexadecimal[2:]  # Remove the '0x' prefix

binary_str = '1100100'
print("Binary to Hexadecimal:", binary_to_hexadecimal(binary_str))  # Output: 64

def binary_to_octal(binary_str):
    decimal = int(binary_str, 2)  # Convert binary to decimal
    octal = oct(decimal)  # Convert decimal to octal
    return octal[2:]  # Remove the '0o' prefix
