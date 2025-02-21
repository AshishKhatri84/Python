# Problem 1: Convert the given expression into its equivalent Python expression
# Example
y = 10   
a = 5    
b = 3   
c = 2 
d = 4   
x = 6   
z = 7   
num = ((10 * y * (a * b + c)) / d) - 0.8 + 2 * b
den = (x + a) * (1 / z)
Ƶ = num // den # // for integer value and / for decimal value
print("Ƶ:", Ƶ)


# Problem 2: Calculate GCD and LCM using Euclidean Algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
# Example
a = 48
b = 18
gcd_result = gcd(a, b)
lcm_result = lcm(a, b)
print("GCD of a and b is ",gcd_result)
print("LCM of a and b is ",lcm_result)

# Using subtraction method
def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
# Example usage
num1 = 48
num2 = 18
gcd_result = gcd(num1, num2)
lcm_result = lcm(num1, num2)
print(f"GCD of {num1} and {num2} is {gcd_result}")
print(f"LCM of {num1} and {num2} is {lcm_result}")


#Problem 3: Calculate the distance between two points (x1, y1) & (x2, y2)
def dist(x1, y1, x2, y2):
    a = (x2 - x1)**2 + (y2 - y1)**2
    b = a**0.5
    return b
# Example usage
x1, y1 = 0, 0
x2, y2 = 3, 4
b = dist(x1, y1, x2, y2)
print("Distance between (x1, y1) and (x2, y2) is: ",b)

# Pyramid of *
def print_pattern(n):
    # Upper part of the pattern
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
# Number of rows for the upper part
n = 5
print_pattern(n)

# Surface Area and Volume of Solid Cube
class Cube:
    def __init__(self, side):
        self.side = side
    
    def surface_area(self):
        # Surface area of a cube: 6 * (side^2)
        return 6 * (self.side ** 2)
    
    def volume(self):
        # Volume of a cube: side^3
        return self.side ** 3
    
    def display(self):
        print("Side Length: ",self.side)
        print("Surface Area: ",self.surface_area())
        print("Volume: ",self.volume())

# Example:
side = int(input("Side: "))
cube = Cube(side)
cube.display()

class Cylinder:
    def input(self):
        self.a=int(input("Enter radius: "))
        self.b=int(input("Enter height: "))
        self.area=2*3.14*(self.a**2)
        self.volume=2*3.14*self.a*self.b
    def display(self):
        print("Area: ",self.area)
        print("Volume: ",self.volume)
obj=Cylinder()
obj.input()
obj.display()

# Palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()

    length = len(s)
    
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

# Factorial using Recursive Function
def factorial(n): # Parameter
    if n==0:
        return 1
    return n*factorial(n-1)
num=int(input("n = "))
a=factorial(num) # Arguement
print(a)

# nth Fibonacci number using Recursive function (0th term=0,1st term=1)
a=int(input("Enter a = "))
def fib(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return fib(n-1) + fib(n-2)
print("The",a,"th fibonacci number is ",fib(a))

# Pangram string
import string
def is_pangram(s):
    # Convert to lowercase and create a set of the alphabet
    s = s.lower()
    alphabet = set(string.ascii_lowercase)
    
    # Create a set of characters in the string
    letters_in_string = set(c for c in s if c in alphabet)
    
    # Compare the two sets
    return letters_in_string == alphabet

# Test cases
test_string1 = "The quick brown fox jumps over the lazy dog"
test_string2 = "Hello world!"

print(f"Is the first string a pangram? {is_pangram(test_string1)}")
print(f"Is the second string a pangram? {is_pangram(test_string2)}")