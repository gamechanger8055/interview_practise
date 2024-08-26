'''
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize,
 and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true
 if she can rearrange the cards, or false otherwise.



Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.



Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
'''

from collections import Counter
import heapq


def checkIfCardsCanBeArranged(hand, groupSize):
    if len(hand) % groupSize != 0:
        return False

    card_count = Counter(hand)
    min_heap = list(card_count.keys())
    heapq.heapify(min_heap)

    while min_heap:
        first_card = min_heap[0]
        for card in range(first_card, first_card + groupSize):
            if card_count[card] == 0:
                return False
            card_count[card] -= 1
            if card_count[card] == 0:
                if card != min_heap[0]:
                    return False
            heapq.heappop(min_heap)
        return True


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
print(checkIfCardsCanBeArranged(hand, groupSize))
