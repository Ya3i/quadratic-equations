#Create by : Yasin Allahyari
#instagram : @i._.ya3in
#E-mail : Yasinallahyari@yahoo.com


import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
d = b**2 - 4*a*c

if d > 0:
    # Calculate the two roots
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("The roots are real and different.")
    print("x1 = ", x1)
    print("x2 = ", x2)
elif d == 0:
    # Calculate the only root
    x = (-b) / (2*a)
    print("The roots are real and equal.")
    print("x = ", x)
else:
    # Calculate the complex roots
    realPart = -b / (2*a)
    imagPart = math.sqrt(abs(d)) / (2*a)
    print("The roots are complex and conjugate.")
    print("x1 = ", realPart, "+", imagPart, "i")
    print("x2 = ", realPart, "-", imagPart, "i")
