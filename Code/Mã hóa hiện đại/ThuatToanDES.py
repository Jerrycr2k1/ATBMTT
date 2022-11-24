SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]
IIP = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]
PC_1 =  [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]
E =  [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]
S_box = [
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],
[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],
[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],
[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  
[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 
[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 
[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],]]
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]
PreXOR2 = [29, 25, 21, 17, 13, 9, 5, 1,
           30, 26, 22, 18, 14, 10, 6, 2,
           31, 27, 23, 19, 15, 11, 7, 3,
           32, 28, 24, 20, 16, 12, 8, 4]
def HexToBin(hex):
    return bin(int(hex, 16))[2:].zfill(4)
def StringHexToBin(string):
    res = "" 
    for i in string:
        res += HexToBin(i)
    return res
def ListBinToListHex(ListBin):
    Text = ""
    for i in range(len(ListBin) // 8):
        Text += hex(int(ListBin[i * 8: i * 8 +8], 2))[2:].zfill(2)
    if len(ListBin) % 8 != 0 :
        Text += hex(int(ListBin[len(ListBin) // 8 * 8:], 2))[2:].zfill(2)
    return Text.upper()
def XOR(a, b):
    return "0" if a == b else "1"
def HoanVi(input, Maxtrix):
    res = ""
    for i in Maxtrix:
        res += input[i - 1]
    return res
def HoanVi_IP(input):
    return HoanVi(input, IP)
def HoanViIIP(input):
    return HoanVi(input, IIP)
def HoanViPC_1(key):
    return HoanVi(key, PC_1)
def HoanViPC_2(key):
    return HoanVi(key, PC_2)
def HoanViP(input):
    return HoanVi(input, P)
def ER(input):
    return HoanVi(input, E)
def ShiftLeft(C, si):
    return C[si:] + C[:si]
def subkey(input, key):
    res = ""
    for i in range(len(input)):
        res += XOR(input[i], key[i])
    return res
def HoanViPC1(K):
        return ListBinToListHex(HoanViPC_1(StringHexToBin(K)))
def HoanViIP(M):
        return HoanVi_IP(StringHexToBin(M))
def OutputSbox(input, i):
    hang = input[0] + input[5]
    cot = input[1:5]
    hang = int(hang, 2)
    cot = int(cot, 2)
    return bin(S_box[i][hang][cot])[2:].zfill(4)
def SinhKhoa(K):
        K = StringHexToBin(K)
        # Chia làm 2 nửa
        C = [[] for i in range(17)]
        D = [[] for i in range(17)]
        C[0] = K[:len(K)//2]
        D[0] = K[len(K)//2:]
        # print("C[0]: ", C[0])
        # print("D[0]: ", D[0])
        # print("C[0]: ", ListBinToListHex(C[0]))
        # print("D[0]: ", ListBinToListHex(D[0]))

        # Tạo khóa ShiftLeft
        for i in range(1, 17):
                C[i] = ShiftLeft(C[i - 1], SHIFT[i - 1])
                D[i] = ShiftLeft(D[i - 1], SHIFT[i - 1])
        #         print("C[", i, "]: ", C[i])
        #         print("D[", i,"]: ", D[i])
        #         print("C[", i, "]: ", ListBinToListHex(C[i]))
        #         print("D[", i,"]: ", ListBinToListHex(D[i]))
        # Tạo khóa con
        Key = [HoanViPC_2(C[i] + D[i]) for i in range(17)]
        for i in range(len(Key)):
            # print("K" +str(i)+" :", Key[i])
            # print("K" +str(i)+" :", ListBinToListHex(Key[i]))
            pass
        return Key
def F(M, Keyi, i):
        M = ListBinToListHex(M)
        # Tách 
        L = M[:len(M) // 2]
        R = M[len(M) // 2:]
        RCopy = R
        # print("L =", L)
        # print("R =", R)
        # Mở rộng nửa phải
        R = ER(StringHexToBin(R))
        # print("ER"+str(i)+" :",R)
        # print("ER"+str(i)+" :",ListBinToListHex(R))
        # Xor Khóa
        A = subkey(R, Keyi)
        # print("A: ",A)
        # print("A: ",ListBinToListHex(A))
        # Thế S-box 
        # Thế
        Hang = ["" for i in range(8)]
        B = ""
        for t in range(8):
                Hang[t] = A[t * 6 : t * 6 + 6]
                B += OutputSbox(Hang[t], t)
        # print("B:", B)
        # print("B:", ListBinToListHex(B))
        # Hoán vị P
        P = HoanViP(B)
        # print("F :", P)
        # print("F :", ListBinToListHex(P))
        R = subkey(StringHexToBin(L), P)
        R = ListBinToListHex(R)
        # print("L"+str(i)+" =", RCopy)
        # print("R"+str(i)+" =", R)
        return RCopy, R
def F_1(C, Keyi):
        C = ListBinToListHex(C)
        # Tách 
        L = C[:len(C) // 2]
        R = C[len(C) // 2:]
        RCopy = R
        # print("L =", L)
        # print("R =", R)
        # Mở rộng nửa phải
        R = ER(StringHexToBin(R))
        # print("R mở rộng:",ListBinToListHex(R))
        # Xor Khóa
        A = subkey(R, Keyi)
        # print("XOR với khóa: ",ListBinToListHex(A))
        # Thế S-box 
        # Thế
        Hang = ["" for i in range(8)]
        B = ""
        for t in range(8):
                Hang[t] = A[t * 6 : t * 6 + 6]
                B += OutputSbox(Hang[t], t)
        # print("OutputSbox:", ListBinToListHex(B))
        # Hoán vị P
        P = HoanViP(B)
        R = subkey(StringHexToBin(L), P)
        R = ListBinToListHex(R)
        # print("L sau =", RCopy)
        # print("R sau =", R)
        return RCopy, R
