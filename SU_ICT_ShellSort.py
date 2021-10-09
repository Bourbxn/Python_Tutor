def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


numList = [22, 32, 37, 24, 9, 27, 28, 1, 12, 13]
shellSort(numList, len(numList))
for i in numList:
    print(i,end=' ')