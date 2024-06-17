with open("day10/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

with open("day10/test.aoc", "r") as file: 
    test_data = [line.strip("\n") for line in file.readlines()]

def return_valid_paths(pipe, data):
    x, y = pipe
    pipe_type = data[x][y]
    potential_paths = []
    match pipe_type:
        case "S":
            if data[x+1][y] in ["|", "J", "L"]:
                potential_paths += [(x+1, y)]
            if data[x-1][y] in ["|", "F", "7"]:
                potential_paths += [(x-1, y)]
            if data[x][y+1] in ["-", "7", "J"]:
                potential_paths += [(x, y+1)]
            if data[x][y-1] in ["-", "F", "L"]:
                potential_paths += [(x, y-1)]
        case "|":
            potential_paths = [(x-1, y), (x+1, y)]
        case "-":
            potential_paths = [(x, y+1), (x, y-1)]
        case "F":
            potential_paths = [(x+1, y), (x, y+1)]
        case "L":
            potential_paths = [(x-1, y), (x, y+1)]
        case "7":
            potential_paths = [(x+1, y), (x, y-1)]
        case "J":
            potential_paths = [(x-1, y), (x, y-1)]
        case _:
            return []
    
    valid_paths = [path for path in potential_paths if path[0] >= 0 and path[1] >= 0]
    return valid_paths

            
def bfs_1(data):
    # useses only valid paths
    visited = set()
    start = (first_S_found(data), 0)
    queue = [start]
    results = []
    while queue:
        #print(queue)
        current = queue.pop(0)
        results.append(current)
        visited.add(current[0])
        for path in return_valid_paths(current[0], data):
            if path not in visited:
                queue.append((path, current[1]+1))
    return results, visited

def first_S_found(data):
    # Returns first char S found in data
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "S":
                return (i, j)
            
def longest_path(data):
    return max(bfs_1(data), key=lambda x: x[1])

# ------------ boring

def sol2(data):
    main_path = bfs_1(data)[1]
    enclosed_set = set()
    for i in range(len(data)):
        enclosed = False
        for j in range(len(data[0])):
            if (i, j) in main_path:
                if enclosed and :
                    enclosed = not enclosed
            elif(enclosed) and (i, j) not in main_path:
                enclosed_set.add((i, j))
    return enclosed_set

print(sol2(test_data))