# DFS recursive and BFS iterative

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(bt, val):
    if bt == None:
        return
    queue = [bt]
    while len(queue) > 0:
        cursor = queue.pop(0)

        # return the first node that matches
        if cursor.val == val:
            return cursor

        if cursor.left:
            queue.append(cursor.left)
        if cursor.right:
            queue.append(cursor.right)

    return

 def dfs(bt, val):
    if bt == None:
        return
    if bt.val == val:
        return bt

    left = dfsRecursive(bt.left, val)
    if left != None:
        return left

    right = dfsRecursive(bt.right, val)
    if right != None:
        return right

    return
