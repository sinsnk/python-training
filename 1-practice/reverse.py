def reverse(s):
  ret = ""
  for i in range(0, len(s)):
    ret += s[-(i+1)]
  return ret

print reverse("hello")
print reverse("good")

orig = raw_input("Type a phrease: ")
result = reverse(orig)
if orig == result:
  print "** palidrome **"
print result
