# ponteiros alto e baixo
# enquanto o ponteiro baixo for menor ou igual ao ponteiro alto
# se o valor do meio for igual ao esperado, retornar ele
# senao, se o valor do meio for menor que o esperado, alterar o ponteiro baixo para meio + 1
# senao, se o valor do meio for maior que o esperado, alterar o ponteiro alto para meio - 1
# retornar false

# O(log n)
def binary_tree(items, needle):
  lowPointer, highPointer = 0, len(items) - 1

  while lowPointer <= highPointer:
    middlePosition = (lowPointer + highPointer) // 2
    middleValue = items[middlePosition]

    if middleValue == needle:
      return True
  
    elif middleValue < needle:
      lowPointer = middlePosition + 1

    else:
      highPointer = middlePosition - 1

  return False

items = [1,3,6,7,9]

print(binary_tree(items, 3))