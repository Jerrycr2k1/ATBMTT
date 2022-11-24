q = 6947
a = 5 # Căn nguyên thủy của q
xA = 395
xB = 338
yA = pow(a, xA) % q
yB = pow(a, xB) % q
K_A = pow(yA, xB) % q
K_B = pow(yB, xA) % q
K_AB = pow(a, xA * xB) % q

# print("q", q)
# print("a", a)
# print("xA", xA)
# print("xB", xB)
# print("yA", yA)
# print("K_A", K_A)
# print("yB", yB)
# print("K_B", K_B)
# print("K_AB", K_AB)

# print("<p>q =", q, ",a =", a, end = "</p>\n")
print("<p>xA = " + str(xA) + ", yA = a <sup>xA</sup> mod q = " + str(a) + "<sup>" + str(xA) + "</sup> mod " + str(q) + " = " , yA, end = "</p>\n")
print("<p>K = yA <sup>xB</sup> mod q = " + str(yA) + "<sup>" + str(xB) + "</sup> mod " + str(q) + " = " , K_A, end = "</p>\n")
print("<p>xB = " + str(xB) + ", yB = a <sup>xB</sup> mod q = " + str(a) + "<sup>" + str(xB) + "</sup> mod " + str(q) + " = " , yB, end = "</p>\n")
print("<p>K = yB <sup>xA</sup> mod q = " + str(yB) + "<sup>" + str(xA) + "</sup> mod " + str(q) + " = " , K_B, end = "</p>\n")