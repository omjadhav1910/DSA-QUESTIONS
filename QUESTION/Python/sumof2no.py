# Use print() to print to the console
# Use print() to print to the console

size1 = int(input())

a = input()
b = a.split()
arr1 = [int(term) for term in b]

size2 = int(input())

a = input()
b = a.split()
arr2 = [int(term) for term in b]

if size2 > size1:
  bigger = arr2
  smaller = arr1
  biggerSize = size2
  smallerSize = size1
else:
  bigger = arr1
  smaller = arr2
  biggerSize = size1
  smallerSize = size2

for i in range(smallerSize,biggerSize):
  smaller.insert(0,0)

# print(smaller)
# print(bigger)

finalArr = []
carry = 0

for i in range(biggerSize-1,-1,-1):
  # print(i,carry)
  sumC = smaller[i] + bigger[i] + carry
  # print("sumc",sumC)
  if sumC >= 10:
    carry = 1
  else:
    carry = 0
  finalArr.insert(0,sumC%10)



if carry == 1:
  print(1,end=" ")


for el in finalArr:
  print(el,end=" ")