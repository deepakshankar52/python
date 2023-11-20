# Check whether the given number is Perfect Cube or not 

num = int(input("Enter a number:"))
flag = 0
for i in range(num):
    if(i*i*i == num):
        print("Perfect Cube")
        flag = 1
        break
if(flag == 0):
    print("Not a Perfect Cube")