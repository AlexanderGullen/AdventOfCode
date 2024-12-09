def part1(disk_map):
    expanded_map = list()
    
    id_counter = 0
    for i in range(len(disk_map)):
        if i % 2 == 1:
            expanded_map += ['.'] * int(disk_map[i])
        else:
            expanded_map += [id_counter] * int(disk_map[i])
            id_counter += 1

    compressed = list()

    l,r, = 0, len(expanded_map) - 1

    while l <= r:
        if expanded_map[l] == '.':
            compressed.append(int(expanded_map[r]))
            expanded_map[r] = '.'
            while expanded_map[r] == '.':
                r -= 1
        else:
            compressed.append(int(expanded_map[l]))
        l += 1

    total = 0
    for i in range(len(compressed)):
        total += i * compressed[i]
    return total

if __name__ == "__main__":

    test_file = open("test1.txt",'r')
    test_data = test_file.read().strip()
    test_file.close()

    input_file = open("input1.txt",'r')
    input_data = input_file.read().strip()
    input_file.close()

    print(f"part1 test: {part1(test_data)}")

    print(f"part1 solution: {part1(input_data)}")

