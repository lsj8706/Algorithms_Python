# 이진트리 순회 (깊이우선탐색)

tree = [1,2,3,4,5,6,7]

# 중위순회 출력 (왼, 본인, 오른)
def inOrder(tree, len, index):
    if index < len:
        inOrder(tree, len, 2*index + 1)
        print(tree[index], end=' ')
        inOrder(tree, len, 2*index + 2)
    else:
        return

# 전위순회 출력 (본인, 왼, 오른)
def preOrder(tree, len, index):
    if index < len:
        print(tree[index], end=' ')
        preOrder(tree, len, 2*index + 1)
        preOrder(tree, len, 2*index + 2)
    else:
        return

# 후위순회 출력 (왼, 오른, 본인)
def postOrder(tree, len, index):
    if index < len:
        postOrder(tree, len, 2*index + 1)
        postOrder(tree, len, 2*index + 2)
        print(tree[index], end=' ')
    else:
        return

print("전위순회 출력 : ", end='')
preOrder(tree, len(tree), 0)
print()
print("중위순회 출력 : ", end='')
inOrder(tree, len(tree), 0)
print()
print("후위순회 출력 : ", end='')
postOrder(tree, len(tree), 0)