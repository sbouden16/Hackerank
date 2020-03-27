def jumpingOnClouds(c):
    i = 0
    jumps = 0
    while i < len(c) - 1:
        if i == len(c) - 2:
            return jumps + 1
        if c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    return jumps


if __name__ == "__main__":
    c = [[0, 1, 0, 0, 0, 1, 0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,1,0,0,1,0],[0,0,1,0,0,0,0,1,0,0]]
    for i in c:
        print(jumpingOnClouds(i))


#wojtek

