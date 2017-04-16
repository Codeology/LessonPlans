# return true if the two binary trees are equal
# return false otherwise
def sameTree(bt1, bt2):
    if bt1 == None and bt2 == None:
        return True
    if bt1 == None and bt2 != None:
        return False
    if bt1 != None and bt2 == None:
        return False

    if bt1.val != bt2.val:
        return False

    return sameTree(bt1.left, bt2.left) and sameTree(bt1.right, bt2.right)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# helper to create a test tree
def testTree():
    bt = TreeNode(1)
    bt = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n3 = TreeNode(3)
    n4 = TreeNode(5)
    n5 = TreeNode(6)
    n6 = TreeNode(7)

    #     1
    #    / \
    #   2   3
    #  / \ / \
    # 3  5 6  7
    bt.left = n1
    bt.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6   

    return bt

def tests():
    # setup
    bt1 = testTree()
    bt2 = testTree()
    bt3 = testTree()
    bt3.left.left = None

    # tests
    assert(sameTree(bt1, bt2))
    assert(sameTree(bt1, bt3) == False)

tests()
