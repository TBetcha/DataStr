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


trie_one = Trie()
trie_one.insert_string('App')
trie_one.insert_string("Appl")