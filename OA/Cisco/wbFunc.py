def wbFunc(strSize):
    modTwo = strSize // 2 + (1 if strSize % 2 else 0)
    str1, str2 = ''.join(['WB'] * modTwo), ''.join(['BW'] * modTwo)
    if strSize % 2:
        str1, str2 = str1[:-1], str2[:-1]
    retStr = [str1+'\n'+str2+'\n'] * modTwo
    if strSize % 2:
        retStr = retStr[:-1]
        retStr.append(str1)
    print(''.join(retStr))
    
wbFunc(5)