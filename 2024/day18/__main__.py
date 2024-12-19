from collections import defaultdict
import heapq

def format(puzzle):
    return [(int(s.split(',')[0]),int(s.split(',')[1])) for s in puzzle.strip().split()]

def part1(pixels,w,n):
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    edges = defaultdict(list)
    malfunctioning=set(pixels[:n])

    #create a graph for traversal
    for y in range(w+1):
        for x in range(w+1):
            for d in directions:
                if x + d[0] >= 0 and y + d[1] >= 0 and x + d[0] <= w and y + d[1] <= w and (x + d[0],y + d[1]) not in malfunctioning:
                    edges[(x,y)].append((x + d[0],y + d[1]))
    

    #djikstra's algorithm
    heap = []
    distances = dict()
    heapq.heappush(heap,(0,(0,0)))
    distances[(0,0)] = 0

    while len(heap) > 0:
        current = heapq.heappop(heap)

        if current[1] == (w,w):
            break

        for edge in edges[current[1]]:
            new_cost = distances[current[1]] + 1
            if edge not in distances or new_cost < distances[edge]:
                distances[edge] = new_cost
                heapq.heappush(heap,(new_cost,edge))

    return distances[(w,w)]

def traversable(edges,w):
    heap = []
    distances = dict()
    heapq.heappush(heap,(0,(0,0)))
    distances[(0,0)] = 0

    while len(heap) > 0:
        current = heapq.heappop(heap)

        if current[1] == (w,w):
            break
        
        for edge in edges[current[1]]:
            new_cost = distances[current[1]] + 1
            if edge not in distances or new_cost < distances[edge]:
                distances[edge] = new_cost
                heapq.heappush(heap,(new_cost,edge))

    return True if (w,w) in distances else False


def part2(pixels,w):
    n = 0

    while True:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        edges = defaultdict(list)
        malfunctioning=set(pixels[:n])

        #create a graph for traversal
        for y in range(w+1):
            for x in range(w+1):
                for d in directions:
                    if x + d[0] >= 0 and y + d[1] >= 0 and x + d[0] <= w and y + d[1] <= w and (x + d[0],y + d[1]) not in malfunctioning:
                        edges[(x,y)].append((x + d[0],y + d[1]))
        if not traversable(edges,w):
            return pixels[n - 1]
        n += 1


if __name__ == "__main__":
    test_file = open("test1.txt",'r')
    test_data = test_file.read()
    test_file.close()

    input_file = open("input1.txt",'r')
    input_data = input_file.read()
    input_file.close()


    print(f"part1 format: {format(test_data)}")

    print(f"part1 test: {part1(format(test_data),6,12)}")

    print(f"part1 solution: {part1(format(input_data),70,1024)}")

    print(f"part2 test: {part2(format(test_data),6)}")

    print(f"part2 solution: {part2(format(input_data),70)}")
