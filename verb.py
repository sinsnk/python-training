def verb_ing(s):
  if len(s) >= 3:
    if s[-3:] == "ing":
      ret = s + "ly"
    else:
      ret = s + "ing"
  elif len(s) <= 2:
    ret = s
  return ret

print verb_ing("hail")
print verb_ing("swimming")
print verb_ing("do")
