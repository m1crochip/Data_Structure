from Node import Node
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def size(self):
        temp = self.head
        length = 0
        while temp != None:
            length += 1
            temp = temp.next
        return length

    def isEmpty(self):
        return self.size() == 0

    def append(self, data):
        if isinstance(data , Node):
            newNode = data
        else:
            newNode = Node(data)

        if self.head == None:
            self.head = newNode
        else:
            pointer = self.head
            while True:
                if pointer.next == None:
                    pointer.next = newNode
                    break
                pointer = pointer.next
            
    def addHead(self, data):
        if(self.head == None):
            self.head = data
        else:
            data.next = self.head
            self.head = data

    def isIn(self, data):
        temp = self.head
        found = False
        while temp != None:
            if(temp.data == data):
                found = True
                break
            temp = temp.next
        return found
  
    def before(self, data):
        check = data
        temp = self.head
        count = 0
        if self.isIn(data):
            while (temp.data != check):
                count += 1
                temp = temp.next
            temp = self.head
            for i in range(0,count-1):
                temp = temp.next
            if temp != None:
                print("Found is ",end='')
                print(temp)
        else:
            print("Not Found")

    def remove(self, data):
        head = self.head
        if head.data == data:
            self.removeHead()
        elif self.isIn(data):
            p1 = self.head
            p2 = p1.next
            
            while p2.next != None and p2.data != data:
                p1 = p1.next
                p2 = p2.next
            # print(p2)
            if p2.next != None:
                temp = p2.next
                p2.setNext()
                p1.setNext(temp)
            else:
                p1.setNext()
            
        else:
            print(data,end='')
            print(" isn't in Linkedlist")
        return p2

    def removeTail(self):
        tail = None
        if self.head != None:
            if self.head.next == None:
                tail = self.head
                self.head = None
            else:
                temp = self.head
                while temp.next.next != None:
                    temp = temp.next
                tail = temp.next
                temp.next = None
        return tail

    def getTail(self):
        tail = None
        tail = self.head
        while tail.next != None:
            tail = tail.next
        return tail
    
    def getHead(self):
        tail = self.head
        if self.head != None:
            tail = self.head
        return tail

    def removeHead(self):
        tail = self.head
        if self.head != None:
            self.head = self.head.next
        return tail

    def __str__(self):
        temp = self.head
        s = ''
        while temp != None:
            s += str(temp.data)+' '
            temp = temp.next
        return s
        
    def headtotail(self):
        head = self.removeHead()
        tail = self.getTail()
        head.setNext()
        tail.setNext(head)

    def tailtohead(self):
        tail = self.removeTail()
        self.addHead(tail)

    def insert_specindex(self , data, index_data):
        if isinstance(data , Node):
            newNode = data
        else:
            newNode = Node(data)
        p = self.head
        x = 1
        while True:
            if p.getData() == index_data:
                break
            p = p.next
            x += 1
        index = x
        # print(x)
        if index < 1:
            print("Index can't less than 1")
        elif index > self.size():
            print("Index out boundary of Linkedlist's length")
        else:
            p1 = self.head
            p2 = p1.next
            count = 1
            while count < index:
                p1 = p1.next
                p2 = p2.next
                count += 1
            # print(p1)
            # print(p2)
            newNode.setNext(p2)
            p1.setNext(newNode)

    def riff(self, length):
        p1_to_LL = self.head
        pointer = self.head
        x = 0
        if length >= 5:
            # print("more than 50")
            while x < 10-length:
                count = 0
                while count < length:
                    pointer = pointer.next
                    count += 1
                # print(pointer)
                temp = self.remove(pointer.getData())
                # print(temp.getData())
                pointer = self.head
                self.insert_specindex(temp, p1_to_LL.getData())
                p1_to_LL = temp.next
                length += 1
        else:
            static_length = length
            # print("less than 50")
            while x < static_length:
                # print(length)
                count = 0
                while count < length:
                    pointer = pointer.next
                    count += 1
                # print(pointer)
                temp = self.remove(pointer.getData())
                pointer = self.head
                # print(temp)
                self.insert_specindex(temp, p1_to_LL.getData())
                p1_to_LL = temp.next
                length += 1
                x+=1
    
    def driff(self, length):
        p1 = self.head

        if length >= 5:
            static_length = 10-length
            count = 0
            while count < static_length:
                temp = self.remove(p1.next.getData())
                p1 = p1.next
                self.append(temp.getData())
                count += 1
        else:
            static_length = 10-length
            p1 = self.head
            point_last = self.head
            x = 1
            while x < length:
                count = 0
                # print(static_length)
                while count < static_length:
                    point_last = point_last.next
                    count += 1
                # print(point_last)
                temp = self.remove(p1.next.getData())
                self.insert_specindex(temp.getData(), point_last.getData())
                p1 = p1.next
                point_last = self.head
                x += 1


            
            
            
            




            






        




        

