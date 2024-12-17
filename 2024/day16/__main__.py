from collections import defaultdict
from collections import deque

def format(puzzle):
    return [list(y) for y in puzzle.strip().split('\n')]

def part1(puzzle):
    # Up down left right
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    start = (0,0)
    end = (0,0)

    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] == 'S':
                start = (x,y)
            if puzzle[y][x] == 'E':
                end = (x,y)

    def walk(puzzle,current,direction,nodes):
        opposite = (direction[0] - (direction[0] * 2), direction[1] - (direction[1] * 2))
        intersection = False

        for d in directions:
            if d != direction and d != opposite:
                if puzzle[current[1] + d[1]][current[0] + d[0]] == '.':
                    intersection = True

        if intersection:
            nodes.append(current)


        if puzzle[current[1] + direction[1]][current[0] + direction[0]] == '#':
            return nodes
        else:
            return walk(puzzle,(current[0] + direction[0],current[1] + direction[1]),direction,nodes)

    paths = deque()

    adj_list = defaultdict(list)

    paths.append(start)
    while len(paths) > 0:
        current = paths.pop()
        if current not in adj_list:
            result = []
            for d in directions:
                if puzzle[current[1] + d[1]][current[0] + d[0]] == '.':
                    result += walk(puzzle,(current[0] + d[0],current[1] + d[1]),d,[])
            for r in result:
                paths.append(r)
                adj_list[current].append(r)

    print(adj_list)

if __name__ == "__main__":
    test_file = open("test1.txt",'r')
    test_data = test_file.read()
    test_file.close()

    print(f"part1 formatting: {format(test_data)}")

    print(f"part1 test1: {part1(format(test_data))}")

    test_file = open("test2.txt",'r')
    test_data = test_file.read()
    test_file.close()

    print(f"part1 test2: {part1(format(test_data))}")

    input_file = open("input1.txt",'r')
    input_data = input_file.read()
    input_file.close()

    print(f"part1 solution: {part1(format(input_data))}")
