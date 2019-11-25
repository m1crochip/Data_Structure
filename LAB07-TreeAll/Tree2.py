class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        # self.parent = None
        self.height = 1
    def __str__(self):
        return str(self.data)


def getHeight(root):
    if root:
        return root.height
    else:
        return False

def addNode(root, data):
    if root: 
        if data <= root.data:
            root.left = addNode(root.left, data)
            root.left.parent = root
        elif data > root.data:
            root.right = addNode(root.right, data)
            root.right.parent = root
            
    else:
        return Node(data)

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)

    if balance > 1 and data < root.left.data and root.left:
        return rightRotate(root)
    
    if balance < -1 and data > root.right.data and root.right:
        return leftRotate(root)
    
    if balance > 1 and data > root.left.data and root.left:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    
    if balance < -1 and data < root.right.data and root.right:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def leftRotate(root):
    swap = root.right
    swapchild = swap.left
    swap.left = root
    root.right = swapchild
    root.height = 1 +  max(getHeight(root.left), getHeight(root.right))
    swap.height = 1 +  max(getHeight(swap.left), getHeight(swap.right))
    return swap

def rightRotate(root):
    swap = root.left
    swapchild = swap.right
    swap.right = root
    root.left = swapchild
    root.height = 1 +  max(getHeight(root.left), getHeight(root.right))
    swap.height = 1 +  max(getHeight(swap.left), getHeight(swap.right))
    return swap

def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left) - getHeight(root.right)


def findNode(root, data):
    if root:
        if data == root.data:
            return True
        else:
            if data < root.data:
                return findNode(root.left, data)
            else:
                return findNode(root.right, data)
    else:
        return False


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
    root = addNode(root, element)


inOrder(root)
print(' ')
print('_|_|_|_|_|_|_|_|_|_|_')
printSideway(root)


# print('_|_|_|_|_|_|_|_|_|_|_')
# printSideway(root)
