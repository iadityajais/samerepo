# Simple Python program
import multicloud
import time

def greet(name):
    return f"Hello, {name}! Welcome to Python 🐍"

def add_numbers(a, b):
    return a + b

# Main execution
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Sum is:", add_numbers(x, y))

