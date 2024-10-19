class TreeNode:
    def __init__(self):
        self.values = None
        self.prod = None
        self.children = []

class Tree:
    def __init__(self):
        self.root = TreeNode()
        self.max = None

    def buildTree(self, input, node):
        newNode = TreeNode()
        newNode.values = input
        prod = 1
        for i in range(len(input)):
            prod *= input[i]
        newNode.prod = prod
        if node == self.root:
            self.max = newNode.prod  
        if newNode.prod > self.max:
            self.max = newNode.prod
        node.child = newNode
        for j in range(len(input)):
            self.buildTree(input[:j] + input[j + 1:], newNode)

    def getMax(self):
        return self.max
    
def solution(xs):
    tree = Tree()
    tree.buildTree(xs, tree.root)
    return str(tree.getMax())