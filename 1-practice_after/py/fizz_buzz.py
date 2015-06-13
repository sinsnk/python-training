class FizzBuzz(object):
  (FIZZ,BUZZ,) = (3, 5)
  MAX_SIZE = 20
  
  def fb(self,n):
    result = ""
    if n % self.FIZZ == 0:
      result += "Fizz"
    if n % self.BUZZ == 0:
      result += "Buzz"
    return result

  def __init__(self):
    i = 1
    while i <= self.MAX_SIZE:
      print i, self.fb(i)
      i = i + 1

FizzBuzz()
