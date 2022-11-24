# (loga)b(mod n) = x Logarit cơ số a của b theo modun lô n 

def TimX(n, a, b):
	check = a % n
	for i in range(1, n):
		# print(pow(a, i), pow(a, i) % n)
		if (pow(a, i) % n == check and i != 1) or pow(a, i) % n == 1:
			return 0
		if pow(a, i) % n == b:
			return i
	return 0
def main():
	a = 3
	b = 4
	n = 13
	# a^x mod n = b
	print("Không tồn tại" if TimX(n, a, b) == 0 else TimX(n, a, b))

main()