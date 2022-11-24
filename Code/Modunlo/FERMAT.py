import Euler_phi as Euler
a = 397
m = 6329
n = 6329
def FERMAT(a, m, n):
	if Euler.gcd(a, n) != 1:
		print("Không thể sử dụng do a, n không phải 2 số nguyên tố cùng nhau")
	else:
		print("ɸ(n) =",Euler.Euler(n))
		print(str(a) + "^" + str(Euler.Euler(n)) + " mod", n, "= 1")
		print(str(a) + "^" + str(m) + " mod", n, "= " + str(a) + ("^" + str(m%Euler.Euler(n)) if m%Euler.Euler(n) > 1 else "") + " mod", n, "")
FERMAT(a, m, n)