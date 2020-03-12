#functions example
def message():
  print('Hey how you doing')
message()

#function with arg example
def hello(name):
  print('Hello dear, ', name)

n = input('Enter your name: ')
hello(n)

#parameterized function
def display(num):
  for i in range (num):
    print('Hello World')

display(5)

#more than one params
def sum(a, b, c):
  c = a + b + c
  return c
s = sum(1, 2, 3)
print('sum=', s)