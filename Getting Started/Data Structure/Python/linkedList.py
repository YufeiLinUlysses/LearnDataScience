class Node:
    def __init__(self, initData=None):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class LinkedList:
    def __init__(self):
        self.head = None

    # Add to head
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        cur = self.head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.getNext()
        return cnt

    def search(self, item):
        cur = self.head
        found = False
        while cur and not found:
            if cur.getData() == item:
                found = True
            else:
                cur = cur.getNext()
        return found

    def remove(self, item):
        cur = self.head
        prev = None
        found = False
        while not found:
            if cur.getData() == item:
                found = True
            else:
                prev = cur
                cur = cur.getNext()

        if prev == None:
            self.head = cur.getNext()
        else:
            prev.setNext(cur.getNext())

    def isEmpty(self):
        return self.head == None
