class Queue:

    def __init__(self, list=None):
        if list == None:
            self.item = []
        else:
            self.item= list

    def __init__(self):
        self.item = []
    
    def Enqueue(self, x):
        self.item.append(x)

    def Dequeue(self):
        self.item.pop(0)
    
    def get(self):
        return self.item[0]

    def show(self):
        return self.item
    
    def size(self):
        return len(self.item)
