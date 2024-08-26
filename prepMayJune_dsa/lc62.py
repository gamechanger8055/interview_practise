'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.

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

def findWords(board,words):
    trie=Trie()
    m,n=len(board),len(board[0])
    for word in words:
        trie.insert(word)
    result=set()
    visited=set()
    def backtracking(r,c,node,curr_word):
        #base condn
        if r<0 or r==m or c<0 or c==n or board[r][c] not in node.children or (r,c) in visited:
            return
        curr_word+=board[r][c]
        visited.add((r, c))
        node = node.children[board[r][c]]
        if node.end_of_word:
            result.add(curr_word)
        backtracking(r, c+1, node, curr_word)
        backtracking(r, c-1, node, curr_word)
        backtracking(r+1, c, node, curr_word)
        backtracking(r-1, c, node, curr_word)
        visited.remove((r,c))

    for r in range(m):
        for c in range(n):
            backtracking(r,c,trie.root,"")
    return list(result)

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(findWords(board,words))