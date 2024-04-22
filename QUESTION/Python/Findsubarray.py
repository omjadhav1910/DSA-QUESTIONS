n = int(input())
max_Sum = 0
S = 0
subarray = []
finalarray = []

arr = list(map(int, input().split()))

if n > 0 and arr:
    for i in range(n):
        for j in range(i, n):
            subar = arr[i:j+1]
            subarray.append(subar)

    for el in subarray:
        s = sum(el)
        finalarray.append(s)

    print(max(finalarray))
else:
    print("0")