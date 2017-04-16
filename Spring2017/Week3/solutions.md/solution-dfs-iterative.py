class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def dfs(bt, val):
    if bt == None:
        return
    stack = [bt]
    while len(stack) > 0:
        cursor = stack.pop()

        # return the first node that matches
        if cursor.val == val:
            return cursor

        if cursor.right:
            stack.append(cursor.right)
        if cursor.left:
            stack.append(cursor.left)

    return


def tests():
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

    # dfs tests (iterative)
    assert(dfs(bt, 3) == n3) # dfs finds a different node first for '3'
    assert(dfs(bt, 7) == n6)
    assert(dfs(bt, 0) == None)

tests()
