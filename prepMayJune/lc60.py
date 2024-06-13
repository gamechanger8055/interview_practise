'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
'''

class TrieNode:
    def __init__(self):
        self.children={}
        self.end_of_word=False
class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        curr=self.root
        for w in word:
            if w not in curr.children:
                curr.children[w]=TrieNode()
            curr=curr.children[w]
        curr.end_of_word=True

    def search(self,word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.end_of_word

    def startsWith(self,prefix):
        curr = self.root
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))#;   // return True
print(trie.search("app"))#;     // return False
print(trie.startsWith("app"))#; // return True
trie.insert("app")
print(trie.search("app"))