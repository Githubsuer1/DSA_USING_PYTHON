class Node:
    def __init__(self,left=None,item=None,right=None):
        self.left = left
        self.item = item 
        self.right = right
class BST:
    def __init__(self):
        self.root = None
    def insert(self,data):
        self.root = self.reInsert(self.root,data)
    def reInsert(self,temp,data):
        if temp is None:
            return Node(None,data,None)
        if data<temp.item:
            temp.left = self.reInsert(temp.left,data)
        elif data>temp.item:
            temp.right = self.reInsert(temp.right,data)
        return temp

    def search(self,data):
        return self.reSearch(self.root,data)
    def reSearch(self,temp,data):
        if temp is None or temp.item == data:
            return root 
        if data < temp.item:
            return self.reSearch(temp.left,data)
        else:
            return self.reSearch(temp.right,data)

    def inOrder(self):
        result = []
        self.rinOrder(self.root,result)
        return result
    def rinOrder(self,temp,result):
        if temp:
            self.rinOrder(temp.left,result)
            result.append(temp.item)
            self.rinOrder(temp.right,result)

    def preOrder(self):
        result = []
        self.rpreOrder(self.root,result)
        return result
    def rpreOrder(self,temp,result):
        if temp:
            result.append(temp.item)
            self.rpreOrder(temp.left,result)
            self.rpreOrder(temp.right,result)

    def postOrder(self):
        result = []
        self.rpostOrder(self.root,result)
        return result
    def rpostOrder(self,temp,result):
        if temp:
            self.rpostOrder(temp.left,result)
            self.rpostOrder(temp.right,result)
            result.append(temp.item)

    def min_value(self):
        current = self.root
        while current.left is not None:
            current = current.left 
        return current.item 

    def max_value(self):
        current = self.root
        while current.right is not None:
            current = current.right 
        return current.item 

        
bst = BST()
bst.insert(200)
bst.insert(100)
bst.insert(300)
bst.insert(150)
bst.insert(250)
bst.insert(50)
bst.insert(350)
print('tree in preOrder',bst.inOrder())
print('tree in postOrder',bst.postOrder())
print('tree in inOrder',bst.preOrder())
print('max item is',bst.max_value())
print('min item is',bst.min_value())