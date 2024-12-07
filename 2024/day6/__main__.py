

def format(puzzle):
    width = (puzzle.find('\n'))
    height = (len(puzzle) - (puzzle.count('\n'))) // width
    grid = [[0] * width] * height
    start = (0,0)
    for y in range(height):
        row = [' '] * width
        for x in range(width):
            index = x + (y * (width + 1))
            row[x] = puzzle[index]
            if puzzle[index] == '^':
                start = (x,y)
        grid[y] = row

    return [grid, start]

directions = [[0,-1],[1,0],[0,1],[-1,0]]
    

def part1(grid,position):

    total = 0
    direction_index = 0
    visited = set()

    while (position[0] >= 0) and (position[0] < len(grid[0])) and (position[1] >= 0) and (position[1] < len(grid)):
        if grid[position[1]][position[0]] == '#':
            position = (position[0] - directions[direction_index][0],position[1] - directions[direction_index][1])
            direction_index = (direction_index + 1) % 4
        if grid[position[1]][position[0]] != 'X':
            total += 1
        dx, dy = position[0] + directions[direction_index][0], position[1] + directions[direction_index][1]
        grid[position[1]][position[0]] = 'X'

        visited.add((dx,dy))
        position = (dx,dy)

        
    return total




if __name__ == "__main__":

    test_file = open('test1.txt','r')
    test_data = test_file.read()
    test_file.close()

    input_file = open('input1.txt','r')
    input_data = input_file.read()
    input_file.close()
    
    print(f'part1 formatted: {format(test_data)}')

    test_grid, test_start = format(test_data)

    print(f'part1 test: {part1(test_grid,test_start)}')

    input_grid, input_start = format(input_data)

    print(f'part1 solution: {part1(input_grid,input_start)}')

