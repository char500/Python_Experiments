import math
print("Please, insert the factors of the following second degree equation in order to calculate its solutions: ax^2 + bx + c = 0 ")
a = ''
while type(a) != int:
    try:
        a = int(input("Input a: "))
    except ValueError:
        pass
if a == 0:
    b = ''
    while type(b) != int:
        try:
            b = int(input("Input b: "))
        except ValueError:
            pass
    if b ==0:
        c = ''
        while type(c) != int:
            try:
                c = int(input("Input c: "))
            except ValueError:
                pass
        if c == 0:
             print("0 = 0 Which is true!")
        else:
             print(str(c) + " = 0 Which is impossible!")
    else:
        res = -c / b
        print("solving for x...")
        print("x = " + str(res))
else:
    b = ''
    while type(b) != int:
        try:
            b = int(input("Input b: "))
        except ValueError:
            pass
    c = ''
    while type(c) != int:
        try:
            c = int(input("Input c: "))
        except ValueError:
            pass
    D = b*b - 4*a*c
    if D >= 0:
       sD = math.sqrt(D)
       res1 = (-b + sD) / (2 * a)
       res2 = (-b - sD) / (2 * a)
       print("solving for x...")
       print("x1 = " + str(res1) + " and " + "x2 = " + str(res2))
    else:
       print("There are no real solutions")