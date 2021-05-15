# Search in unordered list
def searchUnordered(l: List[int], item: int) -> bool:
    pos = 0
    found = False

    while pos < len(l) and not found:
        if l[pos] == item:
            found = True
        pos += 1
    return found

# Search in ordered list
# Binary search
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if alist[mid] == item:
            found = True 
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


def searchUnordered(l: List[int], item: int) -> bool:
    pos = 0
    found = False
    stop = False
    while pos < len(l) and not found and not stop:
        if l[pos] == item:
            found = True
        elif l[pos] > item:
            stop = True
        pos += 1
    return found
