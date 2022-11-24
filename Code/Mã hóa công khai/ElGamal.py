import TimNghichDao as _1
q = 6827
a = 5
xA = 307

yA = pow(a, xA) % q
print("<p>yA = a <sup>xA</sup> mod q = " + str(a) + "<sup>" + str(xA) + "</sup> mod " + str(q) + " =", yA, end = "</p>\n")
print("<p>PU = {q, a, yA} = {"+ str(q) + "," + str(a) + "," + str(yA) + "}", end = "</p>\n")

k = 919
M = 474

K = pow(yA, k) % q

C1 = pow(a, k) % q 
C2 = (M*K) % q

print("<p>K = (yA)<sup>k</sup> mod q = " + str(yA) + "<sup>" + str(k) + "</sup> mod " + str(q) + " =", K, end = "</p>\n")
print("<p>C<sub>1</sub> = a<sup>k</sup> mod q = " + str(a) + "<sup>" + str(k) + "</sup> mod " + str(q) + " =", C1, end = "</p>\n")
print("<p>C<sub>2</sub> = KM mod q = " + str(K) + "*" + str(M) + " mod " + str(q) + " =", C2, end = "</p>\n")



K = pow(C1, xA) % q


K_1 = _1.TimNghichDao(K, q)
M = ((C2 % q) * (K_1 % q)) % q
print("<p>K = (C<sub>1</sub>)<sup>xA</sup> mod q = " + str(C1) + "<sup>" + str(xA) + "</sup> mod " + str(q) + " =", K, end = "</p>\n")
print("<p>K<sup>-1</sup> = ", K_1, end = "</p>\n")
print("<p>M = (C<sub>2</sub>K<sup>-1</sup>) mod q = " + str(C2) + "*" + str(K_1) + " mod " + str(q) + " =", M, end = "</p>\n")


print("yA =", yA)
print("PU = {q, a, yA} = {"+ str(q) + "," + str(a) + "," + str(yA) + "}")
print("{C<sub>1</sub>, C<sub>2</sub>} = {" + str(C1) + "," + str(C2) + "}")
print("Tính K = (C<sub>1</sub>)<sup>xA</sup> mod q ")
print("Bản rõ M = (C<sub>2</sub>K<sup>-1</sup>) mod q ")
