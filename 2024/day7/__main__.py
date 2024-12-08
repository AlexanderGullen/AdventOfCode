def format(puzzle):
    records = puzzle.strip().split('\n')
    tests = [0] * len(records)

    for i in range(len(records)):
        total, rest = records[i].split(':')
        values = [int(v) for v in rest.strip().split(' ')]

        tests[i] = (int(total),values)
    return tests

def recurse(values,stack,y):
    if len(stack) == len(values) and stack[-1] == y:
        return 1
    if len(stack) >= len(values) or stack[-1] > y:
        stack.pop()
        return 0

    total = 0
    if recurse(values,stack + [stack[-1] + values[len(stack)]],y) or recurse(values,stack + [stack[-1] * values[len(stack)]],y):
        return 1
    return 0

def part1(tests):
    total = 0
    for test in tests:
        stack = [test[1][0]]


        if recurse(test[1],stack,test[0]):
            total += test[0]
    return total


def recurse2(values,stack,y):
    if len(stack) == len(values) and stack[-1] == y:
        return 1
    if len(stack) >= len(values) or stack[-1] > y:
        stack.pop()
        return 0
    if recurse2(values,stack + [stack[-1] + values[len(stack)]],y) or recurse2(values,stack + [stack[-1] * values[len(stack)]],y) or recurse2(values,stack + [int(str(stack[-1]) + str(values[len(stack)]))],y):
        return 1
    return 0


def part2(tests):
    total = 0
    for test in tests:
        stack = [test[1][0]]
        if recurse2(test[1],stack,test[0]):
            total += test[0]
    return total


if __name__ == "__main__":

    test_file = open("test1.txt","r")
    test_data = test_file.read()
    test_file.close()

    input_file = open("input1.txt","r")
    input_data = input_file.read()
    input_file.close()

    print(f"part1 formatting: {format(test_data)}")

    print(f"part1 test: {part1(format(test_data))}")

    print(f"part1 solution: {part1(format(input_data))}")


    print(f"part2 test: {part2(format(test_data))}")

    print(f"part2 solution: {part2(format(input_data))}")

