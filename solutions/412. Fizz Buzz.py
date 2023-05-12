# iniciar array com ans = [] e adicoinar nele com append
# usar mod (%) para verificar se é divisível

def fizzBuzz(n: int) -> list[str]:
  ans = []
  for i in range(1, n + 1):
      if i % 3 == 0 and i % 5 == 0:
          ans.append("FizzBuzz")
      elif i % 3 == 0:
          ans.append("Fizz")
      elif i % 5 == 0:
          ans.append("Buzz")
      else:
          ans.append(str(i))
  return ans

print(fizzBuzz(3))