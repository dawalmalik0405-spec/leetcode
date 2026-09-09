
def max_depth(tree):

  if not tree:
    return 0
  

  left_depth  = max_depth(tree.left)
  right_depth = max_depth(tree.right)

  depth = 1 + max(left_depth, right_depth)

  return depth