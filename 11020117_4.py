# 連通元標記 (Connected Component Labeling)
# 演算法分析機測
# 學號: 11020117 / 11020126 / 11020134
# 姓名: 林子皓 / 鄭祐昀 / 呂宗凱
# 中原大學電機資訊學士班
def dfs(matrix, x, y, visited, rows, cols):
    """ Perform DFS to find and label connected components, considering
        8-connectivity (horizontal, vertical, and diagonal connections). """
    if x < 0 or x >= rows or y < 0 or y >= cols or matrix[x][y] == '0' or visited[x][y]:
        return 0
    visited[x][y] = True
    area = 1
    # Check all eight directions (including diagonals)
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        area += dfs(matrix, x+dx, y+dy, visited, rows, cols)
    return area

def connected_components(images):
    """ Find and count connected components in the images using 8-connectivity """
    results = []
    for img in images:
        rows, cols = img[0], img[1]
        matrix = img[2]
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        components = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1' and not visited[i][j]:
                    area = dfs(matrix, i, j, visited, rows, cols)
                    components.append(area)
        results.append(components)
    return results

# Prompt for image inputs until image size is 0x0
inputs = []
while True:
    rows, cols = map(int, input().split())
    if rows == 0 and cols == 0:
        break
    matrix = []
    for _ in range(rows):
        row = input()
        matrix.append(row)
    inputs.append((rows, cols, matrix))

results = connected_components(inputs)

# Prepare the output
output = []
for i, components in enumerate(results, start=1):
    output.append(f"Image #{i}")
    output.append(f"Number of Connected Components = {len(components)}")
    for j, area in enumerate(components, start=1):
        output.append(f"Connected Component #{j} Area = {area}")

# Join the output for display
output_str = '\n'.join(output)
print(output_str)