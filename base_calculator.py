import math

class ScientificCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

    def square_root(self, a):
        return math.sqrt(a)

    def power(self, a, b):
        return math.pow(a, b)

    def factorial(self, n):
        if n < 0:
            return "Error: Factorial of negative number"
        elif n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def sin(self, a):
        return math.sin(math.radians(a))

    def cos(self, a):
        return math.cos(math.radians(a))

    def tan(self, a):
        return math.tan(math.radians(a))

def main():
    calculator = ScientificCalculator()
    while True:
        print("Scientific Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Power")
        print("7. Factorial")
        print("8. Sin")
        print("9. Cos")
        print("10. Tan")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '0':
            break

        if choice in ['1', '2', '3', '4', '6']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        elif choice in ['5', '7', '8', '9', '10']:
            a = float(input("Enter number: "))

        if choice == '1':
            print("Result:", calculator.add(a, b))
        elif choice == '2':
            print("Result:", calculator.subtract(a, b))
        elif choice == '3':
            print("Result:", calculator.multiply(a, b))
        elif choice == '4':
            print("Result:", calculator.divide(a, b))
        elif choice == '5':
            print("Result:", calculator.square_root(a))
        elif choice == '6':
            print("Result:", calculator.power(a, b))
        elif choice == '7':
            print("Result:", calculator.factorial(int(a)))
        elif choice == '8':
            print("Result:", calculator.sin(a))
        elif choice == '9':
            print("Result:", calculator.cos(a))
        elif choice == '10':
            print("Result:", calculator.tan(a))
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
