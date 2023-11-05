# ax**2 + bx + c == 0, where a, b and c are real numbers and a != 0

# solving quadratic eqn ==> (-b +- (b ** 2 - 4 * a *c) ** 0.5) / (2 * a)

# quadratic eqn ==> ax**2 + bx + c = 0

import cmath

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The solution are {0} and {1}".format(sol1,sol2))
