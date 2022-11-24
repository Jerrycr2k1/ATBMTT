import ThuatToanAES
K = "6704C20E086B3F537AE5721F486DC559"
M = "4AEB5D62EC3B55DBF5D5A87708E2FF1E"
def g(W3, j):
	rw = ThuatToanAES.RotWord(W3)
	# print(rw)
	sw = ThuatToanAES.Sub(rw)
	# print(sw)
	xcsw = ThuatToanAES.XOR_Rcon(sw, j)
	# print(xcsw)
	return xcsw
def TaoW(K):
	# Khai báo
	W = [""for i in range(44)] # Mảng Hex
	# Tạo W0->W3:
	for i in range(4):
		W[i] = K[i*len(K)//4:(i+1)*len(K)//4]
	# vòng lặp
	for i in range(4, 44):
		if i % 4 == 0:
			W[i] = ThuatToanAES.XOR_Hex(W[i - 4], g(W[i - 1], i//4))
		else:
			W[i] = ThuatToanAES.XOR_Hex(W[i - 4], W[i - 1])
	return W
def TaoKey(W):
	Key = [[[""for i in range(4)]for j in range(4)] for t in range(11)]
	for i in range(11):
		T = W[i*4]+W[i*4+1]+W[i*4+2]+W[i*4+3]
		Key[i] =ThuatToanAES.StringToMatrixLat(T)
	return Key
def TaoInput(M):
	return ThuatToanAES.StringToMatrixLat(M)
def Round(Input, i, Key):
	if i > 0:
		# SubBytes
		Input = ThuatToanAES.SubBytesMatrix(Input)
		# ShiftRows
		Input = ThuatToanAES.ShiftRows(Input)
		if i < 10:
			# MixColumns
			Input = ThuatToanAES.MixColumns(Input)
	# AddRoundKey Ki
	Input = ThuatToanAES.AddRoundKey(Input, Key)
	return Input
def InRound(Input, Key, i):
	# AddRoundKey K[11 - i]
	# print(Key[10 - i])
	Input = ThuatToanAES.AddRoundKey(Input, Key)
	# print(Input)
	if i < 10:
		# In MixColumns
		if i > 0:
			Input = ThuatToanAES.MixColumns(Input, True)
			# print(Input)
		# InShiftRows
		Input = ThuatToanAES.InShiftRows(Input)
		# InSubBytes
		Input = ThuatToanAES.InSubBytesMatrix(Input)
		# print(Input)
	return Input
def MaHoa(K, M):
	W = TaoW(K)
	Key = TaoKey(W)
	for i in Key:
		# print(i)
		pass
	Input = TaoInput(M)
	# Lặp
	for i in range(11):
		Input = Round(Input, i, Key[i])
	C = ThuatToanAES.GhepOutput(Input)
	# print("C:", C)
	return C
def GiaiMa(C, K):
	W = TaoW(K)
	Key = TaoKey(W)
	for i in Key:
		# print(i)
		pass
	# print(C)
	Input = ThuatToanAES.StringToMatrixLat(C)
	# print(Input)
	# Lặp
	for i in range(11):
		Input = InRound(Input, Key[10 - i], i)
	M = ThuatToanAES.GhepOutput(Input)
	# print(M)
	return M
def main():
	GiaiMa(MaHoa(K, M), K)
main()
