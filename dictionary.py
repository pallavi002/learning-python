dict = {'cat': 'meow', 'dog': 'bhow', 'cow': 'moo'}

for key in dict.keys():
  print(key, '-->', dict[key])

dict['cat'] = 'NA'
print(dict)

a = {
  'raigad': 'alibag',
  'Navi Mumbai': 'Nerul',
  'M P': 'Bhopal'
}
print(a)
b = a.copy()
print(b)