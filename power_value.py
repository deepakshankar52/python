# pow function using looping  statement

base = int(input("Enter base value:"))
power = int(input("Enter power value:"))

res = 1

for i in range(power):
    res *= base

print(res)