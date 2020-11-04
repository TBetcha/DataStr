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



def pre_order(root_node):
    if not root_node:
        return 
    print(root_node.data)
    pre_order(root_node.left_child)
    pre_order(root_node.right_child)


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
    post_order(root_node.right_child)
    print(root_node.data)

new_tree = Node(None)
print(insert_node(new_tree, 70))
print(insert_node(new_tree, 60))
print(insert_node(new_tree, 90))
print(insert_node(new_tree, 20))
print(insert_node(new_tree, 80))
print(insert_node(new_tree, 10))
print(insert_node(new_tree, 50))
print(post_order(new_tree))
