# Given a binary search tree, reverse the order of its values by modifying the nodes’ links.

def reverse(root):
    if root != None:
        a = reverse(root.left)
        b = reverse(root.right)
    
        root.left = b
        root.right = a
    
    return(root)