def front_x(x):
  x_array = []
  non_x_array = []
  sum_array = []
  for i in x:
    if i.startswith('x'):
      x_array.append(i)
    else:
      non_x_array.append(i)
  x_array.sort()
  non_x_array.sort()
  sum_array.extend(x_array)
  sum_array.extend(non_x_array)
  return sum_array

print front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
print front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
print front_x(['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
