'''
/***
 * Part 1
 * Imagine an Airbnb-like vacation rental service, where users in different cities can exchange their apartment with another user for a week.
 * Each user compiles a wishlist of the apartments they like.
 * These wishlists are ordered, so the top apartment on a wishlist is that user's first choice for where they would like to spend a vacation.
 * You will be asked to write part of the code that will help an algorithm find pairs of users who would like to swap with each other.
 *
 * Given a set of users, each with an *ordered* wishlist of other users' apartments:
 *   a's wishlist: c d
 *   b's wishlist: d a c
 *   c's wishlist: a b
 *   d's wishlist: c a b
 * The first user in each wishlist is the user's first-choice for whose apartment they would like to swap into.
 * Write a function called has_mutual_first_choice() which takes a username and returns true if that user and another user are each other's first choice, and otherwise returns false.
 *
 * has_mutual_first_choice('a') // true (a and c)
 * has_mutual_first_choice('b') // false (b's first choice does not *mutually* consider b as their first choice)
 *
 * Then expand the base case beyond just "first" choices, to include all "mutually ranked choices".
 * Write another function which takes a username and an option called "rank" to indicate the wishlist rank to query on.
 * If given a rank of 0, you should check for a first choice pair, as before.
 * If given 1, you should check for a pair of users who are each others' second-choice.
 * Call your new function has_mutual_pair_for_rank() and when done, refactor has_mutual_first_choice() to depend on your new function.
 *
 * has_mutual_pair_for_rank('a', 0) // true (a and c)
 * has_mutual_pair_for_rank('a', 1) // true (a and d are mutually each others' second-choice)
 *
 * data = {
 *   'a': ['c', 'd'],
 *   'b': ['d', 'a', 'c'],
 *   'c': ['a', 'b'],
 *   'd': ['c', 'a', 'b'],
 * }
 *
 * Part2
 * Every wishlist entry in the network is either "mutually ranked" or "not mutually ranked" depending on the rank the other user gives that user's apartment in return.
 * The most common operation in the network is incrementing the rank of a single wishlist entry on a single user.
 * This swaps the entry with the entry above it in that user's list.
 * Imagine that, when this occurs, the system must recompute the "mutually-ranked-ness" of any pairings that may have changed.
 * Write a function that takes a username and a rank representing the entry whose rank is being bumped up.
 * Return an array of the users whose pairings with the given user *would* gain or lose mutually-ranked status as a result of the change, if it were to take place.
 * Call your function changed_pairings()
 *
 * // if d's second choice becomes their first choice, a and d will no longer be a mutually ranked pair
 * changed_pairings('d', 1) // returns ['a']
 *
 * // if b's third choice becomes their second choice, c and b will become a mutually ranked pair (mutual second-choices)
 * changed_pairings('b', 2) // returns ['c']
 *
 * // if b's second choice becomes their first choice, no mutually-ranked pairings are affected
 * changed_pairings('b', 1) // returns []
 *
 */
'''

def has_mutual_first_choice(username, data):
    return has_mutual_pair_for_rank(username,0,data)

def has_mutual_pair_for_rank(username, rank, data):
    if username not in data or len(data[username])<rank:
        return False
    target=data[username][rank]
    if target not in data or rank >= len(data[target]):
        return False
    return data[target][rank]==username

def changed_pairings(username, rank, data):
    if username not in data or rank<=0 or rank>=len(data[username]):
        return []

    changed_users=[]
    target=data[username][rank]
    above_target = data[username][rank - 1]
    data[username][rank], data[username][rank - 1] = data[username][rank - 1], data[username][rank]

    if has_mutual_pair_for_rank(username,rank-1,data)!=has_mutual_pair_for_rank(username,rank,data):
        changed_users.append(target)
    if has_mutual_pair_for_rank(username,rank,data)!=has_mutual_pair_for_rank(username,rank-1,data):
        changed_users.append(above_target)

    data[username][rank], data[username][rank - 1] = data[username][rank - 1], data[username][rank]

    return list(set(changed_users))

data = {
    'a': ['c', 'd'],
    'b': ['d', 'a', 'c'],
    'c': ['a', 'b'],
    'd': ['c', 'a', 'b'],
}

# Part 1 tests
print(has_mutual_first_choice('a', data))  # True
print(has_mutual_first_choice('b', data))  # False

# Part 2 tests
print(has_mutual_pair_for_rank('a', 0, data))  # True
print(has_mutual_pair_for_rank('a', 1, data))  # True
print(has_mutual_pair_for_rank('b', 0, data))  # False
print(has_mutual_pair_for_rank('d', 0, data))  # False

# Part 3 tests
print(changed_pairings('d', 1, data))  # ['a']
print(changed_pairings('b', 2, data))  # ['c']
print(changed_pairings('b', 1, data))  # []