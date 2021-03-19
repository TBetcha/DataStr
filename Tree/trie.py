'''
Typically used to store or search strings in a space and time efficient way

Any node in trie can store non repetitive multiple characters

every node stores link of the next character of the string

every node keeps track of the 'end of string'

'''


class Trie_node:
    def __init__(self):
        self.children = {}
        self.end_string = False


class Trie:
    def __init(self):
        self.root = Trie_node()


trie_one = Trie()
