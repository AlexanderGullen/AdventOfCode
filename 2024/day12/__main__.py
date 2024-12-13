from collections import deque


def format(puzzle):
    return [list(y) for y in puzzle.strip().split('\n')]


def part1(puzzle):
    directions = [( 0,-1),(-1, 0),( 1, 0),( 0, 1)]
    visited = set()

    def get_area(puzzle,area,x,y):
        total = 0
        queue = deque()
        local_visited = set()
        queue.append((x,y))
        visited.add((x,y))
        local_visited.add((x,y))
        fences = []
        while len(queue) > 0:
            current = queue.popleft()
            total += 1
            for d in directions:
                dx,dy = current[0] + d[0], current[1] + d[1]
                if (dx,dy) in local_visited:
                    pass

                elif dx < 0 or dy < 0 or dx >= len(puzzle[0]) or dy >= len(puzzle):
                    if (dx,dy) not in fences:
                        fences.append((dx,dy))
                    pass

                elif puzzle[dy][dx] != area:
                    fences.append((dx,dy))
                    pass


                else:
                    visited.add((dx,dy))
                    local_visited.add((dx,dy))
                    queue.append((dx,dy))
        return total, len(fences)


    def get_perimiter(puzzle,x,y):
        return 0

    areas = list() # (letter,area,perimiter)
    total = 0

    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if (x,y) not in visited:
                area, perimiter = get_area(puzzle,puzzle[y][x],x,y)
                total += area * perimiter
                areas.append((puzzle[y][x],area,perimiter))
                visited.add((x,y))

    return total



if __name__ == "__main__":
    test_file = open("test1.txt",'r')
    test_data = test_file.read()
    test_file.close()

    print(f"part1 formatting: {format(test_data)}")
    print(f"part1 test: {part1(format(test_data))}")


    test_file = open("test2.txt",'r')
    test_data = test_file.read()
    test_file.close()

    print(f"part1 formatting: {format(test_data)}")
    print(f"part1 test2: {part1(format(test_data))}")

    test_file = open("test3.txt",'r')
    test_data = test_file.read()
    test_file.close()

    print(f"part1 formatting: {format(test_data)}")
    print(f"part1 test3: {part1(format(test_data))}")

    input_file = open("input1.txt",'r')
    input_data = input_file.read()
    input_file.close()

    print(f"part1 formatting: {format(input_data)}")
    print(f"part1 solution: {part1(format(input_data))}")



