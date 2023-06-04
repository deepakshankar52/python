# Python program to print all prime numbers in an interval

def prime(start,end):
    prime_list = []
    for i in range(start,end):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

start_limit = int(input("Enter the starting limit:"))
end_limit = int(input("Enter the ending limit:"))

prime_nos = prime(start_limit,end_limit)

if(len(prime_nos) == 0):
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are:", prime_nos)