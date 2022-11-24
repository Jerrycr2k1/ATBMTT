# a^ -1 mod b
def Euclid(A, B, a):
    if B[2] == 0:
        return -1
    if B[2] == 1:
        return B[1] if B[1] > 0 else (a + B[1])
    Q = A[2] // B[2]
    T = [A[0] - Q * B[0], A[1] - Q * B[1], A[2] - Q * B[2]]
    A = B
    B = T
    return Euclid(A, B, a)
def TimNghichDao(a, b):
    A = [1, 0, b]
    B = [0, 1, a]
    return Euclid(A, B, b)
    