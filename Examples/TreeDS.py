class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# node0 = TreeNode(3)

# root = node0
# root.left = TreeNode(4)
# root.right = TreeNode(5)

# print(root.right.key)

root = TreeNode(2)

root.left = TreeNode(3)
root.right = TreeNode(5)

#   2 
# 3   5

#  Tree DS Left, Right, Root

left_sub_tree = root.left
left_sub_tree.left = TreeNode(1)

#    2
#  3   5
#1   0

right_sub_tree = root.right
right_sub_tree.left = TreeNode(3)
right_sub_tree.right = TreeNode(7)

#    2
#  3   5
#1    3 7

# 2nd Level Sub Tree from Left Root & Right Root

right_leaf_from_left_sub_tree = right_sub_tree.left
right_leaf_from_left_sub_tree.right = TreeNode(4)

left_leaf_from_right_sub_tree = right_sub_tree.right
left_leaf_from_right_sub_tree.left = TreeNode(6)
left_leaf_from_right_sub_tree.right = TreeNode(8)


#    2
#  3   5
#1    3 7
#      46 8


print(root.right.right.key)