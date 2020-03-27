dict = {1:1,2:2,3:4}

def step(n):
    if n in dict.keys():
        return dict.get((n))
    result = step(n-3)+step(n-2) + step(n-1)
    dict[n]=result
    return dict.get(n)

def stepPerms(n):
    #temp_val = [0 for i in range(n)] #% 10000000007
    return step(n)

"""

steps=[1,2,3]
cache={}

def climb(n):
    global cache
    leaves=0

    if n < 0: return
    for s in steps:
        if n - s >= 0:
            if cache.has_key(n-s):
                subres=cache[(n-s)]
            else:
                subres=climb(n - s)
                cache[(n - s)] = subres
            leaves+=subres
        if n - s == 0:
            leaves += 1
    return leaves
"""