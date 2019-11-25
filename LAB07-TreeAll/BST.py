from Node import Node

class BST:
    def __init__(self, root=None):
        self.root = None if root is None else root

    def addI(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            fp = None
            p  = self.root
            while p is not None:
                fp = p
                p = p.left if data < p.data else p.right
                # if data < p.data:
                #   p = p.left
                # else:
                #   p = p.right
            if data < fp.data:
                fp.left = Node(data)
            else:
                fp.right = Node(data)
        # print(self.root)
    
    def add(self, data):
        self.root = BST._add(self.root, data)
    
    def _add(root, data): # recursive _add
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left, data)
            else:
                root.right = BST._add(root.right, data)
        # print(root.left,root.right)
        return root
    
    def inOrder(self):
        BST._inOrder(self.root)
        print()
    
    def _inOrder(root):
        if root: # if root is not None
            BST._inOrder(root.left)
            print(root.data, end=' ')
            BST._inOrder(root.right)

    def preOrder(self):
        BST._preOrder(self.root)
        print()
    
    def _preOrder(root):
        if root:
            print(root.data, end=' ')
            BST._preOrder(root.left)
            BST._preOrder(root.right)

    def postOrder(self):
        BST._postOrder(self.root)
        print()
    
    def _postOrder(root):
        if root:
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root.data, end=' ')

    def search(root, data):
        if root is None or root.data is data:
            return root
        if root.data < data:
            return BST.search(root.right, data)
        return BST.search(root.left, data)

    def printSideway(self):
        BST._printSideway(self.root, 0)
        print()

    def _printSideway(root, level):
        if root:
            # print(' ',root)
            # print(root.left,' ',root.right)
            BST._printSideway(root.right, level+1)
            print('  '*level , root.data, sep='')
            BST._printSideway(root.left, level+1)
       
    # def _printSideway(root, level):
    #     if root:
    #         BST._printSideway(root.right, level+1)
    #         print('  '*level, root.data, sep='')
        # BST._printSideway(root.left, level+1)


    

l = [14,4,9,7,15,3,18,16,20,5,16]
r = BST()
for i in l:
    r.addI(i)
print('inOrder : ',end='')
r.inOrder()
print('preOrder : ',end='')
r.preOrder()
print('postOrder : ',end='')
r.postOrder()

r.printSideway()

r.search(4)

