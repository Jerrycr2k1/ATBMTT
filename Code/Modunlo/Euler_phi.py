def gcd(a, b):
    if (b == 0):
        return a;
    return gcd(b, a % b)

def SNT(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False

def Tinh(a, n):
    return pow(a, n) - pow(a, n - 1)

def Euler(n):
    N = []
    U = {0}
    U.pop()
    t = 2
    while True:
        if n == 1:
            break
        if gcd(t, n) > 1:
            N.append(t)
            U.add(t)
            n = n / t
        else:
            t += 1
    res = 1
    for i in U:
        t = 0
        for j in N:
            if i == j:
                t += 1
        res *= Tinh(i, t)
    return res


def HTML():
    n = 3992
    print("ɸ(" + str(n) + ") = ", end = "")
    print("ɸ(" , end = "") 
    N = []
    U = {0}
    U.pop()
    t = 2
    while True:
        if n == 1:
            break
        if gcd(t, n) > 1:
            N.append(t)
            U.add(t)
            n = n / t
        else:
            t += 1
    # print(N)
    res = 1
    for i in U:
        t = 0
        for j in N:
            if i == j:
                t += 1
        res *= Tinh(i, t)
        print(i,"<sup>", t, "</sup>", end = " ")
    print(")")
# HTMsL()
# print(Euler(3992))
