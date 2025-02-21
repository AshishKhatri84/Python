# Return Function
def add(a,b):
    sum=0
    for i in range(a,b+1):
        sum+=i
    return sum; 
x=int(input("a = "))
y=int(input("b = "))
print("sum = ",add(x,y))

# Keyword Arguement
def display(name,age):
    print("Name is ",name,"\n","Age is ",age)
display("Ash",20)
display(21,"Red")
display(age=25,name="Blur")

# Default Arguement
def values(a,b=58,c=37):
    print("a= ",a,", b= ",b,", c= ",c)
values(34)
values(23,b=38)
values(c=25,a=45,b=65)

# Local & Global Variable
def demo():
    S="Fuck You" # Local Variable
    print(S)
S="Fuck You" # Global Variable
demo()
print(S)# If S is not defined again outside demo it gives Error

#__________________________________________________________________________________________
#______________________________Lecture 2___________________________________________________

# Class and Objects
class abc:
    print("gadd")
# Create an object of the class     
d1=abc() # In C++ [abc d1]                            
print(d1)                              

class rectangle:
    length=38
    breadth=34
R1=rectangle()
R1.length=15
R1.breadth=25
print(R1.length+R1.breadth)

class demo:
    def display(self): # self is mandatory
        print("go away")
obj=demo()
obj.display()

class circle:
    def display(self,radius):
        print("Radius: ",radius)
        return 3.14*(radius**2)
obj=circle()
print("Area: ",obj.display(5)) # 5 is an attribute

#__________________________________________________________________________________________
#______________________________Lecture 3___________________________________________________

# ACCESS SPECIFIER IN PYTHON: There are no keywords like public private or protected in python, All attributes and methods are public by default.
class person:
    Name="Bill"
    AccNo=24324
    def display(self):
        print("Name: ",self.Name)
        print("Account No.: ",self.AccNo)
p=person()
print("Name: ",p.Name)
print("Account No.: ",p.AccNo) 
p.display() # print output twice

class vit:
    def bhopal(self):
        self.Name="Bill"
        self.Salary=1000000
p=vit()
p.bhopal()
print("Name: ",p.Name)
print("Salary: ",p.Salary)

#__________________________________________________________________________________________
#______________________________Lecture 4___________________________________________________

# String
s1='Hello'
s1[2]='z' # Index of String -> s2[0],s2[1],s2[2],...s2[4]
print(s1)
# ERROR: 'str' object does not support item assignment
s2='z'+s1[2]
print(s2)

# String Operations
# SLicing
s="IIT-BOMBAY"
print(s[4:9]) 
print(s[0:len(s):2]) # SLicing with step size
# Length, Max, Min, Reverse Order
print(len(s))
print(max(s))
print(min(s))
print(s[::])
print(s[::-1])
# Contcatenation
s1='Ashish '
s2='Khatri'
s3=s1+s2 
print(s3)
# Repeatation
s4="Kolkata "
s5=3*s4 
print(s5)
# Comparison
s6="abcd"
s7="ABCD"
print(s6>s7) 
print(s6==s7)

#__________________________________________________________________________________________
#______________________________Lecture 5___________________________________________________

# Polymorphism
print(5+5)           # 10
print('5'+'5')       # 55
print(len('VIT'))    # 3
print(len(['kolkata','Bhopal']))    # 2

# Method Overloading
class xyz:
    def add(self,a,b,c=0):
        p=a+b+c
        print(p)
obj=xyz()
obj.add(5,2)
obj.add(3,4,5)

class xyz:
    def product(self,*args):
        p = 1
        for i in args:
            p *= i
        print(p)
obj=xyz()
obj.product(5,2,5)
obj.product(1,2,3,4,5,6,7)

# Method Overriding
class xyz():
    def display(self):
        print("Parent Class method")
class pqr(xyz):
    def display(self):
        print("Child Class method")
        super().display()
obj=pqr()
obj.display()

#__________________________________________________________________________________________
#______________________________Lecture 6___________________________________________________

# Inheritance
class father():
    def lands(self):
        print("Having 50 acres land")
class son(father):
    def Money(self):
        print("Having 10 lakh money")
s=son()
s.lands()
s.Money()
f=father()
# f.money() will give error

# Simple Inheritance
class Kolkata():
    a=int(input("Enter a: ")) 
    b=int(input("Enter b: "))
    def add(self):
        print("Addition is: ",self.a+self.b)
    def sub(self):
        print("Subtraction is: ",self.a-self.b)
