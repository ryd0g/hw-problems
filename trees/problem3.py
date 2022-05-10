# Given a binary tree containing numbers, find the maximum sum path 
# (the path that has the largest sum of node values). The path may start and end at any node in the tree.

def maxPathSum( root):
    def maxsums(node):
        if not node:
            return [-2**31] * 2
        left = maxsums(node.left)
        right = maxsums(node.right)
        return [node.val + max(left[0], right[0], 0),
                max(left + right + [node.val + left[0] + right[0]])]
    return max(maxsums(root))