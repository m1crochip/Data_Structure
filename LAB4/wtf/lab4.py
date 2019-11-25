from class_Linkedlist import LinkedList
from class_Node import Node


def howmuchichoose(size, percent):
    return (percent*size)/100
def show(List):
    if len(List) == 0:
        print("List empty")
    else:
        for i in range(0,len(List)):
            print(List[i],end='')
            print(" ",end='')
        print('')

def bottomUp(percent, LinkedList):
    print("BottomUp Activated!!!")
    percent = percent
    length = int(howmuchichoose(LinkedList.size(), percent))
    print(length)
    for i in range(0,length):
        LinkedList.headtotail()
    print("Now : ",end='')
    print(LinkedList)

def riffle(percent, LL):
    print("Riffle Activated!!!")
    percent = percent
    length = int(howmuchichoose(LL.size(), percent))
    print(length)
    LL.riff(length)
    print("Now : ",end='')
    print(LL)

def deRiffle(percent, LL):
   print("De-Riffle Activated!!!")
   percent = 100-percent
   length = int(howmuchichoose(LL.size(), percent))
   print(length)
   print("Now : ",end='')
   print(LL)

def deBottomUp(percent, LL):
    print("De-BottomUp Activated!!!")
    percent = percent
    length = int(howmuchichoose(LL.size(), percent))
    for i in range(0,length):
        LL.tailtohead()
    print("Now : ",end='')
    print(LL)


LL = LinkedList()
i = 1
while i <= 10:
    LL.append(str(i))
    i += 1

# print("In : ",end='')
print(LL)
print(LL.size())

# bottomUp(30,LL)
# riffle(50,LL)
# # deRiffle(60,LL)
# # deBottomUp(30,LL)
