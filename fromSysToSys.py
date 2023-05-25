def fromSysToSys(n,s1,s2) :
    decn1 = 0
    nList = list(str(n)[::-1])
    for i in range(len(nList)) :
        nList[i] = int(nList[i])
    for i in range(len(nList)) :
        decn1 += nList[i]*(s1**i)
    output = ""
    while (decn1 > 0) :
        output = str(decn1 % s2) + output
        decn1 = decn1 // s2
    return int(output)


print(fromSysToSys(24,10,2))