def difference(A, B):
    i = 0
    j = 1
    n = len(A)
    
    while i < n and j < n:
        if i != j and A[j] - A[i] == B:
            return 1
        elif A[j] - A[i] < B:
            j += 1
        else:
            i += 1
    
    return 0
    
N = int(input(" "))
A = list(map(int, input(" ").split()))
B = int(input(" "))

print(difference(A, B))
