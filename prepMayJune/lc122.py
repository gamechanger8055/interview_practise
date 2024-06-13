'''
Problem Statement: Given a sorted dictionary of an alien language having N words and k starting alphabets of a standard dictionary. Find the order of characters in the alien language.

Note: Many orders may be possible for a particular test case, thus you may return any valid order.

Examples:

Example 1:
Input: N = 5, K = 4
dict = {"baa","abcd","abca","cab","cad"}
Output: b d a c
Explanation:
We will analyze every consecutive pair to find out the order of the characters.
The pair “baa” and “abcd” suggests ‘b’ appears before ‘a’ in the alien dictionary.
The pair “abcd” and “abca” suggests ‘d’ appears before ‘a’ in the alien dictionary.
The pair “abca” and “cab” suggests ‘a’ appears before ‘c’ in the alien dictionary.
The pair “cab” and “cad” suggests ‘b’ appears before ‘d’ in the alien dictionary.
So, [‘b’, ‘d’, ‘a’, ‘c’] is a valid ordering.

Example 2:
Input: N = 3, K = 3
dict = {"caa","aaa","aab"}
Output: c a b
Explanation: Similarly, if we analyze the consecutive pair
for this example, we will figure out [‘c’, ‘a’, ‘b’] is
a valid ordering.

'''