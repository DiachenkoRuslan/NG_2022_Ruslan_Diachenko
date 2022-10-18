# Quadratic equation - ax^2 + bx + c = 0
# QuadraticEquation = a*(x**2) + b*x + c

# Graphic
print("================================")

# Input elements a,b,c
a = int(input("Enter element [a]: "))
b = int(input("Enter element [b]: "))
c = int(input("Enter element [c]: "))

# Graphic
print("================================")


discriminant = b**2 - 4*a*c                                     # find D (discriminant). D = b^2 + 4ac.

if discriminant > 0:                                            # if D > 0,
    x1 = (-b + ( discriminant**(1/2) ) ) / (2*a)                # find x1 = (-b + root(D)) / 2*a
    x2 = (-b - ( discriminant**(1/2) ) ) / (2*a)                # find x2 = (-b - root(D)) / 2*a

    print("x1 = " + str(x1) + " | " + "x2 = " + str(x2))

    # Check result x1
    #print("Check: " + str(int(a*(x1**2) + b*x1 + c)) + " = 0")  # use int() this because value(if elem have big values) go to 0...  
    # Check result x2  
    #print("Check: " + str(int(a*(x2**2) + b*x2 + c)) + " = 0")  # use int() this because value(if elem have big values) go to 0...
elif discriminant == 0:                                         # if D = 0,
    x = -b/(2*a)                                                # x(single root) = -b / (2*a)
    print("x = " + str(x))
    print(a*(x**2) + b*x + c)

    # Check result x
    #print("Check: " + str(int(a*(x**2) + b*x + c)) + " = 0")  # use int() this because value(if elem have big values) go to 0...
    
else:                                                           # if D < 0 or other, no roots...
    print("No roots!")
