class Trie:
    ROOT = "#"
    EOW = "*"

    def __init__(self, words=None):
        self.root = TrieNode(self.ROOT)
        if words:
            for word in words:
                self.add_word(word)

    def add_word(self, word):
        word += self.EOW
        nodes = self.root.children

        for char in word:
            if char not in nodes:
                char_node = TrieNode(char)
                nodes[char] = char_node
                nodes = char_node.children
            else:
                nodes = nodes[char].children

    def is_in_trie(self, word):
        nodes = self.root.children

        for char in word:
            if char not in nodes:
                return False
            else:
                nodes = nodes[char].children

        return True


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}

    def __hash__(self):
        return ord(self.char)

    def __eq__(self, other):
        return self.char == other.char

    def __repr__(self):
        return self.char


class WordNotFoundInTrie(Exception):
    def __init__(self, msg):
        super.__init__(msg)
