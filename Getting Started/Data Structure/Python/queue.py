class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def test():
    q = Queue()
    print(q.isEmpty())
    print(q.enqueue(4))
    print(q.enqueue("dog"))
    print(q.enqueue(True))
    print(q.enqueue(8.4))
    print(q.size())
    print(q.isEmpty())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())

# Name list is a list of names
# Num is each num time a person gets eliminated


def joseph(namelist: "List[str]", num: int) -> str:
    q = Queue()
    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()

# Simulate a printer


def printer(numSeconds, pagesPerminute):
    import random

    class Printer:
        # page per min - ppm
        def __init__(self, ppm: float):
            self.pagerate = ppm
            self.currentTask = None
            self.timeRemaining = 0

        def tick(self):
            if self.currentTask != None:
                self.timeRemaining = self.timeRemaining - 1
                if self.timeRemaining <= 0:
                    self.currentTask = None

        def busy(self):
            if self.currentTask != None:
                return True
            else:
                return False

        def startNext(self, newtask):
            self.currentTask = newtask
            self.timeRemaining = newtask.getPages() * 60 / self.pagerate

    class Task:
        def __init__(self, time: float):
            self.timestamp = time
            self.pages = random.randint(1, 21)

        def getStamp(self) -> float:
            return self.timestamp

        def getPages(self) -> int:
            return self.pages

        def waitTime(self, currenttime: float) -> float:
            return currenttime - self.timestamp

    def newPrintTask() -> bool:
        num = random.randint(1, 181)
        if num == 180:
            return True
        else:
            return False

    labPrinter = Printer(pagesPerminute)
    q = Queue()
    waitingtime = []

    for cur in range(numSeconds):
        if newPrintTask():
            t = Task(cur)
            q.enqueue(t)

        if (not labPrinter.busy()) and (not q.isEmpty()):
            nextTask = q.dequeue()
            waitingtime.append(nextTask.waitTime(cur))
            labPrinter.startNext(nextTask)
        labPrinter.tick()

    avgWait = sum(waitingtime)/len(waitingtime)
    print("Average Wait %6.2f secs %3d tasks remaining" %
          (avgWait, q.size()))


for i in range(10):
    printer(3600, 5)
    break
