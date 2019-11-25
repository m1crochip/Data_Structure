import random
import datetime

def RNGsus(a, b):
    number = random.randint(a, b)
    return number

def bubbleSORT(l, mode):
    start = datetime.datetime.now()
    length = len(l)
    if mode is 'D': # max to min
        for i in range(0,length,+1):
            for j in range(i+1,length,+1):
                if l[j] > l[i]:
                    temp = l[j]
                    l[j] = l[i]
                    l[i] = temp
    else:
        for i in range(0,length,+1):
            for j in range(i+1,length,+1):
                if l[j] < l[i]:
                    temp = l[j]
                    l[j] = l[i]
                    l[i] = temp
    end = datetime.datetime.now()
    duration = end - start
    # print(l)
    print('time spend : ',duration,'<<< BUBBLEsort')

def selectionSORT(l, mode):
    start = datetime.datetime.now()
    length = len(l)
    if mode is 'D': # max to min
        for i in range(0,length,+1):
            indexMIN = i
            for j in range(i+1,length,+1):
                if l[j] > l[i]:
                    indexMIN = j
            temp = l[i]
            l[i] = l[indexMIN]
            l[indexMIN] = temp
    else:
        for i in range(0,length,+1):
            indexMIN = i
            for j in range(i+1,length,+1):
                if l[j] < l[i]:
                    indexMIN = j
            temp = l[i]
            l[i] = l[indexMIN]
            l[indexMIN] = temp
    end = datetime.datetime.now()
    duration = end - start
    # print(l)
    print('time spend : ',duration,'<<< SELECTIONsort')

def insertionSORT(l, mode):
    start = datetime.datetime.now()
    length = len(l)
    if mode is 'D':
        for i in range(1,length,+1):
            temp = l[i]
            j = i
            while j > 0 and l[j-1] < temp:
                l[j] = l[j-1]
                j-=1
            l[j] = temp
    else:
        for i in range(1,length,+1):
            temp = l[i]
            j = i
            while j > 0 and l[j-1] > temp:
                l[j] = l[j-1]
                j-=1
            l[j] = temp
    end = datetime.datetime.now()
    duration = end - start
    # print(l)
    print('time spend : ',duration,'<<< INSERTIONsort')



def shellSORT(l, mode):
    start = datetime.datetime.now()
    length = len(l)
    gap = length//2
    if mode is 'A':
        while gap > 0:
            for i in range(gap, length):
                temp = l[i]
                j = i
                while j >= gap and l[j-gap] > temp:
                    l[j] = l[j-gap]
                    j -= gap
                l[j] = temp
            gap //= 2
    else:
        while gap > 0:
            for i in range(gap, length):
                temp = l[i]
                j = i
                while j >= gap and l[j-gap] < temp:
                    l[j] = l[j-gap]
                    j -= gap
                l[j] = temp
            gap //= 2
    end = datetime.datetime.now()
    duration = end - start
    # print(l)
    print('time spend : ',duration,'<<< SHELLsort')


def runMERGEsort(l):
    start = datetime.datetime.now()
    mergeSort(l)
    end = datetime.datetime.now()
    duration = end - start
    # print(l)
    print('time spend : ',duration,'<<< MERGEsort')


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def quickSORT(lst, low, high):
    if low < high:
        pIdx = partition(lst, low, high)
        quickSORT(lst, low, pIdx)
    # print(lst)

def runQUICKsort(l):
    start = datetime.datetime.now()

    quickSORT(l,0,len(l)-1)

    end = datetime.datetime.now()
    duration = end - start
    # print(l)
    print('time spend : ',duration,'<<< QUICKsort')

def partition(lst, low, high):
    i = low - 1
    pivot = lst[high]
    for j in range(high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i


def NEWquickSort(array, Mode):
    """Sort the array by using quicksort."""
    global count
    # pIdx = 0 if Mode == Con.Low else (
    #     len(array)-1) if Mode == Con.High else (len(array)-1)//2 if Mode == Con.Mid else 0
    if Mode is 'FIRST':
        pivotINDEX = 0
    elif Mode is 'END':
        pivotINDEX = len(array)-1
    elif Mode is 'MID':
        pivotINDEX = (len(array)-1)//2
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[pivotINDEX]
        for x in array:
            if x < pivot:
                count += 1
                less.append(x)
            elif x == pivot:
                count += 1
                equal.append(x)
            elif x > pivot:
                count += 1
                greater.append(x)
        return NEWquickSort(less, Mode)+equal+NEWquickSort(greater, Mode)
    else:
        return array
            

l = []
# RNG
# for i in range(0,1000000):
#     l.append(RNGsus(1,101))
# for i in range(100,0,-1):
#     l.append(i)


l = [193,362,534,402,0,0,0,0,0]
# l = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
# l = [10,99,85,12,36,47,97,35,62,44,33,11,63,13,18,29]
# l = [5]


print(l)
mode = 'A'
print()
# bubbleSORT(l,mode)
# selectionSORT(l,mode)
# insertionSORT(l, mode)
# shellSORT(l, mode)
# runMERGEsort(l)
# runQUICKsort(l)
count=0
FIRST = NEWquickSort(l,'FIRST') 
print(FIRST,'>>> FIRST count :',count)
count=0
END = NEWquickSort(l,'END')
print(END, '>>> END count :',count)
count=0
MID = NEWquickSort(l,'MID')
print(MID,'>>> MID count :',count)






















