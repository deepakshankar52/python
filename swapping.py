# using a temporary variable

x = input("Enter value of x:")
y = input("Enter vaue of y:")

temp = x 
x = y
y = temp

print("The value of x after swapping: {}".format(x))
print("The value of y after swapping: {}".format(y))


# without using temporary variable

x = input("Enter value of x:")
y = input("Enter vaue of y:")

x, y = y, x 
print("Value of x: {}".format(x))
print("Value of y: {}".format(y))
