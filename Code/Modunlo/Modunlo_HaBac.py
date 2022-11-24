a = 14
m = 19
n = 47
# a^m mod n
def x(a, m, n):
	print("b =", str(a) + "<sup>" + str(m) + "</sup> mod " + str(n) + " =", pow(a, m) % n)
	while(m > 1):
		m = dongHTML(a, m, n)
	print(str(a) + " mod " + str(n) + " =", a % n)
def X(a, m, n):
	print("b =", str(a) + "<sup>" + str(m) + "</sup> mod " + str(n) + " =", pow(a, m) % n)
	while(m > 1):
		m = dong(a, m, n)
	print(str(a) + " mod " + str(n) + " =", a % n)
def dong(a, m, n):
	print(str(a) + "^" + zfill(m) + " mod " + str(n) + " =", end = " ")
	if m % 2 == 0:
		print(" (" + str(a) + "^" + zfill(m // 2) + " mod " + str(n) + ")^2        mod " + str(n), end = "")
	else:
		print("[(" + str(a) + "^" + zfill(m // 2) + " mod " + str(n) + ")^2 * " + str(a)+ "] mod " + str(n), end = "")
	print(" =" ,pow(a, m) % n)
	return m // 2	
def dongHTML(a, m, n):
	print("<p>" + str(a) + "<sup>" + str(m) + "</sup> mod " + str(n) + " =", end = " ")
	if m // 2 == 1:
		if m % 2 == 0:
			print(" (" + str(a) + " mod " + str(n) + ")<sup>2</sup> mod " + str(n), end = "")
			# print(str(a % n) + "<sup>2</sup> mod " + str(n), end = " = ")
			# print(str(pow(a % n, 2)) + " mod " + str(n), end = "")
		else:
			print("[(" + str(a) + " mod " + str(n) + ")<sup>2</sup> * " + str(a)+ "] mod " + str(n), end = "")
	else:		
		if m % 2 == 0:
			print(" (" + str(a) + "<sup>" + str(m // 2) + "</sup> mod " + str(n) + ")<sup>2</sup> mod " + str(n), end = "")
			# print(str(pow(a, m //2)) + "<sup>2</sup> mod " + str(n), end = " = ")
			# print(str(pow((pow(a, m //2)), 2)) + " mod " + str(n), end = "")
		else:
			print("[(" + str(a) + "<sup>" + str(m // 2) + "</sup> mod " + str(n) + ")<sup>2</sup> * " + str(a)+ "] mod " + str(n), end = "")
	print(" =" ,pow(a, m) % n, "</p>")
	return m // 2
def zfill(i, m = 1000):
	res = str(i)
	while len(str(m)) - len(res) > 0:
		res += " "
	return res
a = 227
m = 80
n = 71
# print(pow(5, 387) % 7523)
x(a, m, n)