
# O(n²)
def ordenacaoPorSelecao(arr):
  arrCopy = arr.copy()
  orderedArray = []

  for i in range(len(arr)):
    lowest = arrCopy[0]
    lowest_indice = 0

    for j in range(1, len(arrCopy)):
      if arrCopy[j] < lowest:
        lowest = arrCopy[j]
        lowest_indice = j
    orderedArray.append(arrCopy.pop(lowest_indice));

  print(orderedArray)

print(ordenacaoPorSelecao([5,3,6,2,10]))