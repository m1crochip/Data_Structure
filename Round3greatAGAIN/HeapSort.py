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
        s = 'LinkedList Data    :   '
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


def print90(l, index=0, level=0):
    if index < len(l):
        print90(l, 2*index+2, level+1)
        print(' '*level*3, end=' ')
        print(l.nodeAt(index).data)
        print90(l, 2*index+1, level+1)
def insert(l, data):
    l.append(data)
    minHeap(l, data)

INPUT = [68, 65, 32, 24, 26, 21, 19, 13, 16, 14]
def minHeap(l, data):
    index = l.indexOf(data)
    if index != 0:
        if index%2 == 0:
            prev_index = (int)((index-2)/2)
        else:
            prev_index = (int)((index-1)/2)

        if l.nodeAt(prev_index).data > data:
            #SWAP
            temp = l.nodeAt(prev_index).data
            l.nodeAt(prev_index).data = data
            l.nodeAt(index).data = temp
            minHeap(l,data)
        else:
            return

def deleteMin(l):
    HL = 0
    temp = l.nodeAt(HL).data;
    # Left_INDEX // Right_INDEX
    LI = HL * 2 + 1
    RI = HL * 2 + 2
    while LI < len(l) and RI < len(l):
        L_data = l.nodeAt(LI).data
        R_data = l.nodeAt(RI).data
        if LI < len(l) and RI < len(l):
            if L_data > temp and R_data > temp:
                l.nodeAt(HL).data = L_data if L_data < R_data else R_data
                HL = LI if L_data < R_data else RI

            elif L_data > temp or R_data > temp:
                l.nodeAt(HL).data = L_data if L_data > temp else R_data
                HL = LI if L_data > R_data else RI
            else:
                break
        else:
            if LI < len(l) and L_data > temp:
                l.nodeAt(HL).data = L_data
                HL = LI
            elif RI < len(l) and R_data > temp:
                l.nodeAt(HL).data = R_data
                HL = RI
            else:
                break
        
        LI = HL * 2 + 1
        RI = HL * 2 + 2
    l.nodeAt(HL).data = temp
    return temp

L = DoublyLinkedList()
asc = []
for i in INPUT:
    print('insert : ',i)
    insert(L, i)
    print(L, sep=' ')
    print90(L,0,0)
    print('--------------------------------')

print('delete MIN or >>> minHEAP goto maxHEAP')
print(L,sep=' ')
print90(L)

for i in range(len(L)):
    print('deleteMin =',L.nodeAt(0).data,end = ' FindPlaceFor ')
    asc.append(deleteMin(L))
    print(L.nodeAt(0).data)
    print(L,sep=' ')
    print90(L)

print('==== Sorting ascending ====')
print(*asc,sep=' ')
print('==== Sorting descending ====')
print(L,sep=' ')

print()
print('Finished')












