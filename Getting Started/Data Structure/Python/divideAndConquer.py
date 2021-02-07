def recMC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        temp = [c for c in coinValueList if c <= change]
        for i in temp:
            numCoins = 1 + recMC(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins


def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(1, change + 1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins
        minCoins[cents] = coinCount
    return minCoins[change]


def bag(treasure, maxWeight):
    m = {(i, w): 0 for i in range(len(treasure)) for w in range(maxWeight + 1)}

    for i in range(1, len(treasure)):
        for w in range(1, maxWeight + 1):
            if treasure[i]['w'] > w:
                m[(i, w)] = m[(i-1, w)]
            else:
                m[(i, w)] = max(m[(i-1, w)],
                                m[(i-1, w-treasure[i]['w'])] + treasure[i]['v'])
    return m[(len(treasure) - 1, maxWeight)]


treasure = [None, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {
    'w': 4, 'v': 8}, {'w': 5, 'v': 8}, {'w': 9, 'v': 10}]
maxWeight = 20
print(bag(treasure, maxWeight))
