class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
        self.parent = None if parent is None else parent
    
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

def find(root, data):
    if root.data == data:
        return True
    else:
        if data < root.data and root.left:
            return find(root.left, data)
        elif data > root.data and root.right:
            return find(root.right, data)
        else:
            return False

def path(root, data, P=[]):
    if root.data == data:
        P.append(data)
    else:
        if data < root.data and root.left:
            P.append(root.data)
            path(root.left, data, P)
        elif data > root.data and root.right:
            P.append(root.data)
            path(root.right, data,P)
    return P

def depth(root, data, dep=[]):
    if root.data == data:
        pass
    else:
        if data < root.data and root.left:
            dep.append(root.data)
            depth(root.left, data, dep)
        elif data > root.data and root.right:
            dep.append(root.data)
            depth(root.right, data, dep) 
    return len(dep)

def ISP(root, parent):
    if root.left: # root.left:
        # print(root.data)
        return ISP(root.left, root)
    else:
        temp = root.data
        # print(temp,'<<TEMP')
        delete(parent, root.data)
        return temp

def delete(root, data, parent=None):
    if root:
        if data > root.data:
            delete(root.right, data, root)
        else:
            delete(root.left, data, root)

        if root.data is data:
            #No children
            if root.left is None and root.right is None:
                if parent:
                    if parent.right is root:
                        parent.right = None
                    else:
                        parent.left = None
                else:
                    root.data = None
            #has 2 children
            elif root.left and root.right:
                root.data = ISP(root.right, root)
            # has 1 child
            else:
                lower = root.right if root.right else root.left
                if parent:
                    if parent.right is root:
                        parent.right = lower
                    else:
                        parent.left = lower
                else:
                    root = lower

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

def printTree(root):
        _printTree(root, 0)
        print()

def _printTree(root, level):
    if root is not None:
        _printTree(root.right, level+1)
        print('  '*level, root.data, sep='')
        _printTree(root.left, level+1)

def inOrder(root, l=[]):
    if root.left:
        inOrder(root.left, l)
    l.append(root.data)
    if root.right:
        inOrder(root.right, l)
    return l


# def parent(root, data, parent=None):
#     if root:
#         if root.data == data:
#             parent = root.parent
#         else:
#             if data < root.data:
#                 parent(root.left, data, parent)
#             else:
#                 parent(root.right, data, parent)
            
            
    
    


l = [14,4,9,7,15,3,18,16,20,5,16]
# l = [14]
x = None # Empty root
for ele in l:
    x = insert(x,ele)




print('input : ',l)
print('inorder : ', inOrder(x,[]))
print('printSideway')
printTree(x)
print('height of 14 : ', height(x))
print('path 5 : ', path(x, 5,[]))
# print('father of 14 : ', parent(x, 4))
# print(x,x.left.right.parent)
print('depth of node data 18 : ',depth(x, 18, []))

# print(path(x, 20, []))
# print(height(x))
# print('depth of 18 is :',depth(x,18))
# delete(x, 15)
# print('--- deleted --')
# printTree(x)

