class Delhi(Kolkata):
    def mul(self):
        print("Multiplication is: ",self.a*self.b)
    def div(self):
        print("Division is: ",self.a/self.b)
obj=Delhi()
print(obj.a)
obj.add()
obj.sub()
obj.mul()
obj.div()

# Multiple Inheritance
class Kolkata():
    back="Oracle DB & Java"
    def Backend(self):
        print("Backend task implemented using: ",self.back)
class Delhi():
    front="HTML CSS Javascript"
    def Frontend(self):
        print("Frontend task implemented using: ",self.front)
class Leader(Kolkata,Delhi):
    def show(self):
        print("Website created")
obj=Leader()
obj.Backend()
obj.Frontend()
obj.show()

# Multi-Level Inheritance 
class grandparent:
    surname="Khatri"
class parent(grandparent):
    def show(self):
        print("Karmbir",self.surname)
class grandson(parent):
    def display(self):
        print("Ashish",self.surname)
p=parent()
g=grandson()
p.show()
g.show()
g.display()

# Hierarchical Inheritance
class father:
    surname="Khatri"
    def show(self):
        print("Surname is ",self.surname)
class son(father):
    def display(self):
        print("My name is Ashish ",self.surname)
class daughter(father):
    def display(self):
        print("My name is Pooja ",self.surname)
s=son()
d=daughter()
s.display()
d.display()
s.show()
d.show()

# Hybrid Inheritance
class grandparent:
    surname="Khatri"
class Dad(grandparent):
    def show(self):
        print("Karmbir",self.surname)
class Mom(grandparent):
    def show(self):
        print("Anil",self.surname)
class son(Mom,Dad):
    def display(self):
        print("Ashish",self.surname)
p=Dad()
m=Mom()
g=son()
p.show()
m.show()
g.show()
g.display()

#__________________________________________________________________________________________
#______________________________Lecture 7___________________________________________________

# Diamond Problem 
class A:
    def display(self):
        print("display from Class A")
class B(A):
    def display(self):
        print("display from Class B")
class C(A):
    def display(self):
        print("display from Class C")
class D(B,C):
    def display(self):
        print("display from Class D")
d=D()
d.display()
print(D.mro())

# MRO
class C:
    def show(self):
        print("Class C method")
class A(C):
    pass
class B(A):
    def show(self):
        print("Class B method")
class D(B,C):
    pass
p=D()
p.show()

class Kolkata:
    pass
class Delhi(Kolkata):
    def display(self):
        print("Class Delhi method")
class kgp(Kolkata):
    def display(self):
        print("Class kgp method")
class bombay(Kolkata):
    pass
class madras(bombay):
    pass
p=madras()
p.display()   # Error
print(p.mro)

#__________________________________________________________________________________________
#______________________________Lecture 8___________________________________________________

# Exception Handling
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=a/b
print(c)
print("Hello")
'''If we run this code with b=0, then "ZeroDivisionError" will be shown.
Thus exception occurs at run-time. It can be solved in the following way:'''
a=int(input("Enter a: "))
b=int(input("Enter b: "))
try:
    c=a/b
    print("Result is ",c)
except:
    print("Division by 0 not allowed.")
else:
    print("No Exception Found")

# File Handling
# Write to a file
with open('example.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is an example of file handling in Python.\n")
    file.write("Each line of text will be written to the file.\n")
# Read from the file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Content of the file:")
    print(content)
# Append data to the file
with open('example.txt', 'a') as file:
    file.write("Appending this line to the file.\n")
# Read from the file line by line
with open('example.txt', 'r') as file:
    print("Reading the file line by line:")
    for line in file:
        print(line, end='')

# Open existing file for reading
with open('numbers.txt', 'r') as file:
# Read all lines from the file
   lines = file.readlines()
# Convert each line to an integer
numbers = [int(line.strip()) for line in lines]
# Print the list of numbers
print(numbers)


def read_and_write_files(file1_path, file2_path, output_file_path):
    try:
        # Read the first file
        with open(file1_path, 'r') as file1:
            content1 = file1.read()
        # Read the second file
        with open(file2_path, 'r') as file2:
            content2 = file2.read()
        # Write contents to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(content1)
            output_file.write(content2)

        print("Files have been read and written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
# Example usage
file1_path = 'file1.txt'
file2_path = 'file2.txt'
output_file_path = 'output.txt'
read_and_write_files(file1_path, file2_path, output_file_path)