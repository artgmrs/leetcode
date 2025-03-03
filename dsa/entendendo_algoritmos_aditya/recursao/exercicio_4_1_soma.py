


def soma_recursiva(arr):
  if len(arr) == 0:
    return 0
  return arr[0] + soma_recursiva(arr[1:])

print(soma_recursiva([1, 2, 3, 4, 5])) # 15