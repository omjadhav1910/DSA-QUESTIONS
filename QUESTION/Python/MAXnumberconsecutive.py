def max_consecutive_after_changes(answerKey, k):
    max_length = 0
    left = 0
    change_count = 0

    for right in range(len(answerKey)):
        if answerKey[right] != 'T':   
            change_count += 1
        
        while change_count > k:
            if answerKey[left] != 'T':
                change_count -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)

    return max_length


answerKey = input()
k = int(input())


result = max_consecutive_after_changes(answerKey, k)
print(result)
