# using recursion
def fib(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
n = int(input())
for i in range(1, n+1):
    fib(i)
print(fib(i))

# using for loop
num = int(input())
first = 0
second = 1
for i in range(1, num+1):
    if(i <= 1):
        next = i
    else:
        next = first + second
        first = second
        second = next

print(next)