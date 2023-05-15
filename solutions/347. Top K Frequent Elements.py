def topKFrequent(nums: list[int], k: int) -> list[int]:
  # crio um dict para ter as contas de cada número
  # ordeno o dict por valor, em ordem descrescente
  # retorno apenas as k posições do dict ordenado
  output = {}
  for i in nums:
    output[i] = 1 + output.get(i, 0)
  result = dict(sorted(output.items(), key=lambda x:x[1],  reverse=True))
  return list(result)[:k]

print(topKFrequent([4,1,-1,2,-1,2,3], 2))