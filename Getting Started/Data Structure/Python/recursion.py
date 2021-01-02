def listSum(numList: "List[int]") -> int:
    if len(numList) == 1:
        return numList[0]
    return numList[0] + listSum(numList[1:])


def changeBase(num: int, base: int) -> str:
    baseStr = "0123456789ABCDEF"
    if num < base:
        return baseStr[num]
    return changeBase(num//base, base) + baseStr[num % base]
