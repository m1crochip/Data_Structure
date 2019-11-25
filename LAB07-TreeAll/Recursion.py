def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* factorial(n-1)


def findMIN(l, start, end):
    if start == end:
        return l[start]
    else:
        MIN = findMIN(l, start+1, end)
        if l[start] < MIN:
            return l[start]
        else:
            return MIN

def sumlist1toN(l,n):
    if n == 0:
        return 0
    elif n == 1:
        return l[0]
    else:
        return l[n-1] + sumlist1toN(l,n-1)

def sumNtoM(l,n,m):
    if n > m:
        return 0
    elif n == m:
        return l[n]
    else:
        return l[n] + sumNtoM(l,n+1,m)


def printNto1(n):
    if n == 0:
        return 0
    elif n == 1:
        return str(n)
    else:
        return str(n) + str(printNto1(n-1))

def print1toN(n):
    if n == 0:
        return 0
    elif n == 1:
        return str(n)
    else:
        return str(print1toN(n-1)) + str(n)

# print(factorial(5))
# print(findMIN(l,0,len(l)-1))
# print(sumlist1toN(l,2))
# l = [1,2,3,4,5]
# print(sumNtoM(l,0,4))
# print(printNto1(3))
# print(print1toN(3))



# search x in list
def BNS(l, data, n):
    if l[n] == data:
        return n
    else:
        # if l[n] > data:
        #     return BNS(l, data, n-1)
        # else:
        #     return BNS(l, data, n+1)
        if data > l[n]:
            return BNS(l, data, n+1)
        else:
            return BNS(l, data, n-1)
# l = [1,2,3,4,5,6,7,8,9]
# print(BNS(l,4,len(l)-1))



# tower of Hanoi
    # can move only ONE disk per round
    # upper only can move
    # No disk may placed on top if it be smaller disk

                    #start    stop     middle
def TowerOfHanoi(n, fromthis, tothis, tonextto):
    if n == 1:
        print('Move disk 1 from',fromthis,' to ', tothis) # A > C
        return
    TowerOfHanoi(n-1, fromthis, tonextto, tothis) # A > B
    print('Move disk',n,' from ', fromthis, ' to ', tothis)
    TowerOfHanoi(n-1, tonextto, tothis, fromthis) # C > B

# n = 4
# TowerOfHanoi(4, 'A', 'C', 'B')


def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)

def sumN(l, n):
    if n == 0:
        return 0
    elif n == 1:
        return l[0]
    else:
        return l[n-1]+sumN(l,n-1)

def sumItoJ(l, i, j):
    if i > j:
        return 0
    elif i == j:
        return l[i]
    else:
        return l[i] + sumItoJ(l, i+1, j)
    
a = [1,2,3,4,5]
print(sumItoJ(a, 0, 4))







