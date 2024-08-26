from collections import defaultdict

st = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
st1 = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]


def groupPaths(paths):
    path_dict = defaultdict(list)
    for path in paths:
        path_list = path.split(" ")
        root = path_list[0]
        for path_ele in path_list[1:]:
            open_idx = path_ele.find('(')
            content = path_ele[open_idx + 1:-1]
            path_dir = root + "/" + path_ele[:open_idx]
            path_dict[content].append(path_dir)
    print(path_dict)
    ans = []
    for key in path_dict:
        ans.append(path_dict[key])
    return ans


# print(groupPaths(st1))


def findWinner(arr, k):
    left, right = 0, 1
    n = len(arr)
    winner = -1
    count = 0
    if k >= n - 1:
        k = n - 1
    while left < right and right < n:
        if arr[left] < arr[right]:
            if arr[right] == winner:
                count += 1
            else:
                winner = arr[right]
                count = 1
            left = right
            right += 1
        else:
            if arr[left] == winner:
                count += 1
            else:
                winner = arr[left]
                count = 1
            right += 1
        if count == k:
            return winner
        print(winner, count)
    # return -1


arr = [2, 1, 3, 5, 4, 6, 7]
k = 2
arr = [3, 2, 1]
k = 10
print(findWinner(arr, k))






