def format(puzzle):
    keys, locks = [],[]
    grids = [[list(y) for y in g.split('\n')] for g in puzzle.strip().split('\n\n')]

    for grid in grids:
        if grid[0] == ['#','#','#','#','#']:
            heights = [0] * len(grid[0])
            for y in range(len(grid[0])):
                height = 0
                for x in range(1,len(grid)):
                    if grid[x][y] == '#':
                        height += 1

                heights[y] = height
            locks.append(heights)

        if grid[0] == ['.','.','.','.','.']:
            heights = [0] * len(grid[0])
            for y in range(len(grid[0])):
                height = 0
                for x in range(0,len(grid)-1):
                    if grid[x][y] == '#':
                        height += 1
                heights[y] = height
            keys.append(heights)

    return [locks,keys]

def part1(locks,keys):

    total = 0
    for lock in locks:
        for key in keys:
            fit = True
            for i in range(len(lock)):
                if lock[i] + key[i] >= 6:
                    fit = False
            total += fit
    return total

        



if __name__ == "__main__":
    test_file = open("test1.txt",'r')
    test_data = test_file.read()
    test_file.close()

    input_file = open("input1.txt",'r')
    input_data = input_file.read()
    input_file.close()

    print(f"part1 test data: {test_data}")

    print(f"part1 formatting: {format(test_data)}")

    test_locks, test_keys = format(test_data)

    print(f"part1 test: {part1(test_locks,test_keys)}")

    locks, keys = format(input_data)

    print(f"part1 solution: {part1(locks,keys)}")
