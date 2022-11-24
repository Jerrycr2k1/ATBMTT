import TimNghichDao as _1
p = 43
q = 47
e = 67

n = p*q
print("n = p*q = " + str(p) + "*" +str(q)+" = ", n)

Phi_n = (p-1)*(q-1)
print(Phi_n)


d = _1.TimNghichDao(e, Phi_n)

def PU():
	print("PU = {e, n} = {"+ str(e) + "," + str(n) + "}")
def PR():
	print("PR = {d, n} = {"+ str(d) + "," + str(n) + "}")
def MaHoaM(M, i = 0, BaoMat = True):
	if BaoMat:
		C = pow(M, e) % n
	else:
		C = pow(M, d) % n
	if i != 0:
		if BaoMat:
		 	print("<p>C = M<sup>e</sup> mod n = " + str(M) + "<sup>" + str(e) + "</sup> mod " + str(n) + " = " + str(C), end = "</p>\n")
		else:
		 	print("<p>C = M<sup>d</sup> mod n = " + str(M) + "<sup>" + str(d) + "</sup> mod " + str(n) + " = " + str(C), end = "</p>\n")
	return C
def GiaiMaC(C, i = 0, BaoMat = True):
	if BaoMat:
		M = pow(C, d) % n
	else:
		M = pow(C, e) % n
	if i != 0:
		if BaoMat:
			print("<p>M = C<sup>d</sup> mod n = " + str(C) + "<sup>" + str(d) + "</sup> mod " + str(n) + " = " + str(M), end = "</p>\n")
		else:
			print("<p>M = C<sup>e</sup> mod n = " + str(C) + "<sup>" + str(e) + "</sup> mod " + str(n) + " = " + str(M), end = "</p>\n")
	return M
PU()
PR()
M = 59
BaoMat = True
MaHoaM(M, 1, BaoMat)
GiaiMaC(MaHoaM(M, 0, BaoMat), 1, BaoMat)
