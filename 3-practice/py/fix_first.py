def fix_first(s):
  ret = s[0] + s[1:].replace(s[0], '*')
  return ret

print fix_first("babbel")
print fix_first("google")
print fix_first("apple")
print fix_first("orange")
