# 15-拼圖 (15-Puzzle)
# 演算法分析機測
# 學號: 11020117 / 11020126 / 11020134
# 姓名: 林子皓 / 鄭祐昀 / 呂宗凱
# 中原大學電機資訊學士班
from heapq import heappush, heappop

def manhattan_distance(puzzle, goal, size):
    distance = 0
    for i in range(size):
        for j in range(size):
            if puzzle[i][j] and puzzle[i][j] != goal[i][j]:
                x, y = divmod(puzzle[i][j] - 1, size)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    size = len(state)
    flat_state = [num for row in state for num in row]
    zero_index = flat_state.index(0)
    i, j = divmod(zero_index, size)
    neighbors = []
    moves = []
    
    if i > 0:  # Up
        neighbors.append(swap(state, i, j, i - 1, j))
        moves.append('D')  # In the move list 'D' indicates the blank moves down (tile above moves up)
    if i < size - 1:  # Down
        neighbors.append(swap(state, i, j, i + 1, j))
        moves.append('U')  # 'U' indicates the blank moves up (tile below moves down)
    if j > 0:  # Left
        neighbors.append(swap(state, i, j, i, j - 1))
        moves.append('R')  # 'R' indicates the blank moves right (tile to the left moves left)
    if j < size - 1:  # Right
        neighbors.append(swap(state, i, j, i, j + 1))
        moves.append('L')  # 'L' indicates the blank moves left (tile to the right moves right)
    
    return neighbors, moves

def swap(state, i1, j1, i2, j2):
    new_state = [list(row) for row in state]
    new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
    return new_state

def solve_puzzle(start, goal):
    size = len(start)
    pq = []
    heappush(pq, (manhattan_distance(start, goal, size), 0, start, []))  # (cost, moves, state, path)
    visited = set()

    while pq:
        cost, moves, current, path = heappop(pq)
        if current == goal:
            return path
        if tuple(tuple(row) for row in current) in visited:
            continue
        visited.add(tuple(tuple(row) for row in current))
        
        neighbors, moves_direction = get_neighbors(current)
        for i, neighbor in enumerate(neighbors):
            if tuple(tuple(row) for row in neighbor) not in visited:
                new_cost = moves + 1 + manhattan_distance(neighbor, goal, size)
                heappush(pq, (new_cost, moves + 1, neighbor, path + [moves_direction[i]]))
    
    return None  

def add_numbers_to_moves(start_state, moves):
    size = len(start_state)
    state = {start_state[i][j]: (i, j) for i in range(size) for j in range(size)}
    numbered_moves = []
    for move in moves:
        zero_i, zero_j = state[0]
        if move == 'L':
            tile = start_state[zero_i][zero_j + 1]
            state[0], state[tile] = state[tile], state[0]
        elif move == 'R':
            tile = start_state[zero_i][zero_j - 1]
            state[0], state[tile] = state[tile], state[0]
        elif move == 'U':
            tile = start_state[zero_i + 1][zero_j]
            state[0], state[tile] = state[tile], state[0]
        elif move == 'D':
            tile = start_state[zero_i - 1][zero_j]
            state[0], state[tile] = state[tile], state[0]
        numbered_moves.append(f"{tile}{move}")
    return numbered_moves

# Define the goal state of the 15-Puzzle
goal_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

def get_puzzle_configurations(num_puzzles):
    puzzle_configurations = []
    for i in range(num_puzzles):
        puzzle = []
        for _ in range(4):
            row = input().split()
            row = [int(num) for num in row]
            puzzle.append(row)
        puzzle_configurations.append(puzzle)
    return puzzle_configurations

num_puzzles = int(input())
start_states = get_puzzle_configurations(num_puzzles)


# Solve the puzzles
solutions = []
for index, start_state in enumerate(start_states, 1):
    solution = solve_puzzle(start_state, goal_state)
    if solution is not None:
        solutions.append((index, len(solution), solution))

# Format the output with numbers
output_str = []
for solution in solutions:
    index, moves, path = solution
    start_state = start_states[index - 1]
    numbered_path = add_numbers_to_moves(start_state, path)
    
    output_str.append(f"15-Puzzle #{index}")
    output_str.append(f"Number of moves = {moves}")
    # Split the path into chunks of 5 moves for printing
    for chunk in [numbered_path[i:i + 5] for i in range(0, len(numbered_path), 5)]:
        output_str.append(' '.join(chunk))

# Join the output for display
output_str = '\n'.join(output_str)
print(output_str)