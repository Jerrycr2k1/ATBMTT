import Euler_phi as Euler
n = 5
a = 463

def KiemTra(n, a):
    if Euler.gcd(n, a) != 1:
        return False 
    for i in range(1, n):
        if pow(a, i) % n == 1:
            if i == Euler.Euler(n):
                return True
            else:
                return False

# print(KiemTra(n, a))