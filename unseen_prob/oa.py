def suitable_locations(centers, d):
    result = 0

    # Solve location where distance == maximum allowed or right-most-suitable-location
    _max_dist = (lambda x, di: ((di / 2) + sum(x)) / (len(x)))(centers, d)

    check_dist = lambda x, di: sum([2 * abs(di - v) for v in x])

    # If there's no right-most-suitable-location exit
    if _max_dist - int(_max_dist) == 0:
        result += 1
        left = _max_dist - 1

        # Iterate backwards to find the left-most-suitable-location
        while check_dist(centers, left) <= d:
            result += 1
            left -= 1
    return result


case_1 = [2, 0, 3, -4]
d1 = 22

case_2 = [-2, 1, 0]
d2 = 8

print(suitable_locations(case_1, d1))
print(suitable_locations(case_2, d2))


