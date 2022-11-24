key = "THEDIEIS"
string = "THETRUTHWILLOU"
BangChuCai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# key = "MONARCHY"
# string = "balloon"
MaTranPlayfair = [["" for i in range(5)] for i in range(5)]
# Dict = {}
Lap = [""]
def TaoMaTran(key, Dict):
	key = key.upper()
	key_set = []
	for i in key:
		if i not in key_set:
			key_set.append(i)
	check = 3
	if "I" in key_set and "J" in key_set:
		check = 2
	else: 
		if "I" in key_set or "J" in key_set:
			if "I" in key_set:
				check = 0
			else:
				check = 1
	for i in BangChuCai:
		if i not in key_set:
			key_set.append(i)
	if check == 2:
		key_set.pop(len(key_set) - 1)
	if check == 0 or check == 3:
		key_set.remove("J")
	if check == 1:
		key_set.remove("I")
	for i in range(5):
		for j in range(5):
			if len(key_set) > 0:
				Dict.update({key_set[0]: [i, j]})
				MaTranPlayfair[i][j] = key_set[0]
				key_set.pop(0)
	return MaTranPlayfair
def TimChuLap(string, key):
	Dict = {}
	_MaTranPlayfair = TaoMaTran(key, Dict)
	myset = set()
	for i in string:
		myset.add(i)
	for i in key:
		myset.add(i)
	for i in BangChuCai:
		if i not in myset:
			# print(myset, i)
			return i
def TachBangRo(string, key):
	string = string.upper()
	stringcopy = string
	_string = [] 
	check = False
	# TimChuLap(string, key)
	while len(string) > 0:
		if len(string) == 1:
			_string.append(string + TimChuLap(stringcopy, key))
			check = True
			break
		if string[0] != string[1]:
			_string.append(string[:2])
			string = string[2:]
		else:
			_string.append(string[0] + TimChuLap(stringcopy, key))
			check = True
			string = string[1:]
	# print(_string)
	return _string, check
def TachString(string):
	string = string.upper()
	_string = []
	while len(string) > 0:
		_string.append(string[:2])
		string = string[2:]
	return _string
def GetVT(char, Dict):
	return Dict[char]
def SoSanhVT(VT1, VT2):
	if VT1[0] == VT2[0]:
		return "Cùng hàng"
	if VT1[1] == VT2[1]:
		return "Cùng cột"
	return "Khác hàng, khác cột"
def SoSanh(i, Dict):
	# print(GetVT(i[0], Dict), GetVT(i[1], Dict))
	return SoSanhVT(GetVT(i[0], Dict), GetVT(i[1], Dict))
def DichPhai(MaTranPlayfair, Dict, i):
	# Lấy vt
	VT1 = GetVT(i[0], Dict)
	VT2 = GetVT(i[1], Dict)
	# Dịch phải xoay vòng
	VT1 = [VT1[0], (VT1[1] + 1) % 5]
	VT2 = [VT2[0], (VT2[1] + 1) % 5]
	text1 = MaTranPlayfair[VT1[0]][VT1[1]]
	text2 = MaTranPlayfair[VT2[0]][VT2[1]]
	return(text1+text2)
def DichDuoi(MaTranPlayfair, Dict, i):
	# Lấy vt
	VT1 = GetVT(i[0], Dict)
	VT2 = GetVT(i[1], Dict)
	# Dịch dưới xoay vòng
	VT1 = [(VT1[0] + 1) % 5, VT1[1]]
	VT2 = [(VT2[0] + 1) % 5, VT2[1]]
	text1 = MaTranPlayfair[VT1[0]][VT1[1]]
	text2 = MaTranPlayfair[VT2[0]][VT2[1]]
	return(text1+text2)
