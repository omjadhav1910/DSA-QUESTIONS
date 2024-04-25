n = int(input())
main = []

for i in range(n):
    arr = list(map(int, input().split()))
    main.append(arr)

stack = []

for el in main:
    if el[0] == 1:
        stack.append(el[1])
    elif el[0] == 2:
        if stack:
            print(stack.pop(), end=" ")
        else:
            print("-1", end=" ")
    elif el[0] == 3:
        if stack:
            print(max(stack), end=" ")
        else:
            print("-1", end=" ")
# Design a stack that supports push, pop, top, and retrieving the maximum element in constant time.