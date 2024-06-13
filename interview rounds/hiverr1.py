def maxCandies(x):
    count = x
    while x >= 3:
        count += x // 3
        x = x // 3 + x % 3
    return count


x = 5
print(maxCandies(x))


def makeLinkedListEqual(head, reqd_count, m, lst):
    temp = head
    count = 0
    idx = 0
    while temp and count < reqd_count:
        lst[idx] = temp
        lst[idx] = lst[idx].next
        temp = temp.next
        count += 1
        if count == reqd_count:
            count = 0
            idx += 1
