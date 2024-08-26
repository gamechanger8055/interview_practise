'''
Given input =>
stripe.com/payments/checkout/customer.maria
output =>s4e.c1m/p6s/c6t/c6r.m3a

For example, imagine compressing a URL such as "section/how.to.write.a.java.program.in.one.day".
After compressing it by following the rules in Part 1, the second major part still has 9 minor parts after compression.

Task: Therefore, to further compress the String, we want to only keep at most m (m>0) compressed minor parts from Part 1 within each major part.

If a major part has more than m minor parts, we keep the first (m-1) minor parts as is,
but concatenate the first letter of the m-th minor part and the last letter of the last minor part with the count of letters in the original string.
This means that if you build on top of results that have numeronyms, you should expand
on the numbers to count the number or letters in the original String, e.g, "w1w.s4e.c1m"
should be compressed into "w10m" instead of "w7m" (go through the examples below). You can either reuse Part 1 output or not.
If a major part has less than or equal to m minor parts, keep all the individual minor parts as they are from Part 1.

Example :
Given:
str = stripe.com/payments/checkout/customer.maria.doe
minor_parts = 2

(after Part 1 compression)
=>
s4e.c1m/p6s/c6t/c6r.m3a.d1e

(then after Part 2 compression)
=>
s4e.c1m/p6s/c6t/c6r.m6e

Step-by-step guide for part 2 compression:

For the last major part "c6r.m3a.d1e", keep the first 2-1=1 minor part "c6r"
For the rest of the minor parts "m3a.d1e", compress into "m6e"
Combine "c6r.m6e" (from step 1 and 2) as the last compressed major part
Do the same for the rest of the major parts (if applicable)
Example starter code
String compress_part_two(String str, Int minor_parts) {
// You can either use results from compress_part_one(str) or not.
return compressed_s;
}

'''

def compress_word(s):
    return f'{s[0]}{len(s)-2}{s[-1]}'

def further_compress(s,m):
    parts=s.split(".")
    if len(parts)<=m:
        return s
    rem_parts=parts[m-1:]
    total_char=sum(len(part) for part in rem_parts)
    return ".".join(parts[:m-1]+[f'{rem_parts[0][0]}{total_char}{rem_parts[-1][-1]}'])

def compress_part1(words):
    word_list=words.split("/")
    compressed=[]
    for parts in word_list:
        subparts=parts.split(".")
        compressed_subparts=[compress_word(word) for word in subparts]
        reverted=".".join(compressed_subparts)
        compressed.append(reverted)
    return "/".join(compressed)

def compress_part2(words,m):
    compressed=compress_part1(words)
    comp_list=compressed.split('/')
    further_compressed=[further_compress(word,m) for word in comp_list]
    return "/".join(further_compressed)

input_string = "stripe.com/payments/checkout/customer.maria.doe"
print(compress_part1(input_string))
#op1=compress_part_one(input_string)
print(compress_part2(input_string,1))
