# 二元樹密碼 (Binary Tree Secret Code)
# 演算法分析機測
# 學號: 11020117 / 11020126 / 11020134
# 姓名: 林子皓 / 鄭祐昀 / 呂宗凱
# 中原大學電機資訊學士班
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    # The first element of preorder is always the root node.
    root_value = preorder[0]
    root = TreeNode(root_value)
    
    # Find the index of the root in inorder to split the left and right subtrees.
    root_index = inorder.index(root_value)
    
    # Recursively build the left and right subtrees.
    root.left = build_tree(preorder[1:1+root_index], inorder[:root_index])
    root.right = build_tree(preorder[1+root_index:], inorder[root_index+1:])
    
    return root

def postorder_traversal(node):
    return postorder_traversal(node.left) + postorder_traversal(node.right) + [node.value] if node else []

# Create a TreeNode class to represent nodes of the binary tree.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Input strings for preorder and inorder traversals
preorder_inputs = []
inorder_inputs = []

# Loop to accept inputs until "0" is entered
while True:
    preorder_input = input()
    if preorder_input == "0":
        break
    inorder_input = input()
    preorder_inputs.append(preorder_input)
    inorder_inputs.append(inorder_input)

# Build trees from the traversals
trees = []
for preorder, inorder in zip(preorder_inputs, inorder_inputs):
    tree = build_tree(preorder, inorder)
    trees.append(tree)

# Generate postorder traversal for each tree
decoded_messages = []
for tree in trees:
    decoded_message = ''.join(postorder_traversal(tree))
    decoded_messages.append(decoded_message)

for message in decoded_messages:
    print(message)

