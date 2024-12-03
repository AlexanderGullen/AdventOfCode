import re

def format():
    pass

def part1(value):

    matches = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)',value)
    
    total = 0

    for match in matches:
        comma = int(match.index(','))
        val1 = int(match[4:comma])
        val2 = int(match[comma+1:-1])

        total += val1 * val2

    return total

def part2(value):
    pass


if __name__ == '__main__':

    test_file = open('test.txt','r')
    test_value = test_file.read()
    test_file.close()

    input_file = open('input.txt','r')
    input_value = input_file.read()
    input_file.close()

    print(test_value)

    print(f'part1 test {part1(test_value)}')

    print(f'part1 solution {part1(input_value)}')