def DichTrai(MaTranPlayfair, Dict, i):
	# Lấy vt
	VT1 = GetVT(i[0], Dict)
	VT2 = GetVT(i[1], Dict)
	# Dịch phải xoay vòng
	VT1 = [VT1[0], (VT1[1] + 4) % 5]
	VT2 = [VT2[0], (VT2[1] + 4) % 5]
	text1 = MaTranPlayfair[VT1[0]][VT1[1]]
	text2 = MaTranPlayfair[VT2[0]][VT2[1]]
	return(text1+text2)
def DichLen(MaTranPlayfair, Dict, i):
	# Lấy vt
	VT1 = GetVT(i[0], Dict)
	VT2 = GetVT(i[1], Dict)
	# Dịch dưới xoay vòng
	VT1 = [(VT1[0] + 4) % 5, VT1[1]]
	VT2 = [(VT2[0] + 4) % 5, VT2[1]]
	text1 = MaTranPlayfair[VT1[0]][VT1[1]]
	text2 = MaTranPlayfair[VT2[0]][VT2[1]]
	return(text1+text2)
def DichCheo(MaTranPlayfair, Dict, i):
	# Lấy vt
	VT1 = GetVT(i[0], Dict)
	VT2 = GetVT(i[1], Dict)
	# Lưu vt vào biến tạm
	vt1 = VT1
	vt2 = VT2
	# Dịch chéo
	VT1 = [vt1[0], vt2[1]]
	VT2 = [vt2[0], vt1[1]]
	text1 = MaTranPlayfair[VT1[0]][VT1[1]]
	text2 = MaTranPlayfair[VT2[0]][VT2[1]]
	return(text1+text2)
def TraBang(listString, MaTranPlayfair, Dict):
	newlistString = []
	for i in listString:
		if SoSanh(i, Dict) == "Cùng hàng":
			newlistString.append(DichPhai(MaTranPlayfair, Dict, i))
			continue
		if SoSanh(i, Dict) == "Cùng cột":
			newlistString.append(DichDuoi(MaTranPlayfair, Dict, i))
			continue
		if SoSanh(i, Dict) == "Khác hàng, khác cột":
			newlistString.append(DichCheo(MaTranPlayfair, Dict, i))
		# if i[0]
		# GetVT(i[0], Dict)
	return newlistString
def TraBangNguoc(listString, MaTranPlayfair, Dict):
	newlistString = []
	for i in listString:
		if SoSanh(i, Dict) == "Cùng hàng":
			newlistString.append(DichTrai(MaTranPlayfair, Dict, i))
			continue
		if SoSanh(i, Dict) == "Cùng cột":
			newlistString.append(DichLen(MaTranPlayfair, Dict, i))
			continue
		if SoSanh(i, Dict) == "Khác hàng, khác cột":
			newlistString.append(DichCheo(MaTranPlayfair, Dict, i))
		# if i[0]
		# GetVT(i[0], Dict)
	return newlistString
def listStringToString(listString):
	res = ""
	for i in listString:
		res += i
	return res
def listStringToStringLap(listString, Lap):
	res = ""
	for i in listString:
		if Lap not in i:
			res += i
		else:
			res += i.replace(Lap, "")
	return res
def create(string, key):
	Dict = {}
	MaTranPlayfair = TaoMaTran(key, Dict)
	# print(MaTranPlayfair)
	listString, check = TachBangRo(string, key)
	newlistString = TraBang(listString, MaTranPlayfair, Dict)
	if check:
		print("Chèn chữ", TimChuLap(string.upper(), key.upper()))
	print("Kết quả mã hóa:", listStringToString(newlistString))
	return listStringToString(newlistString), check
def Giai(string, check, key):
	Dict = {}
	MaTranPlayfair = TaoMaTran(key, Dict)
	listString = TachString(string)	
	newlistString = TraBangNguoc(listString, MaTranPlayfair, Dict)
	# print(newlistString)
	t = ""
	if check:
		t = TimChuLap(string.upper(), key.upper())
	print("Kết quả giải mã:", listStringToStringLap(newlistString, t))
def main():
	newString, check =  create(string, key)
	Giai(newString, check, key)
main()
