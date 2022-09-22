# Ruturns minimum time reuired to place mice in holes using the greedy approach. We can put every mouse to its nearest hole to minimize the time. This can be done by sorting the positions of mice and holes.

def assignHole(mice, holes):

    # Base - num of mice and holes should be the same
    if len(mice) != len(holes):
        return "Number of mice and holes not the same!"

    # Sort
    mice.sort()
    holes.sort()

    # Finding max diffrence between mice and holes
    maxDiff = 0

    for i in range(len(mice)):
        if maxDiff < abs(mice[i] - holes[i]):
            maxDiff = abs(mice[i] - holes[i])

    return maxDiff


mice = [4, -4, 2]
holes = [4, 0, 5]

minTime = assignHole(mice, holes)

print("The last mouse gets into the hole in time: ", minTime)
