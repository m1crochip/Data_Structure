class Queue:
    def __init__(self):
        self.item = []

    def size(self):
        return len(self.item)
    def __str__(self):
        return str(self.item)
    def isEmpty(self):
        return self.size()==0
    def isFull(self):
        pass
        # need setting how much it's full
    def enQueue(self,sth):
        self.item.append(sth)
    def deQueue(self):
        return self.item.pop(0)