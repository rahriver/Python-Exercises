import math

a = int(input("First Integer: "))
b = int(input("Second Integer: "))

summation = a + b
minus = b - a
product = a * b
quotient = a / b
remainder = a % b
logarithm = math.log(a, 10)
power = a ** b

print(f"Sum: {summation}")
print(f"Difference: {minus}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")
print(f"Logarithm: {logarithm}")
print(f"{a} to the power of {b}: {power}")



