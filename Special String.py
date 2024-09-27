def specialString(a,s):
    totalCost=0
    for i in a:
        if i not in s:
            distance=9999
            for j in s:
                tempDist=abs(ord(i)-ord(j))
                if tempDist
