def count_subarrays_with_max_in_range(nums, left, right):
    def count_subarrays_less_equal(nums, threshold):
        count = 0
        current_count = 0
        for num in nums:
            if num <= threshold:
                current_count += 1
                count += current_count
            else:
                current_count = 0
        return count

    total_subarrays = count_subarrays_less_equal(nums, right)
    subarrays_less_than_left = count_subarrays_less_equal(nums, left - 1)
    return total_subarrays - subarrays_less_than_left

# Input from the user
n = int(input(""))
left, right = map(int, input("").split())
nums = list(map(int, input("").split()))

result = count_subarrays_with_max_in_range(nums, left, right)
print (result)
