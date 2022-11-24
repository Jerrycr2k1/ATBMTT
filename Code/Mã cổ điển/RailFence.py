import re
string = "ABADBEGINNINGMAKES"
key = 9

def CreateRailFence(string, key):
    _dong = [[] for i in range(key)]
    for i in range(len(string)):
        _dong[i%key].append(string[i])
    res = ""
    for i in _dong:
        for j in i:
            res += j
    return res

def CreateRailFence2(string, key):
    res = ""
    for i in range(key):
        res += re.sub(r"\s+", "", string, flags=re.UNICODE)[i:len(re.sub(r"\s+", "", string, flags=re.UNICODE)):key]
    return res

def Decrypt(string, key):
    _dong = [[] for i in range(key)]
    them = ""
    for i in range(key - len(string) % key):
        them += " "
    string += them
    for t in range(key):
        for i in range(len(string) // key):
            _dong[t].append(string[i + t * len(string) // key])
    res = ""
    for i in range(len(string) // key):
        for j in range(len(_dong)):
            res += _dong[j][i]
    return re.sub(r"\s+", "", res, flags=re.UNICODE)

def Decrypt2(string, key):
    res = ""
    for i in range(len(string) // key + (1 if len(string) % key != 0 else 0)):
        res += re.sub(r"\s+", "", string, flags=re.UNICODE)[i:len(re.sub(r"\s+", "", string, flags=re.UNICODE)):len(string) // key + (1 if len(string) % key != 0 else 0)]
    return res

def Decoder(string):
    for i in range(1, len(string)):
        print(Decrypt(string, i))
print(CreateRailFence(re.sub(r"\s+", "", string, flags=re.UNICODE), key))
# print(Decrypt('mematrhtgpryetefeteoaat', key))

print(CreateRailFence2(string, key))
# print(Decrypt2('ANBIANDGBMEAGKIENS', key))

# Decoder('mematrhtgpryetefeteoaat')