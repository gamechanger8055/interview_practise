'''
String Encode and Decode
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
'''

def encode(strs):
    s=""
    for st in strs:
        s+=st+"#"
    return s[:-1]

def decode(s):
    st=s.split("#")
    return st

strs=["neet","code","love","you"]
enc=encode(strs)
dec=decode(enc)
print(enc,dec)