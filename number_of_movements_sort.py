def minimumSwaps(arr):
    '''
        a = [i for i in arr]
        a.sort()
        track = 0
        counter = -1
        for i in range(0,len(arr)):
            if a[i] != arr[i]:
                counter += 1
            else:
                track += 1
        return track
        '''
# This is the code found that pass the test
    count = 0
    i = 0
    while (i < len(arr) - 1):
        # print(i)
        # print("swaps", numSwaps)
        if arr[i] != i + 1:
            tmp = arr[i]
            arr[i], arr[tmp - 1] = arr[tmp - 1], arr[i]
            count += 1
        else:
            i += 1
    return count

    '''
    counter = 0
    for i in range(len(arr)):

            if (arr[i]) != i+1:
                    l = arr.index(i+1)
                    arr[i],arr[l] = i+1,arr[i]
                    counter += 1


    return counter    
    '''




if __name__ == "__main__":
    a = [2,31,1,38,29,5,44,6,12,18,39,9,48,49,13,11,7,27,14,33,50,21,46,23,15,26,8,47,40,3,32,22,34,42,16,41,24,10,4,28,36,30,37,35,20,17,45,43,25,19]
    print(minimumSwaps(a))


         #finish this exercise, create a GCP account (google clould platform)