import sys

pat = sys.argv[1]
try:
  f = open(sys.argv[2], 'rU')
except IOError:
  print >> sys.stderr, "Error: open file"
  sys.exit(1)

for i in f.readlines():
  found = i.lower().find(pat)
  if found > -1:
    convert = i[found:len(pat)]
    print i.replace(convert, "***"+convert+"***")
f.close()
