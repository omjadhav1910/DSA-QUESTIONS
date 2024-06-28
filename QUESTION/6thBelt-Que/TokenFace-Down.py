def bagOfTokensScore(tokens, power):
    tokens.sort()
    res = 0
    score = 0
    i = 0
    j = len(tokens) - 1
    
    while i <= j:
        if tokens[i] <= power:
            power -= tokens[i]
            score += 1
            i += 1
            res = max(res, score)
        elif score >= 1:
            power += tokens[j]
            score -= 1
            j -= 1
        else:
            break
    
    return res

# Input handling directly inside the function
n = int(input(""))
tokens = list(map(int, input("").split()))
power = int(input(""))

# Call bagOfTokensScore function and print the result
result = bagOfTokensScore(tokens, power)
print(result)
