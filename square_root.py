# square root for positive numbers

num = float(input("Enter a positive number:"))

num_sqrt = num ** 0.5
print("The square root of %0.3f is %0.3f" %(num, num_sqrt))

# square root for real or complex numbers

import cmath

n = eval(input("Enter a real or complex number:"))

n_sqrt = cmath.sqrt(n)
print("The square root of {0} is {1:0.3f}+{2:0.3f}j".format(n, n_sqrt.real, n_sqrt.imag))