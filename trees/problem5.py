# Given a binary tree, check whether it is a valid binary search tree (values in order).

def isValidBST(root):
    return check_bst(root, float("-inf"), float("inf"))
	
def check_bst(node, left, right):
    if not node:
        return True

    if not left < node.val < right:
        return False

    return (check_bst(node.left, left, node.val)
            and check_bst(node.right, node.val, right))