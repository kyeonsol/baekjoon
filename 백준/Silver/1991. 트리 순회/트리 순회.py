import sys
input = sys.stdin.readline
s = dict()
result = []
n = int(input())

#이진 트리 만들기
for i in range(n): 
    root, left, right = input().split()
    s[root] = [left, right]

#전위 순회 (자기 자신, left, right)
def preorder(root):
    print(root, end='')
    if s[root][0] != '.':
        preorder(s[root][0])
    if s[root][1] != '.':
        preorder(s[root][1])

#중위 순회 (left 자기 자신 right)
def inorder(root):
    if s[root][0] != '.':
        inorder(s[root][0])
    print(root, end='')
    if s[root][1] != '.':
        inorder(s[root][1])
    
#후위 순회 (left right 자기 자신)
def postorder(root):
    if s[root][0] != '.':
        postorder(s[root][0])
    if s[root][1] != '.':
        postorder(s[root][1])
    print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')