class Node:
    def __init__(self, data, Next=None):
        if data is None:
            self.data = None
        else:
            self.data = data

        if Next is None:
            self.next = None
        else:
            self.next = Next

    def __str__(self):
        return str(self.data)

    def setData(self, data):
        self.data = data
    def setNext(self, Next=None):
        if Next is None:
            self.next = None
        else:
            self.next = Next
    def getData(self):
        return self.data
    def getNext(self):
        return self.next

