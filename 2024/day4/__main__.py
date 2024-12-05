

directions = [
        (-1,-1),( 0,-1),( 1,-1),
        (-1, 0),        ( 1, 0),
        (-1, 1),( 0, 1),( 1, 1)
    ]


def format(value):
    lines = value.split('\n')
    output = []
    for line in lines:
        output.append(list(line))

    return output


def find(puzzle,direction,coord,trie):
    if 'end' in trie:
        print(f'found!')
        return 1
    elif 0 <= coord[1] < len(puzzle) and 0 <= coord[0] < len(puzzle[coord[1]]) and puzzle[coord[1]][coord[0]] in trie:
        print(f'found: {puzzle[coord[1]][coord[0]]}, x: {coord[0]}, y: {coord[1]}')
        return find(puzzle,direction,(coord[0] + direction[0],coord[1] + direction[1]),trie[puzzle[coord[1]][coord[0]]])
    return 0



def part1(value):
    xmas_trie = {
                'X' : {
                        'M' : {
                                'A' : {
                                        'S': {
                                                'end' : 0
                                            }
                                    }
                            }
                    }
            }
    total = 0

    for y in range(len(value)):
        for x in range(len(value[y])):
            for (dx,dy) in directions:
                total += find(value,(dx,dy),(x,y),xmas_trie)

    return total

def part2(value):
    mas_trie ={
                'M' : {
                        'A' : {
                                'S': {
                                        'end' : 0
                                    }
                            }
                    },
                'S' : {
                        'A' : {
                                'M': {
                                        'end' : 0
                                    }
                            }
                    }
            }

    total = 0
    for y in range(len(value)):
        for x in range(len(value[y])):
            if value[y][x] == 'A':
                print(f'A @ x: {x}, y: {y}')
                '''
                Down & Left
                find(value,(-1,1),(x+1,y-1),mas_trie)

                Down & Right
                find(value,(1,1),(x-1,y-1),mas_trie)
                '''

                if find(value,(1,1),(x-1,y-1),mas_trie) and find(value,(-1,1),(x+1,y-1),mas_trie):
                    total += 1
    return total



if __name__ == '__main__':

    test_file = open('test1.txt','r')
    test_input = test_file.read()
    test_file.close()

    input_file = open('input.txt','r')
    part1_input = input_file.read()
    input_file.close()

    print(f'input test: {test_input}')

    print(f'input formatting: {format(test_input)}')

    #print(f'part1 test: {part1(format(test_input))}')

    #print(f'part1 solution: {part1(format(part1_input))}')
 
    print(f'part2 test: {part2(format(test_input))}')

    print(f'part2 solution: {part2(format(part1_input))}')

