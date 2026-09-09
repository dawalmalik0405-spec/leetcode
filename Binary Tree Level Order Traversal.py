def tree_order_traversal(root):

    if root is None:
        return []

    queue = [root]
    result = []

    while queue:
        current_level = []

        for i in range(len(queue)):

            node = queue.pop(0)
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
                

            if node.right:
                queue.append(node.right)
                

            

        result.append(current_level)

    return result
