#while condition example
a = 1
while a <= 5:
  print('Hello universe')
  a = a + 1

#for example
for i in range (10):
  print('I love Python')  ##prints this 10 times

#another example
for i in range (2, 8):
  print('The current value of i is: ', i)  #print i value for 2,3,4,5,6,7


#another example
for i in range (2, 8, 3):       #range is 2-7 and i = i + 3
  print('The current value of i is: ', i) 

#break example
for i in range(1, 7):
  if( i == 3):
    break
  print('Inside the loop', i)
print('Outside the loop')

#continue example
for i in range(1, 7):
  if( i == 3):
    continue
  print('Inside the loop', i)
print('Outside the loop')

#program to count 0-10
sum = 0
for i in range(11):
  sum = sum + i
print(sum)

#print odd numbers on the screen
for i in range (11):
  if( i%2 == 0 ):
    continue
  else:
    print('Odd number', i)

#using while loop
print('------while loop-----')
i=1
while( i < 11 ):
  if(i % 2 != 0):
    print('odd', i)
  i = i + 1

#print string before @ in an email
for ch in 'pallavilodhi08@gmail.com':
  if(ch == '@'):
    break
  print(ch, end = '')

#program to replace 0 with x
print('---replace example---')
for digit in '23015801606327':
  if(digit == '0'):
    print('x', end = '')
    continue
  print(digit, end = '')
