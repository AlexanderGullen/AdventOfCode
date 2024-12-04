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


    ''' Oh christmas trie, Oh christmas trie, how lovely are your... branch'''
    christmas_trie = {
            'd': { 
                  'o' : {
                        '(' : {
                                ')' : {
                                        'end' : 1,
                                    }
                            },
                        'n' : { 
                               '\'' : { 
                                       't' : { 
                                              '(' : { 
                                                     ')' : {
                                                            'end': 0
                                                         }
                                                     }
                                              }
                                       }
                               }
                        }
                  }
            }

    do = True

    r = 0

    current = {}

    positive = ''

    while r < len(value):

        if value[r] in current:
            current = current[value[r]]

        elif 'end' in current:
            do = current['end']
        else:
            current = {}

        if value[r] in christmas_trie:
            current = christmas_trie[value[r]]

        if do:
            positive += value[r]

        r += 1

    return part1(positive)


if __name__ == '__main__':

    test_file = open('test.txt','r')
    test_value = test_file.read()
    test_file.close()

    input_file = open('input.txt','r')
    input_value = input_file.read()
    input_file.close()

    print(f'test data: {test_value}')

    print(f'part1 test {part1(test_value)}')

    print(f'part1 solution {part1(input_value)}')

    test_file = open('test2.txt','r')
    test_value = test_file.read()
    test_file.close()

    print(f'test data: {test_value}')

    print(f'part2 test {part2(test_value)}')


    print(f'part2 solution {part2(input_value)}')







