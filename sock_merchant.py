def sockMerchant(n, ar):
    dic = {}
    myset = set(ar)
    #print(ar)
    #print(myset)
    for i in myset:
        x = ar.count(i)
        dic[i]=x
    return sum([y//2 for y in dic.values()])

if __name__ ==  "___main__":
    pass