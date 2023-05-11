# usar sort para deixar os valores em ordem alfabética, aí só é necessário comparar o primeiro e último
# usar min() para iterar o tamanho exato do menor array, evitando null pointer
# criar var ans para ir preenchendo o prefixo de acordo com que vai encontrando cada letra

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
  ans = ""
  strs = sorted(strs)
  first = strs[0]
  last = strs[len(strs) - 1]
  for i in range(min(len(first),len(last))):
    if first[i] != last[i]:
      return ans
    ans += first[i]
  return ans

# print(longestCommonPrefix(["flower","flow","flight"]))
# print(longestCommonPrefix(["dog","racecar","car"]))
# print(longestCommonPrefix(["", "b"]))
# print(longestCommonPrefix(["a"]))
print(longestCommonPrefix(["a", "ab"]))
# print(longestCommonPrefix(["flower","flower","flower","flower"]))