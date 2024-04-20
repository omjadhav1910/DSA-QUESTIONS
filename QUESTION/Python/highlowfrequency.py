s = input()
obj = {}
for i in s:
    if i in obj:
        obj[i] = obj[i] + 1
    elif (i!= " " and i != "!"):
        obj[i] = 1
max_freq = max(obj.values())
min_freq = min(obj.values())

max_chars = [char for char, freq in obj.items() if freq == max_freq]
min_chars = [char for char, freq in obj.items() if freq == min_freq]

max_chars.sort()
min_chars.sort()
print("Highest frequency character(s): ",''.join(max_chars), max_freq)
print("Lowest frequency character(s): ",' '.join(min_chars),min_freq)