class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
    
    def __str__(self):
        return str(self.data)
    
    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        elif data >= self.data:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True
        else:
            return False
    
    def find(self, data):
        if self.data == data:
            return True
        elif data < self.data and self.left:
            return self.left.find(data)
        elif data > self.data and self.right:
            return self.right.find(data)
        return False
    
    def path(self, data, path):
        if self.data == data:
            path.append(self.data)
        elif data < self.data and self.left:
            path.append(self.data)
            return self.left.path(data,path)
        elif data > self.data and self.right:
            path.append(self.data)
            return self.right.path(data,path)
        return path

    def preOrder(self, l):
        l.append(self.data)
        if self.left:
            self.left.preOrder(l)
        if self.right:
            self.right.preOrder(l)
        return l

    def inOrder(self, l):
        if self.left:
            self.left.inOrder(l)
        l.append(self.data)
        if self.right:
            self.right.inOrder(l)
        return l

    def postOrder(self, l):
        if self.left:
            self.left.postOrder(l)
        if self.right:
            self.right.postOrder(l)
        l.append(self.data)
        return l
    
    def printRoot(self):
        print(self.left, self.data, self.right)
    
    #1 no child 
        # no parent
            # set NONE
        # has parent
            # set parent left and right to our child
    #2 has 2 child
        # no parent = root node
            # find right and left until out
        # has parent


class BST:
    def __init__(self, root=None):
        self.root = None if root is None else root
    
    def insert(self, data):
        if self.root is not None:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    
    def path(self, data):
        if self.path:
            return self.root.path(data,[])
        else:
            return False

    def preOrder(self):
        if self.root:
            return self.root.preOrder([])
        else:
            return []
    
    def inOrder(self):
        if self.root:
            return self.root.inOrder([])
        else:
            return []
    
    def postOrder(self):
        if self.root:
            return self.root.postOrder([])
        else:
            return []
    
    #1 no child 
        # no parent
            # set NONE
        # has parent
            # set parent left and right to our child
    #2 has 2 child
        # no parent = root node
            # find right and left until out
        # has parent
    #3 has only one child 
        
    def ISP(self, root, father):
        if root.left:
            return BST.ISP(self, root.left, root)
        else:
            temp = root.data
            BST._remove(self, father, root.data)
               
            return temp
            

    def remove(self, data):
        BST._remove(self, self.root, data)

    def _remove(self, root, data, father=None):
        if root:
            if data >= root.data:
                BST._remove(self, root.right, data, root)
            else:
                BST._remove(self, root.left, data, root)
            
            if root.data is data:
                #No child
                if root.left is None and root.right is None:
                    if father:
                        if father.right is root:
                            father.right = None
                        else:
                            father.left = None
                    else:
                        self.root = None
                
                # has 2 child
                elif root.left and root.right:
                    root.data = BST.ISP(self, root.right, root)
                
                # one child
                else:
                    lower = root.right if root.right else root.left
                    if father:
                        if father.right is root:
                            father.right = lower
                        else:
                            father.left = lower
                    else:
                        self.root = lower
                                        
    
    def printTree(self):
        BST._printTree(self.root, 0)
        print()

    def _printTree(root, level):
        if root is not None:
            BST._printTree(root.right, level+1)
            print('  '*level, root.data, sep='')
            BST._printTree(root.left, level+1)


l = [14,4,9,7,15,3,18,16,20,5,16]
# l = [14]
x = BST()
for ele in l:
    x.insert(ele)

print("preOrder : ",x.preOrder())
print("inOrder : ",x.inOrder())
print("postOrder : ",x.postOrder())

# for a in l:
#     print(a,' : ',x.path(a))
print('-----TREE-----')
x.printTree()
# x.remove(4)
# print('--------------')
# x.printTree()
# print('delete already')
# print(x.root.left.right)



