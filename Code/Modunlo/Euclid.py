# Tính nghịch đảo của b theo m
b = 851
m = 71
def Euclid(A, B):
    # print(A, B)
    if B[2] == 0:
        return "UCLN = " + str(A[2])+ "\nKhông có nghịch đảo"
    if B[2] == 1:
        return "UCLN = " + str(B[2]) + "\nNghịch đảo = " + str(B[1] % m if B[1] > 0 else (m + B[1]))
    Q = A[2] // B[2]
    T = [A[0] - Q * B[0], A[1] - Q * B[1], A[2] - Q * B[2]]
    A = B
    B = T
    return Euclid(A, B)
def EuclidWord(A, B):
    for i in A:
        print(",",str(i), end = "")
    for i in B:
        print(",",str(i), end = "")
    if B[2] == 0:
        return "\nUCLN = " + str(A[2])+ "\nKhông có nghịch đảo"
    if B[2] == 1:
        return "\nUCLN = " + str(B[2]) + "\nB3 = 1 => B2 = " + str(b) + " mod " + str(m) + " = " + str(B[1]) + " mod " + str(m) + " = " + str(B[1] % m if B[1] > 0 else (m + B[1]))
    Q = A[2] // B[2]
    print()
    print(Q, end = "")
    T = [A[0] - Q * B[0], A[1] - Q * B[1], A[2] - Q * B[2]]
    A = B
    B = T
    return EuclidWord(A, B)

A = [1, 0, m]
B = [0, 1, b]
def Word(m, b):
    A = [1, 0, m]
    B = [0, 1, b]
    print("Q, A1, A2, A3, B1, B2, B3")
    print("-", end = "")
    print(EuclidWord(A, B))
Word(m, b)