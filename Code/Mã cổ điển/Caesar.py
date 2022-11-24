string = "xin chao moi nguoi"
k = 8
# Mã hóa
def Create(string, k):
	res = ""
	for i in string:
		# Nếu là dấu cách
		if ord(i) == 32:
			res += " "
			continue
		# Nếu là chữ thì lấy vị trí theo bảng A0Z25
		t = (ord(i) - 65) if ord(i) <= 90 else (ord(i) - 97)
		res += chr((t + k) % 26 + 65)
	return res
# Giải mã
def Decrypt(string, k):
	res = ""
	for i in string:
		# Nếu là dấu cách
		if ord(i) == 32:
			res += " "
			continue
		# Nếu là chữ thì lấy vị trí theo bảng A0Z25
		t = (ord(i) - 65) if ord(i) <= 90 else (ord(i) - 97)
		res += chr((t + 26 - k) % 26 + 65)
	return res
# Thám mã
def Decoder(string):
	for i in range(1, 26):
		print(i, Decrypt(string, i))

print("Sau khi mã hóa: " + Create(string, k))

print("Sau khi giải mã: " + Decrypt(Create(string, k), k))

print("Bảng thám mã: ")
Decoder(Create(string, k))
