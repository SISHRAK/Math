import math


def f(x):
    return 1 / 4 * x ** 4 + x ** 2 - 8 * x + 12


def f2(x):
    return x ** 3 + 2 * x - 8


def f3(x):
    return 3 * x ** 2 + 2
def f4(x):
    return 6 * x


def find_initial_guess(a, b):
    if f2(a) * f4(a) > 0:
        return a
    if f2(b) * f4(b) > 0:
        return b
    return None

def newton(a, b, e):
    x0 = find_initial_guess(a, b)
    #print(x0)
    if x0 is None:
        return None
    i = 0
    flag = True
    while flag:
        i += 1
        x1 = x0 - f2(x0) / f3(x0)
       # print(x1)
        #print("-------")
        if abs(f2(x1)) < e:
            x0 = x1
            break
        x0 = x1
        #print(x0)
    return x0, f(x0)


def chords(a, b, e):
    i = 0
    while True:
        i += 1
        x_0 = a - (a - b) * f2(a) / (f2(a) - f2(b))
        if math.fabs(f2(x_0)) <= e:
            return x_0, f(x_0), i
        else:
           # print(f2(x_0))
            if f2(x_0) > 0:
                b = x_0
            else:
                a = x_0
       # print(a,b)

def golden_section_search(a, b, tol):
    phi = (1 + 5 ** 0.5) / 2
    c = b - (b - a) / phi
    d = a + (b - a) / phi
   # print(c,d)

    while abs(c - d) > tol:
       # print(c, d)
       # print("-------")
        #print(f(c), f(d))
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / phi
        d = a + (b - a) / phi


    return (b + a) / 2


def dihotomia(a, b, eps):
    x1 = (a + b - eps) / 2.0
    x2 = (a + b + eps) / 2.0
   # print(x1,x2)
    y1 = f(x1)
    y2 = f(x2)
   # print(y1,y2)
    if y1 > y2:
        a = x1
    else:
        b = x2
    if b - a > 2 * eps:

        dihotomia(a, b, eps)
    else:
        xm = (a + b) / 2.0
        ym = f(xm)
        print(xm)
        print(ym)


a = 0
b = 2
eps = 0.05
#print(f(1.756))
#print(f(1.706))

dihotomia(a, b, eps)
print(golden_section_search(a, b, eps))
print(f(golden_section_search(a, b, eps)))
# print(f(0.764))
# print(f(1.236))
print(chords(a, b, eps))
print(newton(a, b, eps))
# print(1 / 3)
# print(f2(4 / 3))
