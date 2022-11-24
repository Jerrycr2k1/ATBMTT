a = 3
m = 127
n = 11
# a^m mod n
def mod(a, m, n):
	if m == 2:
		return (a*a) % n
	if m == 1:
		return a % n
	if m%2 == 0:
		return pow(mod(a, m//2, n), 2) % n
	if m%2 == 1:
		return (pow(mod(a, m//2, n), 2) * a) % n
	
print(mod(a, m, n))