# Check whether the given number is a triangular number or not

num = int(input("Enter the number:"))

res = 1
flag = 0
i = 2
while(i<=num):
    res += i
    if(res == num):
        print("Triangular Number")
        flag = 1 
        break
    i += 1

if(flag == 0):
    print("Not a Triangular Number")