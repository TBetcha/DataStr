class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

# dfs
def pre_order(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order(root_node.left_child)
    pre_order(root_node.right_child)

#dfs
def in_order(root_node):
    if not root_node:
        return
    in_order(root_node.left_child)
    print(root_node.data)
    in_order(root_node.right_child)


new_tree = TreeNode('Drinks')
left_child = TreeNode("Hot")
right_child = TreeNode("Cold")
new_tree.left_child = left_child
new_tree.right_child = right_child
pre_order(new_tree)
in_order(new_tree)