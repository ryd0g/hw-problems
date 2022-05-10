# Let’s say a binary tree is "super balanced" if the difference 
# between the depths of all pairs of leaf nodes is at most one. 
# Write a function to check if a binary tree is "super balanced".

class Solution(object):
    def isBalanced(self, root):
            
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1