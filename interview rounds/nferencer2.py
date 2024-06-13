def max_diff_substring(s):
    max_diff = 0
    start = 0
    end = 0
    max_substrings = []
    count0, count1 = 0, 0
    max_length = 0
    for i in range(len(s)):
        if s[i] == '1':
            count1 += 1
        else:
            count0 += 1
        diff = count1 - count0
        length = i - start + 1
        if diff > max_diff:
            max_diff = diff
            max_length = length
            # if length>max_length:
            #     max_length=length
            max_substrings = [s[start:i + 1]]

        elif diff == max_diff:
            if length > max_length:
                max_length = length
                max_substrings = [s[start:i + 1]]
            elif length == max_length:
                max_substrings.append(s[start:i + 1])
        if diff < 0:
            count1 = 0
            count0 = 0
            start = i + 1
    return max_substrings


s = '1111011100000'
t = '110101'
u = '1010110000001101010000'
for i in [s, t, u]:
    print(max_diff_substring(i))


def kthLargest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.right

        root = stack.pop()
        k -= 1
        if k == 0:
            return root.value
        root = root.left
    return -1



