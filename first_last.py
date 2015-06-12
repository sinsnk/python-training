def first_last(s):
  if len(s) <= 1:
    ret = ""
  else:
    ret = s[0:2] + s[-2:]
  return ret

print first_last("spring")
print first_last("hello")
print first_last("a")
print first_last("abc")
#s1 = "spring"
#s2 = s1[0] + s1[1] + s1[4] + s1[5]
#print s2
#s2 = s1[0] + s1[1] + s1[-2] + s1[-1]
#print s2
#s2 = s1[0:2] + s1[4:6]
#print s2
#s2 = s1[0:2] + s1[-2:]
#print s2
