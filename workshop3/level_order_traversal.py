class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_iterative(arr: list):
    if len(arr) == 0 or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        current = queue.pop(0)

        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1

    return root


def level_order_traversal(root: TreeNode):
    if root is None:
        return []

    queue = [root]
    result = []
    while len(queue) > 0:
        result.append(list(node.val for node in queue))

        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return result


def asserts():
    root = build_tree_iterative([9, 16, 8, None, None, 6, 11])
    assert level_order_traversal(root) == [[9], [16, 8], [6, 11]]

    root = build_tree_iterative([])
    assert level_order_traversal(root) == []

    root = build_tree_iterative([9])
    assert level_order_traversal(root) == [[9]]


asserts()
