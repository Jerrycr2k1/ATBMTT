import TimNghichDao as _1
import Euclid
p = 47
q = 23
h = 25
xA = 2
k = 3
HM = 9
# print("p =", p,"\nq =", q,"\nh =", h,"\nxA =", xA,"\nk =", k,"\nHM =", HM)

g = pow(h, ((p-1)//q)) % p
print("<p>g = h<sup>(p-1)/q</sup> mod p = " + str(h) + "<sup>(" + str(p) + "-1)/" + str(q) + "</sup> mod " + str(p) + " = " + str(h) + "<sup>" + str(((p-1)//q)) + "</sup> mod " + str(p) + " =", g, "</p>")
yA = pow(g, xA) % p
print("<p>yA = g<sup>xA</sup> mod p = " + str(g) + "<sup>" + str(xA) + "</sup> mod " + str(p) + " =", yA, "</p>")

r = (pow(g, k) % p) % q
print("r = (g<sup>k</sup> mod p) mod q = (" + str(g) + "<sup>" + str(k) + "</sup> mod " + str(p) + ") mod " + str(q) + " = " + str(pow(g, k) % p) + " mod " + str(q) + " =" , r)
s = (_1.TimNghichDao(k, q) * ((HM + xA * r) % q)) % q
print("s = (k<sup>-1</sup>(H(M) + xA*r)) mod q = (" + str(k) + "<sup>-1</sup>(" + str(HM) + " + " + str(xA) + "*" + str(r) + ")) mod " + str(q) )
Euclid.Word(q, k)
print(str(k) + "^-1 = ",_1.TimNghichDao(k, q))
print("s = (" + str(_1.TimNghichDao(k, q)) + "(" + str(HM) + " + " + str(xA * r) + ")) mod " + str(q) )
print("s = (" + str(_1.TimNghichDao(k, q)) + "*" + str(HM + xA * r) + ") mod " + str(q) )
print("s = (" + str(_1.TimNghichDao(k, q) * (HM + xA * r)) + ") mod " + str(q) )
print("Chữ ký số(r, s) = (" + str(r) + ", " + str(s) + ")")


# Xác thực
print("Kiểm tra chữ ký:\nw = s^-1(mod q)\nu1= (H(M).w)(mod q) \nu2= (r.w)(mod q) \nv = (g^u1.y^u2(mod p)) (mod q) ")

w = _1.TimNghichDao(s, q)
print("w =", w)
u1 = (HM * w) % q
print("u1 =", u1)
u2 = (r * w) % q
print("u2 =", u2)
v = ((pow(g, u1) * pow(yA, u2))% p) % q
print("x1 = g^u1 mod p =", pow(g, u1)%p)
print("x2 = yA^u2 mod p =", pow(yA, u2)%p)
print("v =", v)
print("v == r")
if v == r:
	print("Đúng")