class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = None if left else left 
        self.right = None if right else right
        self.parent = None if parent else parent
        self.height = 1

    def __str__(self):
        return str(self.data)

def insert(root, data):
    if root:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    else:
        return Node(data)

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)

    if balance >1 and data < root.left.data and root.left:
        return RightRotate(root)

    if balance <-1 and data > root.right.data and root.right:
        return LeftRotate(root)

    if balance > 1 and data > root.left.data and root.left:
        root.left = LeftRotate(root.left)
        return RightRotate(root)

    if balance < -1 and data < root.right.data and root.right:
        root.right = RightRotate(root.right)
        return LeftRotate(root)

    return root

def RightRotate(root):
    swap = root.left
    swapchild = swap.right
    swap.right = root
    root.left = swapchild
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    swap.height = 1 + max(getHeight(swap.left), getHeight(swap.right))
    return swap

def LeftRotate(root):
    swap = root.right
    swapchild = swap.left
    swap.left = root
    root.right = swapchild
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    swap.height = 1 + max(getHeight(swap.left), getHeight(swap.right))
    return swap

def getHeight(root):
    if root:
        return root.height
    else:
        return False

def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left)-getHeight(root.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data,end=' ')
        inOrder(root.right)

def printSideway(root):
    _printSideway(root, 0)
    print()

def _printSideway(root, lv):
    if root:
        _printSideway(root.right, lv+1)
        print('  '*lv, root.data, sep='')
        _printSideway(root.left, lv+1)


l = [14,4,9,7,15,3,18,16,20,5,16 ]
root = None
for element in l:
    root = insert(root, element)


inOrder(root)
print(' ')
print('_|_|_|_|_|_|_|_|_|_|_')
printSideway(root)