from linkedList import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        cur = self.head
        prev = None
        stop = False
        while cur and not stop:
            if cur.getData() > item:
                stop = True
            else:
                prev = cur
                cur = cur.getNext()
        temp = Node(item)
        if prev == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(cur)
            prev.setNext(temp)

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
        stop = False
        while cur != None and not found and not stop:
            if cur.getData() == item:
                found = True
            else:
                if cur.getData() > item:
                    stop = True
                else:
                    cur = cur.getNext()
        return found
