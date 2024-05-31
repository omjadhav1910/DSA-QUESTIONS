def subArray(arr, n):
    for i in range(0, n):
        for j in range(i, n):
            for k in range(i, j+1):
                print(arr[k], end=" ")
            print("\n", end="")


n = int(input("  "))
arr = list(map(int, input("  ").split()))
subArray(arr, n)
