Implement DFS iteratively rather than recursively.

## Ideas

DFS can be done recursively by just calling the function again on a
node's children, until you find what you're looking for. To do
iteratively, just use a stack to process the nodes to explore.

Runtime `O(nodes)` - visit each node at least once
Space `O(height)` - at most we're storing # nodes proportional to
                    the height of one path down the tree from the root

## Code

[Python](./solution-dfs-iterative.py)
