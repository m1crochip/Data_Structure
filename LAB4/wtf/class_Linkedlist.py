from class_Node import Node
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
        p = Node(data)
        # if self.head == None:
        #     self.head = p
        # else:
        #     t = self.head
        #     while t.next != None:
        #         t = t.next
        #     t.next = p
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
           
        


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

    # def remove(self, data):
    #     if self.isIn(data):   
    #         select = None
    #         pointer = self.head
    #         b4point = None
    #         aftpoint = None
    #         while pointer.data != data:
    #             check = pointer
    #             b4point = pointer
    #             pointer = pointer.next
    #             aftpoint = pointer.next
    #         b4point.setNext(aftpoint)
    #     else:
    #         print("Data isn't in Linkedlist")

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

    # def __str__(self):
    #     p = self.head
    #     str = ''
    #     if self.head == None:
    #         str = ''
    #     else:
    #         while p.next != None:
    #             str += p.data + ' '
    #             p = p.next
    #     return str

    def __str__(self):
        temp = self.head
        str = ''
        while temp.next != None:
            str += temp.data + ' '
            temp = temp.next
        return str
        
    def headtotail(self):
        # head = self.removeHead()
        # tail = self.getTail()
        # head.setNext()
        # tail.setNext(head)
        head = self.removeHead()
        print(head)

    def tailtohead(self):
        tail = self.removeTail()
        self.addHead(tail)

    def riff(self, length):
        pointer = self.head


    