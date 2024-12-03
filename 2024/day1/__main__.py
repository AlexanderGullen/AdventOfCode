import heapq



def part1(right,left): 
    """
    """
    heapq.heapify(right)
    heapq.heapify(left)

    comparisons = min(len(right),len(left))

    total = 0

    for i in range(comparisons):
        total += abs(heapq.heappop(right) - heapq.heappop(left))

    return total

def part2(right,left):
    left_count = {}

    total = 0

    for i in range(len(left)):
        if left[i] not in left_count:
            left_count[left[i]] = 1
        else:
            left_count[left[i]] += 1

    for i in range(len(right)):
        if right[i] in left:
            total += right[i] * left_count[right[i]]

    print(left_count)

    return total

if __name__ == '__main__':

    input_right = [3]
    input_left = [7]
    print(f'part1 test1: {part1(input_right,input_left)}')

    print(f'part1 solution: {part1(input_right,input_left)}')

    input_right = [3,4,2,1,3,3]
    input_left = [4,3,5,3,9,3]
    print(f'part2 test1: {part2(input_right,input_left)}')

    print(f'part2 solution: {part2(input_right,input_left)}')
