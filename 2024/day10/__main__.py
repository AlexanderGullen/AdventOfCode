from collections import deque

"""
Today I wanted to invert the way I usually order coordinates, hence why 'y' is now 0 and 'x' is now 1
"""

def format(puzzle):
    return [[ int(x) for x in list(y)] for y in puzzle.strip().split('\n')]


def part1(puzzle):
    directions = [[-1,0],[0,-1],[0,1],[1,0]]
    trailheads = list()
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] == 0:
                       trailheads.append([y,x])
    total = 0
    for trailhead in trailheads:
        found_summits = set()

        paths = 0
        stack = deque()
        stack.append((0,[trailhead[0],trailhead[1]]))
        while len(stack) > 0:
            steps, current = stack.popleft()

            if  current[0] < 0 or current[0] >= len(puzzle) or current[1] < 0 or current[1] >= len(puzzle[0]):
                      pass
            elif steps == puzzle[current[0]][current[1]] and steps == 9:
                found_summits.add((current[0],current[1]))
            elif steps == puzzle[current[0]][current[1]]:
                for d in directions:
                    dy, dx = current[0] + d[0], current[1] + d[1]
                    if 0 <= dy < len(puzzle) and 0 <= dx < len(puzzle[0]) and puzzle[dy][dx] == (steps +1):
                      stack.append((steps+1,[dy,dx]))
        total += len(found_summits)
    return total


def part2(puzzle):
    directions = [[-1,0],[0,-1],[0,1],[1,0]]
    trailheads = list()
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] == 0:
                       trailheads.append([y,x])
    total = 0
    for trailhead in trailheads:
        paths = 0
        stack = deque()
        stack.append((0,[trailhead[0],trailhead[1]]))
        while len(stack) > 0:
            steps, current = stack.popleft()

            if  current[0] < 0 or current[0] >= len(puzzle) or current[1] < 0 or current[1] >= len(puzzle[0]):
                pass
            elif steps == puzzle[current[0]][current[1]] and steps == 9:
                total += 1
            elif steps == puzzle[current[0]][current[1]]:
                for d in directions:
                    dy, dx = current[0] + d[0], current[1] + d[1]
                    if 0 <= dy < len(puzzle) and 0 <= dx < len(puzzle[0]) and puzzle[dy][dx] == (steps +1):
                      stack.append((steps+1,[dy,dx]))
    return total

if __name__ == "__main__":
    test_file = open("test1.txt",'r')
    test_data = test_file.read()
    test_file.close()

    input_file = open("input1.txt",'r')
    input_data = input_file.read()
    input_file.close()

    print(f"part1 test input: {test_data}")

    print(f"part1 test formatted: {format(test_data)}")

    print(f"part1 test: {part1(format(test_data))}")

    print(f"part1 solution: {part1(format(input_data))}")

    print(f"part2 test: {part2(format(test_data))}")

    print(f"part2 solution: {part2(format(input_data))}")

