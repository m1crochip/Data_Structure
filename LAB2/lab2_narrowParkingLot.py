class Stack:

    def __init__(self, list = None):
        if list == None:
            self.item = []
        else:
            self.item = list

    def __init__(self):
        self.item = []
    
    def push(self, i):
        self.item.append(i)

    def size(self):
        return len(self.item)

    def space_left(self):
        return 4-len(self.item)

    def isEmpty(self):
        if self.item == []:
            return True
        else:
            return False
    
    def pop(self):
        self.item.pop()

    def peek(self):
        return self.item[len(self.item)-1]

    def isFull(self):
        if len(self.item) < 4:
            return False
        else: return True

    def arrive(self, x):
        if self.isFull() == False:
            self.push(x)
            print(self.item,end=" ")
            print("arrive ",end="")
            print("     Space Left",end="")
            print(self.space_left())
        else:
            print(x,end=" ")
            print(" cannot arrive :",end=" ")
            print("SOI FULL")

    def depart(self, y):
        if y in self.item:
            index = self.item.index(y)
            #print(index)
            B = Stack()
            count = self.size()-1
            while count > index:
                B.push(self.item[count])
                count-=1
            lenB = B.size()
            for i in range(0, B.size()+1):
                self.pop()
                #print('A : ',end="")
                #print(self.item)
            for i in range(0, lenB):
                self.push(B.item[i])
            for i in range(0, lenB):
                B.pop()
            #print('A : ',end="")
            #print(self.item)
            #print(self.space_left())
            #print('B : ',end="")
            #print(B.item)

        else:
            print(y,end=" ")
            print(" cannot depart :",end=" ")
            print("NO ",end="")
            print(y)
       #check = True
       # for i in range(0,self.size()):
       #     if y != self.item[i]:
       #         check = False
       #     else:
       #         check = True
       # if check == False:
       #     print(y,end=" ")
       #     print(" cannot depart :",end=" ")
       #     print("NO ",end="")
       #     print(y)

A = Stack()

A.arrive('car1')
A.arrive('car2')
A.arrive('car3')
A.arrive('car4')
A.arrive('car5')

print("SOI",A.item)
A.depart('car7')
A.depart('car2')
print("Space Left : ",end="")
print(A.space_left())
print("SOI",A.item)
#while TRUE:
    

##### limit of A = 4 car

# print(A.isEmpty())
# print(A.size())
# print(A.isFull())

# A.remove(3)
# print(A.item[1])
# print(B.isEmpty())
# print(A.size())
# print(A.isFull())

## CAR 2 DEPART
 ## A = ก
 ## B = ข

#target = 2 # <<< car2 is target for depart

#print(A.item)
#print(B.item)

#if B.isEmpty() == True:
#    for i in range(target, A.size()):
#        B.push(A.item[i])
#        print('A : ',end="")
#        print(A.item)
#        print('B : ',end="")
#        print(B.item)
#    for i in range(-1, B.size()):
#        A.pop()
#    for i in range(0, B.size()):
#        A.push(B.item[i])
#    for i in range(0 , B.size()):
#        B.pop()
#else:
#    print('SOI FULL')
#print(A.item)
#print(B.item)