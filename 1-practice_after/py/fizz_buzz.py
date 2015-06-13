class FizzBuzz(object):
  MAX_SIZE = 20
  
  def fb(self,n):
    result = ""
    if n % 3 == 0:
      result += "Fizz"
    if n % 5 == 0:
      result += "Buzz"
    return result

  def __init__(self):
    i = 1
    while i <= self.MAX_SIZE:
      print i, self.fb(i)
      i = i + 1

FizzBuzz()
