import heapq


def checkIfWeCanReachEndOfBuilding(heights, bricks, ladders):
    hp = []
    n = len(heights)
    for i in range(n - 1):
        height_diff = heights[i + 1] - heights[i]
        if height_diff > 0:
            heapq.heappush(hp, height_diff)
        if len(hp) > ladders:
            bricks -= heapq.heappop(hp)
            if bricks < 0:
                return i + 1
    return n


heights = [14, 3, 19, 3]
bricks = 17
ladders = 0
print(checkIfWeCanReachEndOfBuilding(heights, bricks, ladders))

