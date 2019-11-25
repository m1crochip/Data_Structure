class Node:
    def __init__(self, data, Next=None):
        self.data = data
        if Next == None:
            self.next = None
        else:
            self.next = Next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next=None):
        if next == None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return self.data