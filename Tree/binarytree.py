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


# dfs
def in_order(root_node):
    if not root_node:
        return
    in_order(root_node.left_child)
    print(root_node.data)
    in_order(root_node.right_child)


def post_order(root_node):
    if not root_node:
        return
    post_order(root_node.left_child)
    pre_order(root_node.right_child)
    print(root_node.data)




new_tree = TreeNode('Drinks')
left_child = TreeNode("Hot")
right_child = TreeNode("Cold")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
left_child.left_child = tea
left_child.right_child = coffee
new_tree.left_child = left_child
new_tree.right_child = right_child
# pre_order(new_tree)
# in_order(new_tree)
# post_order(new_tree)
# level_order(new_tree)
