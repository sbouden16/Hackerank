def countingValleys(n, s):
    a = [-1 if i=="D" else 1 for i in s]
    count = 0
    valley = 0
    c = []
    for step in a:
        if step == 1:
            count += step
            #c.append(count)
            if count == 0:
                valley +=1
        else:
            count += step
    #for i in range(0,len(c)):
        #if c[i] == 0 and a[i] == 1:
            #valley +=1 
    return valley

n = 8
s = ["D","D","U","U","U","U","D","U"]
print(countingValleys(n,s))