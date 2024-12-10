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

def part2(disk_map):
    expanded_map = list()
    
    id_counter = 0
    for i in range(len(disk_map)):
        if i % 2 == 1:
            expanded_map += ['.'] * int(disk_map[i])
        else:
            expanded_map += [id_counter] * int(disk_map[i])
            id_counter += 1

    compressed = list(expanded_map)

    l,r, = 0, len(expanded_map) - 1


    #listen, this isn't the most clever, or the most careful, or the most anything (exept maybe horrible) solution to this problem,
    # but considering it was only 6 months ago that I didn't understand time complexity I think it's quite impressive I even managed
    # to get this far. It's a brute force solution, but at least now I can see the shape of the actual solution a little bit.
    # also why the hell are you reading this deep into a blogpost disguised as a comment? Thanks though =)

    while r > 0:
        if compressed[r] != '.':
            contiguous_length = 0
            contiguous_value = compressed[r]
            while compressed[r - contiguous_length] == contiguous_value:
                contiguous_length += 1
            
            l=0
            while l < r:
                if compressed[l] == '.':
                    buffer_length = 0
                    while compressed[l + buffer_length] == '.':
                        buffer_length += 1
                    if buffer_length >= contiguous_length:
                        compressed[l:l+contiguous_length] = [contiguous_value] * contiguous_length
                        compressed[r-contiguous_length + 1:r + 1] = ['.'] * contiguous_length
                        l+= contiguous_length
                        break

                    l += buffer_length
                else:
                    l += 1

            r -= contiguous_length
        else:
            r -= 1
            
    total = 0
    for i in range(len(compressed)):
        if compressed[i] != '.':
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

    print(f"part2 test: {part2(test_data)}")

    print(f"part2 solution: {part2(input_data)}")
