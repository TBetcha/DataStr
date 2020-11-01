import LinearDS
from LinearDS import linkedQueue


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


def level_order(root_node):
    if not root_node:
        return
    else:
        queue = linkedQueue.Queue()
        queue.enqueue(root_node)
        while not (queue.is_empty()):
            root = queue.dequeue()
            print(root.value.data)
            if root.value.left_child is not None:
                queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                queue.enqueue(root.value.right_child)


def search(root_node, node_value):
    if not root_node:
        return "The tree does not exist"
    else:
        queue = linkedQueue.Queue()
        queue.enqueue(root_node)
        while not (queue.is_empty()):
            root = queue.dequeue()
            if root.value.data == node_value:
                return f"{root.value.data} was found"
            if root.value.left_child is not None:
                queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                queue.enqueue(root.value.right_child)
        return "Not found"


def insert(root_node, new_node):
    if not root_node:
        root_node = new_node
    else:
        queue = linkedQueue.Queue()
        queue.enqueue(root_node)
        while not (queue.is_empty()):
            root = queue.dequeue()
            if root.value.left_child is not None:
                queue.enqueue(root.value.left_child)
            else:
                root.value.left_child = new_node
                return "successfully inserted"
            if root.value.right_child is not None:
                queue.enqueue(root.value.right_child)
            else:
                root.value.right_child = new_node
                return "successfully inserted"


def get_deepest(rootNode):
    if not rootNode:
        return
    else:
        cust = linkedQueue.Queue()
        cust.enqueue(rootNode)
        while not (cust.is_empty()):
            root = cust.dequeue()
            if root.value.left_child is not None:
                cust.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                cust.enqueue(root.value.right_child)
        deepest = root.value
        return deepest


def del_deepest(root_node, d_node):
    if not root_node:
        return
    else:
        cust = linkedQueue.Queue()
        cust.enqueue(root_node)
        while not (cust.is_empty()):
            root = cust.dequeue()
            if root.value is d_node:
                root.value = None
            if root.value.right_child:
                if root.value.right_child is d_node:
                    root.value.right_child = None
                    return
                else:
                    cust.enqueue(root.value.right_child)
            if root.value.left_child:
                if root.value.left_child is d_node:
                    root.value.left_child = None
                    return
                else:
                    cust.enqueue(root.value.left_child)


def delete_node(root_node, node):
    if not root_node:
        return "The Binary Tree does not exist"
    else:
        cust = linkedQueue.Queue()
        cust.enqueue(root_node)
        while not (cust.is_empty()):
            root = cust.dequeue()
            if root.value.data == node:
                d_node = get_deepest(root_node)
                root.value.data = d_node.data
                del_deepest(root_node, d_node)
                return "The node has been deleted, y'all!"
            if root.value.left_child is not None:
                cust.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                cust.enqueue(root.value.right_child)
        return "Failed to delete"
    
    
def delete_tree(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The Binary Tree has successfully been deleted"


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
# print(search(new_tree, "Tea"))
new_node = TreeNode("Cola")
insert(new_tree, new_node)
level_order(new_tree)
deepest_node = get_deepest(new_tree)
print('----')
print(deepest_node.data)
newnode = get_deepest(new_tree)
del_deepest(new_tree, newnode)
print('level-----------')
level_order(new_tree)
print('level-----------')
delete_node(new_tree, 'Hot')
print('level-----------')
level_order(new_tree)
delete_tree(new_tree)
level_order(new_tree)