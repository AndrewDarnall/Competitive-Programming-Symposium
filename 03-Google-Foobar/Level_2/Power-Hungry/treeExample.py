# Example of a Tree data structure
class TreeNode:
    def __init__(self):
        self.value = None
        self.rightChild = None
        self.leftChild = None

    def isEmpty(self):
        if self.value == None:
            return True
        else:
            return False
        

class BST:
    def __init__(self):
        self.root = TreeNode()

    def addNode(self, key):
        trace = None
        current = self.root
        newNode = TreeNode()
        newNode.value = key
        if self.root.isEmpty():
            self.root.value = key
        else:
            while current != None:
                trace = current
                if key < current.value:
                    current = current.leftChild
                elif key >= current.value:
                    current = current.rightChild
            if key < trace.value:
                trace.leftChild = newNode
            else:
                trace.rightChild = newNode

    def preOrder(self, p):
        if p != None:
            print(p.value)
            self.preOrder(p.leftChild)
            self.preOrder(p.rightChild)

    def inOrder(self, p):
        if p != None:
            self.inOrder(p.leftChild)
            print(p.value)
            self.inOrder(p.rightChild)
    
    def postOrder(self, p):
        if p != None:
            self.postOrder(p.leftChild)
            self.postOrder(p.rightChild)
            print(p.value)


inputs = [25,10,30,5,15,26,35]
bst = BST()
for i in range(len(inputs)):
    bst.addNode(inputs[i])
print("preOrder tree walk:")
bst.preOrder(bst.root)
print("inOrder tree walk:")
bst.inOrder(bst.root)
print("postOrder tree walk:")
bst.postOrder(bst.root)