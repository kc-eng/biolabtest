"""
A simple package to print program texts exactly as they are.
"""

PROGRAM1 = '''# Program 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
n = 5
print(f"The factorial of {n} is {factorial(n)}")'''

PROGRAM2 = '''# Program 2
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci(i), end=" ")'''

PROGRAM3 = '''# Program 3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test numbers from 1 to 20
for num in range(1, 21):
    if is_prime(num):
        print(f"{num} is prime")'''

PROGRAM4 = '''# Program 4 - Add your code here'''

PROGRAM5 = '''# Program 5 - Add your code here'''

PROGRAM6 = '''# Program 6 - Add your code here'''

PROGRAM7 = '''# Program 7 - Add your code here'''

PROGRAM8 = '''# Program 8 - Add your code here'''

PROGRAM9 = '''# Program 9 - Add your code here'''

PROGRAM10 = '''# Program 10 - Add your code here'''

def print_program1():
    """Print the exact text of Program 1."""
    print(PROGRAM1)

def print_program2():
    """Print the exact text of Program 2."""
    print(PROGRAM2)

def print_program3():
    """Print the exact text of Program 3."""
    print(PROGRAM3)

def print_program4():
    """Print the exact text of Program 4."""
    print(PROGRAM4)

def print_program5():
    """Print the exact text of Program 5."""
    print(PROGRAM5)

def print_program6():
    """Print the exact text of Program 6."""
    print(PROGRAM6)

def print_program7():
    """Print the exact text of Program 7."""
    print(PROGRAM7)

def print_program8():
    """Print the exact text of Program 8."""
    print(PROGRAM8)

def print_program9():
    """Print the exact text of Program 9."""
    print(PROGRAM9)

def print_program10():
    """Print the exact text of Program 10."""
    print(PROGRAM10) 