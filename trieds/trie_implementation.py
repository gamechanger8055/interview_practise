class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in self.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.end_of_word = True

    def search(self, word):
        curr = self.root
        for w in word:
            if w not in self.children:
                return False
            #curr.children[w] = TrieNode()
            curr = curr.children[w]
        return curr.end_of_word

    def startsWith(self,prefix):
        curr = self.root
        for w in prefix:
            if w not in self.children:
                return False
            curr = curr.children[w]
        return True