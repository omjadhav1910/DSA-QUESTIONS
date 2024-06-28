def beautiful_subsets(nums, k):
    def count_beautiful_subsets(nums, k, start, subset):
        count = 0
        for i in range(start, len(nums)):
            valid = True
            for num in subset:
                if abs(num - nums[i]) == k:
                    valid = False
                    break
            if valid:
                count += 1 + count_beautiful_subsets(nums, k, i + 1, subset + [nums[i]])
        return count

    return count_beautiful_subsets(nums, k, 0, [])

# Input from the user
n, k = map(int, input("").split())

if n == 1:
    print("1")
else:
    nums = list(map(int, input("").split()))
    result = beautiful_subsets(nums, k)
    print(result)
