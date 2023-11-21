# Divide the given two numbers and print the quotient using / operator

num = int(input("Enter a number:"))
divisor = int(input("Enter the Divisor:"))

for i in range(num):
    quotient = divisor * i
    if(quotient >= num):
        if(quotient == num):
            print(i)
            break
        print(i-1)
        break