from collections import defaultdict
import heapq

def format(puzzle):
    return [(int(s.split(',')[0]),int(s.split(',')[1])) for s in puzzle.strip().split()]

def part1(pixels,w,n):
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    edges = defaultdict(list)
    malfunctioning=set(pixels[:n])

    print(malfunctioning)

    #create a graph for traversal
    for y in range(w+1):
        for x in range(w+1):
            for d in directions:
                if x + d[0] >= 0 and y + d[1] >= 0 and x + d[0] <= w and y + d[1] <= w and (x + d[0],y + d[1]) not in malfunctioning:
                    edges[(x,y)].append((x + d[0],y + d[1]))
    #print(edges)
    
    heap = []
    visited = set()
    nodes = {k:float("inf") for k in edges.keys()}
    heapq.heappush(heap,(0,(0,0)))
    nodes[(0,0)] = 0

    while len(heap) > 0:
        print(visited)
        current = heapq.heappop(heap)
        visited.add(current[1])
        #print(f"current: {current}")
        #print(f"adjacent: {edges[current[1]]}")
        for edge in edges[current[1]]:
            nodes[edge] = min(nodes[edge],nodes[current[1]] + 1)
            if edge not in visited:
                heapq.heappush(heap,(nodes[edge],edge))

    return nodes[(6,6)]






if __name__ == "__main__":
    test_file = open("test1.txt",'r')
    test_data = test_file.read()
    test_file.close()

    print(f"part1 format: {format(test_data)}")

    print(f"part1 test: {part1(format(test_data),6,12)}")

    input_file = open("input1.txt",'r')
    input_data = input_file.read()
    input_file.close()

    print(f"part1 solution: {part1(format(input_data),70,1024)}")
