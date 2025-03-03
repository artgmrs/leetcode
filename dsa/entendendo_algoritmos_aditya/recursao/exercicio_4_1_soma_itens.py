
def soma_itens_recursiva(arr):
  if len(arr) == 0:
    return 0
  return 1 + soma_itens_recursiva(arr[1:])

print(soma_itens_recursiva([1, 2, 3, 4, 5])) # 5