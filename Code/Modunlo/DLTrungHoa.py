import TimNghichDao as _1
import Euler_phi
_a = 227
_m = 80
n = 60421
Uc_n = []
def PTTSNT(n):
	for i in range(2, n):
		if n % i == 0 and Euler_phi.SNT(i):
			Uc_n.append(i)
			n = n //i
	return Uc_n
def main():
	m = PTTSNT(n)
	print("m", m)
	_M = 1
	for i in m:
		_M *= i
	M = [_M//i for i in m]
	print("M", M)
	c = [i*_1.TimNghichDao(i, n //i) for i in M]
	print("c", c)
	a = [pow(_a, _m) % i for i in m]
	print("a", a)
	A = 0
	for i in range(len(m)):
		A += a[i]*c[i]
	print("A", A)
	print("x = ",A % n)
main()