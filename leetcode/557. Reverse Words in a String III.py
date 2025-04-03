# Como nao dá pra manipular string em python, tem que ir concatenando numa string nova as palavras invertidas

def reverse_array(s: str):
  res = ''
  l, r = 0,0

  while r < len(s):
    if s[r] != ' ':
      r += 1
    else:
      res += s[l:r+1][::-1]
      r += 1
      l = r

  res += ' '
  res += s[l:r+2][::-1]
  return res[1:]
  
s = "Let's take LeetCode contest" # "s'teL ekat edoCteeL tsetnoc"
print(reverse_array(s))