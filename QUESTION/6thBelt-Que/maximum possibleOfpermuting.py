def maxGreatness(nums):
    n = len(nums)
    
    # Sort nums to get sorted_nums
    sorted_nums = sorted(nums)
    
    # Sort nums in descending order to maximize greatness
    sorted_perm = sorted(nums, reverse=True)
    
    # Two-pointer approach to find maximum possible greatness
    max_greatness = 0
    j = n - 1
    for i in range(n):
        while j >= 0 and sorted_perm[j] <= sorted_nums[i]:
            j -= 1
        if j >= 0:
            max_greatness += 1
            j -= 1
    
    return max_greatness

# Example usage
n=int(input())
nums = [int(x) for x in input().split()]
print(maxGreatness(nums))
