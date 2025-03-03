

def valor_mais_alto_recursivo(arr):
  # caso base
  if len(arr) == 2:
    return arr[0] if arr[0] > arr[1] else arr[1]
  sub_max = valor_mais_alto_recursivo(arr[1:])
  return arr[0] if arr[0] > sub_max else sub_max
    
print(valor_mais_alto_recursivo([3,2,7,9,15]))







