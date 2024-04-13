s = input()

compressed_str = " "
count = 1

for i in range(1,len(s)):
  if s[i]==s[i-1]:
    count+=1
  else:
    if count==1:
      compressed_str+=s[i-1]
    else:
      compressed_str+= s[i-1] + str(count)
    count =1

if count==1:
  compressed_str+=s[-1]
else:
  compressed_str+= s[-1] + str(count)

print(compressed_str)