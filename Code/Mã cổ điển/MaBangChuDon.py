Goc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Key = "THLEYNPSXADWKFUBOGMQVJRCIZ"
M   = "AWOMANGIVESANDFO"
# Từ điển biến đổi
Dict_Create = {} # từ điển tạo
Dict_Decrypt = {} # từ điển giải
for i in range(len(Key)):
    Dict_Create[Goc[i]] = Key[i]
Dict_Create[" "] = " "
for i in range(len(Key)):
    Dict_Decrypt[Key[i]] = Goc[i]
Dict_Decrypt[" "] = " "

def Create(M):
    M = M.upper()
    res = ""
    for i in M:
        res += Dict_Create[i]
    return res

def Decrypt(M):
    M = M.upper()
    res = ""
    for i in M:
        res += Dict_Decrypt[i]
    return res

def main():
    print(Create(M))
    print(Decrypt(Create(M)))
main()