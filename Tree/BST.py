class Node:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert_node(root_node, node_value):
    if root_node.data is None:
        root_node.data = node_value
    elif node_value <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = Node(node_value)
        else:
            insert_node(root_node.left_child, node_value)
    else:
        if root_node.right_child is None:
            root_node.right_child = Node(node_value)
        else:
            insert_node(root_node.right_child, node_value)
    return "The node has been inserted"


new_tree = Node(None)
print(insert_node(new_tree, 70))
print(insert_node(new_tree, 60))

