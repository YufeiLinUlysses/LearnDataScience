class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self,item):
        self.items.append(item)
    
    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
def checkPal(string:str)->bool:
    dq = Deque()
    for c in string:
        dq.addRear(c)
    
    equal = True

    while dq.size() > 1 and equal:
        first = dq.removeFront()
        last = dq.removeRear()
        if first != last:
            return False
    return equal