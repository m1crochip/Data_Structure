class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
        self.parent = None if parent is None else parent
        self.height = 1
    def __str__(self):
        return str(self.data)
def insert(root, data):
    if not root:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
            root.left.parent = root
        else:
            root.right = insert(root.right, data)
            root.right.parent = root
    return root


def ISP(root, parent):
    if root.left:
        return ISP(root.left, root)
    else:
        temp = root.data
        delete(parent, root.data)
        return temp


def delete(root, data):
    if root:
        if data < root.data:
            delete(root.left, data)
        else:
            delete(root.right, data)

        if root.data is data:
            #no child
            if root.left is None and root.right is None:
                if root.parent:
                    if root.parent.right is root:
                        root.parent.right = None
                    else:
                        root.parent.left = None
                else:
                    root = None

            #2 children
            elif root.left and root.right:
                root.data = ISP(root.right, root)
            
            else:
                lower = root.right if root.right else root.left
                if root.parent:
                    if root.parent.right is root:
                        root.parent.right = lower
                    else:
                        root.parent.left = lower
                else:
                    root = lower

def PATH(root, data, l=None):
    if root.data == data:
        pass
    else:
        # print(root.data,end=' ')
        l.append(root.data)
        if data < root.data:
            PATH(root.left, data, l)
        else:
            PATH(root.right, data, l)
    return l

def height(root):
    if root:
        hl = height(root.left)
        hr = height(root.right)
        if hl>hr:
            return hl+1
        else:
            return hr+1
    else:
        return -1

def printSideway(root):
    _printSideway(root, 0)
    print()
  
def _printSideway(root, lv):
    if root:
        _printSideway(root.right, lv+1)
        print('  '*lv, root.data,sep='')
        _printSideway(root.left, lv+1)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data,end=' ')
        inOrder(root.right)
   


l = [14,4,9,7,15,3,18,16,20,5]
root = None
for element in l:
    root = insert(root, element)


inOrder(root)
print(' ')
printSideway(root)
print(PATH(root, 5, []))
print(height(root))
# print(root.left.parent)
# print('find node 3',findNode(root,3))
# print('find path of node 3 : ',end='')
# PATH(root, 3)

# print('parent of 16 : ',findParentofNode(root, 16))


# delete(root, 9)
# print('--------------------------')
# printSideway(root)















