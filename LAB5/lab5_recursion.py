# def getFact(n):
#     if n == 0 or n == 1:
#         return 1
#     elif n <2:
#         return 1
#     else:
#         return n*getFact(n-1)

# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n-1)

# def sum_list(n, L):
#     if n is 0:
#         return 0
#     elif n is 1:
#         return L[0]
#     else:
#         return sum_list(n-1,L) + L[n-1]

# def sum_list_tt(l, start, stop):
#     if start > stop:
#         return 0
#     elif start == stop:
#         return l[0]
#     else:
#         return l[start] + sum_list_tt(l, start+1,stop)

# a = []
# for i in range(1,6):
#     a.append(i)
# print(a)
# print(sum_list_tt(a,1,len(a)))



def printSack(sack, maxi):
    global good
    global name
    for i in range(maxi+1):
        print(good[sack[i]], end=' ')
        # print(name[sack[i]],good[sack[i]], end = ' ')
    print()

def pick(sack, i, mLeft, ig):
    global N
    global good
    #pick(sack, 0, 20,0)
    #i = index in sack
    #ig = index of our select 
    if ig < N:  # have something left to pick
        price = good[ig]    # good's price
        if mLeft < price:   # CAN'T BUY ---------------------
            pick(sack, i,mLeft, ig+1)    # try to pick next good 
        else:   # can buy
            mLeft -= price  # pay >> decrease money
            sack[i] = ig    # pick that ig to the sack at i
            if mLeft == 0:  # done
                printSack(sack, i)
            else:   # still have moneyLeft
                pick(sack, i+1, mLeft, ig+1)
            pick(sack, i, mLeft+price, ig+1)    # take the item off the sack for other solutions
    

good = [20,10,5,5,3,2,20,10]
name = ['soap', 'potato chips', 'loly pop', 'toffy', 'pencil', 'rubber', 'milk','cookie']
N = len(good) # number of good

sack = N*[-1]  # empty sack
# print(good)
# print(name)
# print(sack)
mLeft = 20 #money left
i = 0 #scak index
ig = 0 # good index

pick(sack, i, mLeft, ig)
#pick(sack, 0, 20,0)