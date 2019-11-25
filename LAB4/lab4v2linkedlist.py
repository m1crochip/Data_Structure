from Node import Node
from Linkedlist import LinkedList

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
    # print("BottomUp Activated!!!")
    percent = percent
    # print(LinkedList.size())
    length = int(howmuchichoose(LinkedList.size(), percent))
    # print(length)
    for i in range(0,length):
        LinkedList.headtotail()
    # print("Now : ",end='')
    print(LinkedList)

def riffle(percent, LL):
    # print("Riffle Activated!!!")
    percent = percent
    length = int(howmuchichoose(LL.size(), percent))
    # print(length)
    # LL.insert_specindex('X','4')
    LL.riff(length)
    # print("Now : ",end='')
    print(LL)

def deRiffle(percent, LL):
#    print("De-Riffle Activated!!!")
   percent = percent
   length = int(howmuchichoose(LL.size(), percent))
#    print(length)
   LL.driff(length)
#    print("Now : ",end='')
   print(LL)

def deBottomUp(percent, LL):
    # print("De-BottomUp Activated!!!")
    percent = percent
    length = int(howmuchichoose(LL.size(), percent))
    # print(length)
    for i in range(0,length):
        LL.tailtohead()
    # print("Now : ",end='')
    print(LL)

LL = LinkedList()
for i in range(1,11):
    LL.append(str(i))

# print("start ",end='')
# print(LL)

bottomUp(130,LL)
riffle(60,LL)
deRiffle(60,LL)
deBottomUp(130,LL)


