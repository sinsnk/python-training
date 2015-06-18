def remove_adjacent(li):
  tmp = -1 
  i = 0
  for j in li:
    if i == 0:
      tmp = j
      i = i + 1
    if tmp == j:
      li.pop(i)
    tmp = j
    i = i + 1
  return li



print remove_adjacent([1,2,2,3])
print remove_adjacent([2,2,3,3,3])
print remove_adjacent([])
