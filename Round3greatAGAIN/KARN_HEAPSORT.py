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


def print90(a,index = 0,level = 0):
  if index < len(a):
    print90(a,2*index+2,level+1)
    print(' '*level*3,end = '')
    print(a.nodeAt(index).data)
    print90(a,2*index+1,level+1)

def insert(a,d):
  a.append(d)
  perlocate(a,d)

def perlocate(a,d):
  index = a.indexOf(d)
  if index != 0:
    if index%2 == 0:
      #right subtree
      fatherIndex = (int)((index-2) / 2)
    else:
      #left subtree
      fatherIndex = (int)((index-1) / 2)
    if a.nodeAt(fatherIndex).data > d:
      temp = a.nodeAt(fatherIndex).data
      a.nodeAt(fatherIndex).data = d
      a.nodeAt(index).data =  temp
      perlocate(a,d)
    else:
      return

def deleteMin(a):
  holeIndex = 0
  temp = a.nodeAt(holeIndex).data
  holeLeftIndex = holeIndex*2 + 1
  holeRightIndex = holeIndex*2 + 2
  while (holeLeftIndex < len(a) or holeRightIndex < len(a)):
    if holeLeftIndex < len(a) and holeRightIndex < len(a):
      if a.nodeAt(holeLeftIndex).data > temp    and     a.nodeAt(holeRightIndex).data > temp:
        a.nodeAt(holeIndex).data = a.nodeAt(holeLeftIndex).data if a.nodeAt(holeLeftIndex).data < a.nodeAt(holeRightIndex).data else a.nodeAt(holeRightIndex).data
        holeIndex = holeLeftIndex if a.nodeAt(holeLeftIndex).data < a.nodeAt(holeRightIndex).data else holeRightIndex
      elif a.nodeAt(holeLeftIndex).data > temp    or    a.nodeAt(holeRightIndex).data > temp:
        a.nodeAt(holeIndex).data = a.nodeAt(holeLeftIndex).data if a.nodeAt(holeLeftIndex).data > temp else a.nodeAt(holeRightIndex).data
        holeIndex = holeLeftIndex if a.nodeAt(holeLeftIndex).data > temp else holeRightIndex
      else: break
    else:
      if holeLeftIndex < len(a) and a.nodeAt(holeLeftIndex).data > temp:
        a.nodeAt(holeIndex).data = a.nodeAt(holeLeftIndex).data
        holeIndex = holeLeftIndex
      elif holeRightIndex < len(a) and a.nodeAt(holeRightIndex).data > temp:
        a.nodeAt(holeIndex).data = a.nodeAt(holeRightIndex).data
        holeIndex = holeRightIndex     
      else: break   
    ###
    holeLeftIndex = holeIndex*2 + 1
    holeRightIndex = holeIndex*2 + 2
  a.nodeAt(holeIndex).data = temp
  return temp
    
###############################################
inpt = [68, 65, 32, 24, 26, 21, 19, 13, 16, 14]
print ('input array = ',inpt)
heap = DoublyLinkedList()
acs = []
for ele in inpt:
  print('insert ',ele)
  ##################
  insert(heap,ele)
  ##################
  print(heap,sep = ' ')
  print90(heap)
  print('------------')

print('***deleteMin***')
print('input heap:\n')
print(heap,sep=' ')
print90(heap)
print('==== heap sort ====')
for i in range(len(heap)):
  print('deleteMin =',heap.nodeAt(0).data,end = ' FindPlaceFor ')
  acs.append(deleteMin(heap))
  print(heap.nodeAt(0).data)
  print(heap,sep=' ')
  print90(heap)

print('==== Sorting ascending ====')
print(*acs,sep=' ')
print('==== Sorting descending ====')
print(heap,sep=' ')

print()
print('Finished')