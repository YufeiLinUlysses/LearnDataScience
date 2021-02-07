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
