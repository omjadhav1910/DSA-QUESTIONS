n,d = map(int,input().split())

arr = list(map(int,input().split()))

rotated_arr = arr[-d:] + arr[:-d]

print(*rotated_arr)