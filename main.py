import operations
def main():
    a = 10
    b = 5
    print(f"{a} + {b} = {operations.add(a, b)}")
    print(f"{a} - {b} = {operations.subtract(a, b)}")
    print(f"{a} * {b} = {operations.multiply(a, b)}")
if __name__ == "__main__":
    main()