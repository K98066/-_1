# 水桶謎題 (Water Jug Puzzle)
# 演算法分析機測
# 學號: 11020117 / 11020126 / 11020134
# 姓名: 林子皓 / 鄭祐昀 / 呂宗凱
# 中原大學電機資訊學士班
from collections import deque

def water_bucket_solver(capacity_a, capacity_b, target):
    # The states are tuples of (amount_a, amount_b)
    start_state = (0, 0)
    visited = set()  # to keep track of visited states
    queue = deque()  # to perform BFS

    # Parent dictionary to store the solution path
    parent = {start_state: (None, None)}

    # Each action is a function that takes the current state and returns the new state
    def fill_a(state): return (capacity_a, state[1])
    # def fill_b(state): return (state[0], capacity_b)
    def empty_a(state): return (0, state[1])
    def empty_b(state): return (state[0], 0)
    def pour_a_to_b(state):
        transfer = min(state[0], capacity_b - state[1])
        return (state[0] - transfer, state[1] + transfer)
    def pour_b_to_a(state):
        transfer = min(state[1], capacity_a - state[0])
        return (state[0] + transfer, state[1] - transfer)
    
    # Actions are stored with their corresponding functions and the text representation
    actions = {
        fill_a: "Fill A",
        # fill_b: "Fill B",
        empty_a: "Empty A",
        empty_b: "Empty B",
        pour_a_to_b: "Pour A B",
        pour_b_to_a: "Pour B A",
    }

    queue.append(start_state)
    visited.add(start_state)

    # Perform BFS
    while queue:
        current_state = queue.popleft()
        
        # Check if we reached the target
        if current_state[1] == target:
            break
        
        # Try all possible actions
        for action, action_text in actions.items():
            next_state = action(current_state)
            if next_state not in visited:
                queue.append(next_state)
                visited.add(next_state)
                parent[next_state] = (current_state, action_text)

    # Backtrack to find the solution
    solution = deque()
    state = current_state
    while parent[state][0] is not None:
        solution.appendleft(parent[state][1])
        state = parent[state][0]

    solution.append("Success")
    return list(solution)

# Prompt for inputs until "0 0 0" is entered
capacities_and_targets = []
while True:
    input_str = input()
    a, b, t = map(int, input_str.split())
    if a == 0 and b == 0 and t == 0:
        break
    capacities_and_targets.append((a, b, t))

# Solve for each input
solutions = [water_bucket_solver(a, b, t) for (a, b, t) in capacities_and_targets]

# Print the solutions
for i, solution in enumerate(solutions, start=1):
    print(f"{solution}")
