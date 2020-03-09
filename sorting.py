#bubble sort
swapped = True
list = []

a = int(input('Enter the limit of array'))
for i in range (a):
  b = int(input('Enter element'))
  list.append(b)
print(list)

while swapped:
  swapped = False
  for i in range (len(list) - 1):
    if (list[i] > list[i+1]):
      swapped = True
      list[i], list[i+1] = list[i+1], list[i]
print('------sorted array------')
print(list)