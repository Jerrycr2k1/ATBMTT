import re
string = "attack postponed until two am"
key = [4, 3, 1, 2, 5, 6, 7]

def CreateMaDichChuyenDong(string, key):
    # xóa dấu cách
    string = re.sub(r"\s+", "", string, flags=re.UNICODE)
    res = ""
    # số dòng
    k = len(string) // len(key) + (1 if len(string) % len(key) != 0 else 0)
    # các dòng
    _dong = [[] for i in range(k)]
    for i in range(k):
        # nếu độ dài khóa > số lượng từ thì thêm các chữ cái cuối trong bảng chũ cái
        for j in range(len(key) - len(string)):
            string += chr(122 - (len(key) - len(string)) + 1)
        # dòng thứ i lấy đi len(key) chữ cái đầu tiên trong string còn lại
        _dong[i] = string[:len(key)]
        # giảm string
        string = string[len(key):]

    for i in range(1, len(key) + 1):
        # dong tiếp theo trong dãy mới
        vt = 0
        # tìm dòng tiếp theo
        for j in key:
            if j == i:
                break
            vt += 1
        # thêm dòng tiếp theo
        for j in _dong:
            res += j[vt]
    return res
def CreateMaDichChuyenDong2(string, key):
    # xóa dấu cách
    string = re.sub(r"\s+", "", string, flags=re.UNICODE)
    # Thêm kí tự vào cuối 
    for i in range(len(key) - len(string) % len(key)):
        string += chr(122 - (len(key) - len(string) % len(key)) % len(key) + 1)
    res = ""
    # số dòng
    k = len(string) // len(key)
    # mảng có thứ tự mới
    arr = ["" for i in range(len(string))]
    t = 0
    # đảo vị trí các kí tự về vị trí mới
    for j in range(k):
        for i in key:
            arr[k * (i - 1) + j] = string[t]
            t += 1
    # gộp mảng thành dãy mới
    for i in arr:
        res += i
    return res

def CreateMaDichChuyenDong3(string, key):
    # xóa dấu cách
    string = re.sub(r"\s+", "", string, flags=re.UNICODE)
    # Thêm kí tự vào cuối 
    for i in range(len(key) - len(string) % len(key)):
        string += chr(122 - (len(key) - len(string) % len(key)) % len(key) + 1)
    res = ""
    # số dòng
    k = len(string) // len(key)
    # mảng có thứ tự mới
    arr = [[] for i in range(k)]
    # đảo vị trí các kí tự về vị trí mới
    for i in range(k):
        arr[i] = string[len(key) * i : len(key) * i + len(key)]
    
    for i in range(1, len(key) + 1):
        # dong tiếp theo trong dãy mới
        vt = 0
        # tìm dòng tiếp theo
        for j in key:
            if j == i:
                break
            vt += 1
        # thêm dòng tiếp theo
        for j in arr:
            res += j[vt]
    return res

def Decrypt(string, key):
    # xóa dấu cách
    string = re.sub(r"\s+", "", string, flags=re.UNICODE) 
    res = ""
    # Số dòng
    k = len(string) // len(key) + (1 if len(string) % len(key) != 0 else 0)
    # chuyển dòng về vị trí cũ
    for j in range(k):
        for i in key:
            res += string[k * (i - 1) + j]
    return res
# print(CreateMaDichChuyenDong(string, key))
# print(Decrypt('ttnaaptmtsuoaodwcoixknlypetz', key))
# print(CreateMaDichChuyenDong2(string, key))
# print(CreateMaDichChuyenDong3(string, key))