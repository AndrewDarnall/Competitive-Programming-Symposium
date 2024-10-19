# N-ary tree solution
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
        print("Node -- [{}]".format(input))
        for i in range(len(input)):
            prod *= input[i]
        newNode.prod = prod
        if node == self.root:
            self.max = newNode.prod
        # print("{} > {}".format(newNode.prod, self.max))    
        if newNode.prod > self.max:
            self.max = newNode.prod
        node.child = newNode
        for j in range(len(input)):
            # print("Iterating on:\t{}".format(input[:j] + input[j + 1:]))
            self.buildTree(input[:j] + input[j + 1:], newNode)

    def printTree(self, node):
        print(node.prod)
        for i in range(len(node.children)):
            self.printTree(node.children[i])

    def printMax(self):
        print(self.max)

    def getMax(self):
        return self.max

# tree = Tree()
# tree.buildTree([2, -3, 1, 0, -5], tree.root)
# tree.printMax()
# tree.printTree(tree.root)

def solution(xs):
    tree = Tree()
    tree.buildTree(xs, tree.root)
    return str(tree.getMax())

if __name__ == "__main__":
    print("The solution is:\t{}".format(solution([2,-3, 1, 0, -5])))