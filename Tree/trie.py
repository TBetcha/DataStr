'''
Typically used to store or search strings in a space and time efficient way

Any node in trie can store non repetitive multiple characters

every node stores link of the next character of the string

every node keeps track of the 'end of string'


'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_string = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_string(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.end_string = True
        print("Successfully inserted")

    def search_str(self, word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node

        if current.end_string == True:
            return True
        else:
            return False


def delete_str(root, word, index):
    ch = word[index]
    current_node = root.children.get(ch)
    can_be_deleted = False

    # case 1 call recursively
    if len(current_node.children) > 1:
        delete_str(current_node, word, index+1)
        return False

    # case 2 str is prefix of another, change end of str to false
    if index == len(word) - 1:
        if len(current_node.children) >= 1:
            current_node.end_string = False
            return False
        # if there is no other node, delete it
        else:
            root.children.pop(ch)
            return True

    # third case other word is prefix
    if current_node.end_string == True:
        delete_str(current_node, word, index+1)
        return False

    can_be_deleted = delete_str(current_node, word, index+1)
    if can_be_deleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


'''
Deleteion 

3 cases:

Common prefix: 
    Check for inclusion
    find leaf node
        delete leaf
        move up to the highest noncommon node

String is prefix of other string:
    other will string be impacted so relocate leaf
        Go down from root until end of string:
            delete end of string char keeping other string intact


Other string is prefix of this string:
    start at leaf node:
        delete left and move end up end of string until the desired string is removed
        
No nodes depend on it:
    delete going up until string is removed:
        if parent has more than one letter remove letter desired

'''


trie_one = Trie()
trie_one.insert_string('App')
trie_one.insert_string("Appl")
delete_str(trie_one.root, "App", 0)
print(trie_one.search_str('App'))
