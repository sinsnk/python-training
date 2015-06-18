# -*- coding: utf-8 -*-

def not_bad(s):
  not_index = s.find('not')
  bad_index = s.rfind('bad')
  if bad_index < not_index or not_index < 0 or bad_index < 0:
    return s
  return s.replace(s[s.find('not'):s.rfind('bad') + 3], 'good')

print not_bad('This movie is not so bad')
print not_bad('This dinner is not that bad!')
print not_bad('This tea is not hot')
print not_bad('It`s bad yet not')
