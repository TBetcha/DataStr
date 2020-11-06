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


def search(root_node, node_value):
    if root_node.data == node_value:
        print('The value was found')
    elif node_value < root_node.data:
        if root_node.left_child.data == node_value:
            print("the value is found")
        else:
            search(root_node.left_child, node_value)
    else:
        if root_node.right_child.data == node_value:
            print('the value is found')
        else: return search(root_node.right_child, node_value)


# delete has three cases one child, two child, leaf
# leaf - just remove it
# has oen child - remove it and assign it's child to the deleted's parent
# has two child - find successor and switch it, then delete it
# successor will always be min value in right subtree
def min_val(node):
    current = node
    while(current.left_child is not None):
        current = current.left_child
    return current


def del_node(root_node, node_value):
    if root_node is None:
        return root_node
    #find the node and has no children
    if node_value < root_node.data:
        root_node.left_child = del_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child= del_node(root_node.right_child, node_value)
    else:
        # if node has one child
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None
            return temp
        if root_node.right_child is None:
            temp = root_node.left_child
            root_node = None
            return temp
        #if node has two children swap w/ successor then delete successor
        temp = min_val(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child  = del_node(root_node.right_child, temp.data)
    return root_node


new_tree = Node(None)
print(insert_node(new_tree, 70))
print(insert_node(new_tree, 60))
print(insert_node(new_tree, 90))
print(insert_node(new_tree, 20))
print(insert_node(new_tree, 80))
print(insert_node(new_tree, 10))
print(insert_node(new_tree, 50))
print(post_order(new_tree))
search(new_tree, 60)
del_node(new_tree, 10)
print(in_order(new_tree))









