def factorial_iterative(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Example usage:
number = 5
print(f"Factorial of {number} (iterative): {factorial_iterative(number)}")
