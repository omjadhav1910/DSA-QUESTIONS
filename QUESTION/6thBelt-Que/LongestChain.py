def find_longest_chain(pairs):
    if not pairs:
        return 0
    
    # Sort pairs by the ending value (right value)
    pairs.sort(key=lambda x: x[1])
    
    n = len(pairs)
    dp = [1] * n
    
    for j in range(1, n):
        for i in range(j):
            if pairs[i][1] < pairs[j][0]:  # pairs[i].right < pairs[j].left
                dp[j] = max(dp[j], dp[i] + 1)
    
    return max(dp)

# Input from the user
n = int(input())
pairs = []
for _ in range(n):
    left, right = map(int, input().split())
    pairs.append((left, right))

# Calculate and print the result
result = find_longest_chain(pairs)
print(result)
