def numFriendRequests(ages):
    def can_send_request(age1, age2):
        return not (age2 <= 0.5 * age1 + 7 or age2 > age1 or (age2 > 100 and age1 < 100))

    n = len(ages)
    requests = 0

    for i in range(n):
        for j in range(n):
            if i != j and can_send_request(ages[i], ages[j]):
                requests += 1
    
    return requests

# Input handling directly inside the function
n = int(input())
ages = list(map(int, input().split()))
print(numFriendRequests(ages))
