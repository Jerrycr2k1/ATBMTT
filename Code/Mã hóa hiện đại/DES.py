import ThuatToanDES as Des
K = "B35F59255E3BCB54"
M = "32D604E6C4504149"
def MaHoa(K, M):
	# Hoán vị PC1(K) -> ListHex
	K = Des.HoanViPC1(K)
	# Sinh khóa Key[i] -> ListBin
	Key = Des.SinhKhoa(K)
	# Hiển thị khóa Ki
	for i in range(len(Key)):
		# print("K"+str(i),Des.ListBinToListHex(Key[i]))
		pass
	# Hoán vị IP cho M -> ListBin
	# print(M)
	# print(Des.StringHexToBin(M))
	M = Des.HoanViIP(M)
	# print(M)
	# print(Des.ListBinToListHex(M))
	# Các vòng
	for i in range(1, 17):
		# Hàm F
		L, R = Des.F(M, Key[i], i)
		# M sau các vòng
		M = L + R
		# print("M"+str(i)+" :", M)
		M = Des.StringHexToBin(M)
	M = R + L
	# print(M)
	# print(Des.StringHexToBin(M))
	M = Des.StringHexToBin(R + L)
	# Thực hiện Hoán vị IP-1
	C = Des.HoanViIIP(M)
	# print("C:", Des.ListBinToListHex(C))
	return Des.ListBinToListHex(C)
def GiaiMa(C, K):
	# Hoán vị PC1(K) -> ListHex
	K = Des.HoanViPC1(K)
	# Sinh khóa Key[i] -> ListBin
	Key = Des.SinhKhoa(K)
	# Hiển thị khóa Ki
	for i in range(len(Key)):
		# print("K"+str(i),Des.ListBinToListHex(Key[i]))
		pass
	# Hoán vị IP cho M -> ListBin
	C = Des.HoanViIP(C)
	# Các vòng
	for i in range(1, 17):
		# Hàm F
		L, R = Des.F_1(C, Key[17 - i])
		# C sau các vòng
		C = L + R
		# print("C"+str(i)+" :", C)
		C = Des.StringHexToBin(C)
	# C = R + L
	C = Des.StringHexToBin(R + L)
	# Thực hiện Hoán vị IP-1
	M = Des.HoanViIIP(C)
	# print("M:", Des.ListBinToListHex(M))
	return Des.ListBinToListHex(M)
def main():
	MaHoa(K, M)
	# GiaiMa(MaHoa(K, M), K)
main()