
def isSameTree(t1,t2):


    if not t1 and not t2:
        return True

    if not t1 and t2:
        return False

    if t1 and not t2:
        return False

    if t1.val != t2.val:
      return False

    left = isSameTree(t1.left, t2.left)
    right = isSameTree(t1.right, t2.right)

    return left and right

        
    
    
    

    

