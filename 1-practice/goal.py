def goal(count):
  if count >= 10:
    count = "many"
  ret = "Number of goals: " + str(count)
  return ret

print goal(4)
print goal(9)
print goal(10)
print goal(99)
