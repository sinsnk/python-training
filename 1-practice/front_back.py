def front_back(a, b):
  len_middle_a = len(a)/2
  len_middle_b = len(b)/2
  if len(a) % 2 == 0:
    head_a = a[:len_middle_a]
    tail_a = a[len_middle_a:]
  else:
    head_a = a[:len_middle_a+1]
    tail_a = a[len_middle_a+1:]
  if len(b) % 2 == 0:
    head_b = b[:len_middle_b]
    tail_b = b[len_middle_b:]
  else:
    head_b = b[:len_middle_b+1]
    tail_b = b[len_middle_b+1:]
  ret = head_a + head_b + tail_a + tail_b
  return ret

print front_back("abcd","xy")
print front_back("abcde", "xyz")
print front_back("Kitten", "Donut")
