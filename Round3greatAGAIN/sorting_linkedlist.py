class DoublyLinkedList:
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            if prev is None:
                self.prev = None
            else:
                self.prev = prev
            if next is None:
                self.next = None
            else:
                self.next = next

    def __init__(self):
        self.header = self.Node(None, None, None)
        self.header.next = self.header.prev = self.header
        self.size = 0

    def __str__(self):
        s = '>>>>>'
        p = self.header.next
        for _ in range(len(self)):
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def indexOf(self, data):
        q = self.header.next
        for i in range(len(self)):
            if q.data == data:
                return i
            q = q.next
        return -1

    def isIn(self, data):
        return self.indexOf(data) >= 0

    def nodeAt(self, i):
        p = self.header
        for _ in range(-1, i):
            p = p.next
        return p

    def insertBefore(self, q, data):
        p = q.prev
        x = self.Node(data, p, q)
        p.next = q.prev = x
        self.size += 1

    def append(self, data):
        self.insertBefore(self.nodeAt(len(self)), data)

    def add(self, i, data):
        self.insertBefore(self.nodeAt(i), data)

    def removeNode(self, q):
        p = q.prev
        x = q.next
        p.next = x
        x.prev = p
        self.size -= 1

    def delete(self, index):
        self.removeNode(self.nodeAt(index))

    def remove(self, data):
        q = self.header.next
        while q != self.header:
            if q.data == data:
                self.removeNode(q)
                break
            q = q.next

    
l = [82, 52, 1, 13, 78, 9, 66, 60, 55, 78, 15, 14, 48, 89, 77]
LL = DoublyLinkedList()
for i in l:
    LL.append(i)

print(LL)

def bubbleSORT(l, mode):
    length = len(l)
    if mode is 'A':
        for i in range(0, length, +1):
            for j in range(i+1, length, +1):
                if l.nodeAt(j).data < l.nodeAt(i).data:
                    temp = l.nodeAt(j).data
                    l.nodeAt(j).data = l.nodeAt(i).data
                    l.nodeAt(i).data = temp
    else:
        for i in range(0, length, +1):
            for j in range(i+1, length, +1):
                if l.nodeAt(j).data > l.nodeAt(i).data:
                    temp = l.nodeAt(j).data
                    l.nodeAt(j).data = l.nodeAt(i).data
                    l.nodeAt(i).data = temp
    return l

def selectionSORT(l, mode):
    length = len(l)
    if mode is 'D': # max to min
        for i in range(0,length,+1):
            indexMIN = i
            for j in range(i+1,length,+1):
                if l.nodeAt(j).data > l.nodeAt(i).data:
                    indexMIN = j
            temp = l.nodeAt(i).data
            l.nodeAt(i).data = l.nodeAt(indexMIN).data
            l.nodeAt(indexMIN).data = temp
    else:
        for i in range(0,length,+1):
            indexMIN = i
            for j in range(i+1,length,+1):
                if l.nodeAt(j).data < l.nodeAt(i).data:
                    indexMIN = j
            temp = l.nodeAt(i).data
            l.nodeAt(i).data = l.nodeAt(indexMIN).data
            l.nodeAt(indexMIN).data = temp
    return l

def insertionSORT(l, mode):
    length = len(l)
    if mode is 'D':
        for i in range(1,length,+1):
            temp = l.nodeAt(i).data
            j = i
            while j > 0 and l.nodeAt(j-1).data < temp:
                l.nodeAt(j).data = l.nodeAt(j-1).data
                j-=1
            l.nodeAt(j).data = temp
    else:
        for i in range(1,length,+1):
            temp = l.nodeAt(i).data
            j = i
            while j > 0 and l.nodeAt(j-1).data > temp:
                l.nodeAt(j).data = l.nodeAt(j-1).data
                j-=1
            l.nodeAt(j).data = temp
    return l

def shellSORT(l, mode):
    length = len(l)
    gap = length//2
    if mode is 'A':
        while gap > 0:
            for i in range(gap, length):
                temp = l.nodeAt(i).data
                j = i
                while j >= gap and l.nodeAt(j-gap).data > temp:
                    l.nodeAt(j).data = l.nodeAt(j-gap).data
                    j -= gap
                l.nodeAt(j).data = temp
            gap //= 2
    else:
        while gap > 0:
            for i in range(gap, length):
                temp = l.nodeAt(i).data
                j = i
                while j >= gap and l.nodeAt(j-gap).data < temp:
                    l.nodeAt(j).data = l.nodeAt(j-gap).data
                    j -= gap
                l.nodeAt(j).data = temp
            gap //= 2
    return l

print("BUBBLE : ",bubbleSORT(LL, 'A'))
print("SELECTION : ",selectionSORT(LL, 'A'))
print("BUBBLE : ",insertionSORT(LL, 'A'))
print(shellSORT(LL, 'A'))