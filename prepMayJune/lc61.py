'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
'''

class TrieNode:
    def __init__(self):
        self.children={}
        self.end_of_word=False
class WordDictionary:
    def __init__(self):
        self.root=TrieNode()

    def addWord(self,word):
        curr=self.root
        for w in word:
            if w not in curr.children:
                curr.children[w]=TrieNode()
            curr=curr.children[w]
        curr.end_of_word=True

    def search(self,word):
        return self._search_in_word(word,self.root)

    def _search_in_word(self,word,root):
        for i,char in enumerate(word):
            #core logic -> to check for . and then search in rest words after that.
            if char==".":
                for child in root.children:
                    if self._search_in_word(word[i+1:],root.children[child]):
                        return True
                return False
            else:
                if char not in root.children:
                    return False
                root=root.children[char]
        return root.end_of_word

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))#; // return False
print(wordDictionary.search("bad"))#; // return True
print(wordDictionary.search(".ad"))#; // return True
print(wordDictionary.search("b.."))#; // return True