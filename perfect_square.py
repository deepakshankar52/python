#check whethr given number is perfect square or not

num = int(input("Enter a number:"))
flag = 0
for i in range(num):
    if(i*i == num):
        print("Perfect Square")
        flag = 1
        break
if(flag == 0):
    print("Not a Perfect Square")
