import sys

try:
  f = open(sys.argv[1], 'rU')
except:
  pass

str = f.readlines()
str.reverse()
for line in str:
  line = line.replace('\n','')
  print line
f.close()
