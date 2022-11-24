import TimNghichDao as _1
m = [17, 19, 11]
a = [5, 16, 3]
for i in range(len(m)):
    a[i] = a[i] % m[i]
M = 1
for i in m:
    M *= i
M_1 = []
c = [0 for i in a]

def TimM_1():
    for i in m:  
        print(M // i, i)
        M_1.append(_1.TimNghichDao(M // i, i))

def main():
    TimM_1()
    print(M_1)
    A = 0
    for i in range(len(m)):
        c[i] = M_1[i] * (M // m[i])
        A += a[i] * c[i]
    x = A % M
    print(c)
    print(x)

main()
