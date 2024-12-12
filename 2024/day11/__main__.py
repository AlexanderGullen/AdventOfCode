
def format(stones):
    return stones.strip().split(" ")

def part1(stones,blinks):

    for generation in range(blinks):
        new_stones = list()
        for i in range(len(stones)):
            if stones[i] == '0':
                stones[i] = '1'
            elif len(stones[i]) % 2 == 0:
                length = len(stones[i])
                left, right = int(stones[i][0:length // 2]), int(stones[i][length // 2:])
                stones[i] = str(left)
                new_stones.append(str(right))

            else:
                stones[i] = str(int(stones[i]) * 2024)

        stones += new_stones
    return len(stones)

def part2(stones,blinks):
    total = 0

    mem = {}
    def calculate_max_stones(stone,blinks):
        if blinks <= 0:
            return 1
        if (stone,blinks) in mem:
            return mem[(stone,blinks)]
        if stone == '0':
            mem[('1',blinks-1)] = calculate_max_stones('1',blinks-1)
            return mem[('1',blinks-1)]
        elif len(stone) % 2 == 0:
            left, right = str(int(stone[0:len(stone) // 2])), str(int(stone[len(stone) // 2:]))
            mem[(left,blinks-1)] = calculate_max_stones(left,blinks-1)
            mem[(right,blinks-1)] = calculate_max_stones(right,blinks-1)

            return mem[(left,blinks-1)] + mem[(right,blinks-1)]
        else:
            return calculate_max_stones(str(int(stone) * 2024),blinks-1)

    for stone in stones:
        total += calculate_max_stones(stone,blinks)

    return total

if __name__ == "__main__":
    test_file = open("test1.txt",'r')
    test_data = test_file.read()
    test_file.close()

    input_file = open("input1.txt",'r')
    input_data = input_file.read()
    input_file.close()


    print(f"part1 test input: {format(test_data)}")

    print(f"part1 test (5): {part1(format(test_data),5)}")

    print(f"part1 test (25): {part1(format(test_data),25)}")


    print(f"part1 solution (25): {part1(format(input_data),25)}")

    print(f"part2 test (6): {part2(format(test_data),6)}")

    print(f"part2 test (25): {part2(format(test_data),25)}")

    print(f"part2 solution (75): {part2(format(input_data),75)}")

