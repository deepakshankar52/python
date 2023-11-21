# Multiply the given two numbers without using * operator

num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))
res = 0

for i in range(num1):
    res += num2

print("Multiplication of ",num1,"X",num2," = ",res)