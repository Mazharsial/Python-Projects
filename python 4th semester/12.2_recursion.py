# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Recursive function to calculate sum of natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)

# Example usage
num = int(input("Enter a number: "))

print(f"Factorial of {num} is: {factorial(num)}")
print(f"Sum of natural numbers up to {num} is: {sum_natural(num)}")
