a = [2, 4, 6, 8, 10]
#printing length of an array
print(len(a))

#deleting an array element
del a[2]

#print new array
print(a)

#appending a number at the end of array
a.append(12)
print(a)

#adding a number at the particular index
a.insert(1,5)   #it will insert 5 at index 1
print(a)

#copying complete array
b = a[:]
print(b)

#copying some part of array 
c = [1, 5, 2, 9, 12]
b = c[0:3]
print(b)

#negative index
d = c[-1]
print(d)  #prints 12

i = 2
while i>=0:
  print("*")
  i-= 2

for i in range (-1, 1):
  print('#')

print('-------')
nums = []
vals = nums[:]
vals.append(1)
print(vals)
print(nums)

print('-----')
l = [0 for i in range (1, 3 )]
print(l)

print('-----')
lst = [0, 1, 2, 3]
x = l
for elm in lst:
  x *= elm
print(x)