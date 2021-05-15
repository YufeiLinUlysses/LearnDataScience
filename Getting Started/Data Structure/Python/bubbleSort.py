def bubbleSort(aList):
    for p in range(len(aList) - 1, 0 , -1):
        for i in range(p):
            if aList[i] > aList[i+1]:
                aList[i], aList[i+1] = aList[i+1], aList[i]

def fastBubbleSort(aList):
    exchange = True 
    p = len(aList) - 1
    while p > 0 and exchange:
        exchange = False
        for i in range(p):
            if aList[i] > aList[i+1]:
                exchange = True
                aList[i], aList[i+1] = aList[i+1], aList[i]
        p -= 1

def selectionSort(aList):
    for i in range(len(aList) - 1, 0, -1):
        p = 0
        for j in range(1,i+1):
            if aList[j] > aList[i]:
                p = j
        aList[i], aList[p] = aList[p],aList[i]

def insertionSort(aList):
    for i in range(1,len(aList)):
        cur = aList[i]
        pos = i
        while pos > 0 and aList[pos - 1] > cur:
            aList[pos] = aList[pos - 1]
            pos -= 1
        aList[pos] = cur

def shellSort(aList):
    cnt = len(aList) // 2
    while cnt > 0:
        for i in range(cnt):
            gapInsertionSort(aList, i, cnt)
        cnt = cnt // 2

def gapInsertionSort(aList, i, cnt):
    for j in range(i+cnt, len(aList), cnt):
        cur = aList[i]
        pos = i 
        while pos >= cnt and aList[pos-cnt] > cur:
            aList[pos] = aList[pos-cnt]
            pos-=cnt
        aList[pos] = cur

def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left = mergeSort(lst[:middle])
    right = mergeSort(lst[middle:])

    merged = []
    while left and right:
        if left[0]<= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)
    return merged

def quickSort(lst):
    quickSortHelper(lst, 0,len(lst)-1)

def quickSortHelper(lst, first, last):
    if first < last:
        split = partition(lst, first, last)
        quickSortHelper(lst, first, split - 1)
        quickSortHelper(lst, split + 1, last)

def partition(lst, first, last):
    pivot = lst[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while left <= right and lst[left] <= pivot:
            left += 1
        while lst[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            temp = lst[left]
            lst[left] = lst[right]
            lst[right] = temp 
    temp = lst[first]
    lst[first] = lst[right]
    lst[right] = temp
    return right
