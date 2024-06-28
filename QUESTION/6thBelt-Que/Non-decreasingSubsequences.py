def find_subsequences(nums):
    def backtrack(start, path):
        if len(path) > 1:
            subsequences.add(tuple(path))
        
        for i in range(start, len(nums)):
            if not path or nums[i] >= path[-1]:
                backtrack(i + 1, path + [nums[i]])
    
    subsequences = set()
    backtrack(0, [])
    
    return sorted(subsequences)

# Input from the user
n = int(input(""))
nums = list(map(int, input("").split()))

# Find all non-decreasing subsequences with at least two elements
result = find_subsequences(nums)

# Print the result
for subsequence in result:
    print(" ".join(map(str, subsequence)))
