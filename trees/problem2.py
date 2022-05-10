# Given a binary search tree containing integers and a target integer, 
# come up with an efficient way to locate two nodes in the tree whose sum is equal to the target value.

def find_nodes(root, new_nodes):
    if root.left:
        find_nodes(root.left)
    if root.right:
        find_nodes(root.right)
    
    new_nodes.add(root.val)

def find_nodes_add(root, target):
    new_nodes = set()
    if not root:
        return None
    find_nodes(root, new_nodes)
    for val in new_nodes:
        if target - val in new_nodes:
            return(val, target - val)
    return None