from collections import defaultdict
import math

def format(puzzle):
    #split puzzle string into grid
    return [list(y) for y in puzzle.strip().split('\n')]

def get_antinodes(node_a,node_b):
    antinodes = [(0,0),(0,0)]

    dx, dy = node_b[0] - node_a[0], node_b[1] - node_a[1]
    slope = dy / dx
    distance = math.sqrt((dx * dx) + (dy * dy))
    b = node_a[1] - (slope * node_a[0])

    f = lambda x: (slope*x)+b

    antinodes[0] = (node_a[0] - dx,round(f(node_a[0] - dx)))
    antinodes[1] = (node_b[0] + dx,round(f(node_b[0] + dx)))
    #print(f"dx: {dx}, dy: {dy}, slope: {slope}, distance: {distance}, b: {b}")

    #print(f"f: {f(node_a[0] - dx)}")



    return antinodes

def part1(grid):
    antinodes = set()
    antennas = defaultdict(list)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '.':
                antennas[grid[y][x]] += [(x,y)]
    
    #print(antennas)

    for frequency in antennas.values():
        #print(frequency)
        l,r = 0,1
        while l < len(frequency):
            while r < len(frequency):
                #print(f"combination: {sorted([frequency[l],frequency[r]])}")
                ordered = sorted([frequency[l],frequency[r]])
                first, second = ordered[0], ordered[1]
                for node in get_antinodes(first,second):
                    #print(f"{node}")
                    if 0 <= node[0] < len(grid[0]) and 0 <= node[1] < len(grid):
                        antinodes.add(node)
                        if grid[node[1]][node[0]] == '.':
                            grid[node[1]][node[0]] = '#'
                r += 1
            l += 1
            r  = l + 1
    #print(antinodes)
    #print(grid)
    return len(antinodes)

if __name__ == "__main__":

    test_file = open("test1.txt","r")
    test_data = test_file.read()
    test_file.close()

    input_file = open("input1.txt","r")
    input_data = input_file.read()
    input_file.close()

    print(f"part1 formatted: {format(test_data)}")

    print(f"part1 test: {part1(format(test_data))}")

    print(f"part1 solution: {part1(format(input_data))}")


