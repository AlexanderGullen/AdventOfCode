def formatInput(raw):
    '''function to format the raw string input of the puzzel into a computer readable version of the problem'''
    reports = raw.strip().split('\n')
    output = [[]] * len(reports)


    for i in range(len(reports)):
        output[i] = [int(f) for f in reports[i].split(' ')]

    return output


def part1(reports):
    '''Returns the number of safe reports as defined by this problem: https://adventofcode.com/2024/day/2'''
    safe_reports = 0

    for report in reports:

        increasing = True if report[0] < report[-1] else False
        safe = True

        left,right = 0,1

        while right < len(report):
            difference = report[right] - report[left]

            if increasing and not (difference <= 3 and difference >= 1):
                safe = False
                break
            if (not increasing) and not (difference >= -3 and difference <= -1):
                safe = False
                break

            left += 1
            right += 1

        safe_reports += safe

    return safe_reports


def part2(reports):
    '''Returns the number of safe reports as defined by this problem: https://adventofcode.com/2024/day/2'''
    safe_reports = 0

    for report in reports:
        print(report)
        faults = 0

        increasing = []
        decreasing = []


        # 9 1 2 3  4 5
        # 9 6 9 12 9 6

    return safe_reports


if __name__ == '__main__':

    test_file = open('test.txt','r')
    test_input = test_file.read()
    test_file.close()

    print('##### Formatting #####')

    print(f'unformatted: {test_input}')

    print(f'formatted: {formatInput(test_input)}')



    print('##### Testing #####')

    print(f'test1 solution: {part2(formatInput(test_input))}')


    print('##### Solution #####')

    input_file = open('input.txt','r')

    solution_input = input_file.read()

    input_file.close()

    print(f'unformatted: {solution_input}')

    #print(f'formatted: {formatInput(solution_input)}')


    print(f'part2 solution: {part2(formatInput(solution_input))}')

    #print(f'part1 solution: {part1(formatInput(solution_input))}')

    print(len(solution_input))








