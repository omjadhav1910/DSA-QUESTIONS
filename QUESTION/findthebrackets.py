s = input()
balance = 0
pair ={'(':')','[':']','{':'}'}

for char in s:
    if char in pair:
        balance+=1
    elif char in pair.values():
        balance-=1
        if balance<0:
            print ("false")
            break
else:
    print("true" if balance==0 else "false")