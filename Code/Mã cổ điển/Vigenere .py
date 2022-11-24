table = []
for i in range(26):
    _table = []
    for j in range(26):
        _table.append((i + j) % 26)
    table.append(_table)

string = "MONEYMAKESTHE"
key = "YOUREON"

def Chuyen(string, key, update):
    string = string.upper()
    key = key.upper()
    string_Num = []
    Key_Num = []
    for i in string:
        string_Num.append(ord(i) - 65)
    for i in range(len(string)):
        if update:
            if i >= len(key):
                Key_Num.append(ord(string[i - len(key)]) - 65)
                continue
    # Basic
        Key_Num.append(ord(key[i % (len(key))]) - 65)
    return string_Num, Key_Num

def Vigenere(string , key, update, Key_Num1):
    string_Num, Key_Num = Chuyen(string, key, update)
    for i in Key_Num:
        Key_Num1[0] += chr(i + 65)
    _res = []
    for i in range(len(string_Num)):
        _res.append((string_Num[i] + Key_Num[i]) % 26)
    res = ""
    for i in _res:
        res += chr(i + 65)
    return res

def Decrypt(string, key, update):
    string_Num, Key_Num = Chuyen(string, key, update)
    
    _res = []
    for i in range(len(string_Num)):
        _res.append((string_Num[i] - Key_Num[i]) % 26)
    res = ""
    for i in _res:
        res += chr(i + 65)
    return res

Key_Num = [""]
IsAutoKey = 1
# 1 Là Autokey, 0 Là khóa lặp
print(Vigenere(string, key, IsAutoKey, Key_Num))
# print(Decrypt(Vigenere(string, key, 1, Key_Num), Key_Num[0], IsAutoKey))

