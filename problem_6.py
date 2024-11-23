#finding the greatest common divisor (GCD) of two numbers
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
a, b = num1, num2
while b != 0:
    remainder = a % b
    a = b
    b = remainder
print(f"GCD of {num1} and {num2} numbers is: {a}")