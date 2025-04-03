
# By the Book (pode ser O(n²) por pegar o pivo do inicio)
# O pior cenario acontece quando o array ja esta ordenado
# Mas caso medio ainda e O(n log n)
def quicksort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivo = arr[0]
    menores = [i for i in arr[1:] if i <= pivo]
    maiores = [i for i in arr[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

itens = [3,5,2,1,4]
print("By The Book", quicksort(itens)) # Saída esperada: By The Book [1, 2, 3, 4, 5]

# O(n log n)
# Pegando pivo do meio para evitar pior cenario
# Retirando iguais ao pivo da recursividade para evitar loop infinito
def quicksort2(arr):
  if len(arr) < 2:
    return arr
  else:
    pivo = arr[len(arr) // 2]
    menores = [i for i in arr if i < pivo]
    iguais = [i for i in arr if i == pivo]
    maiores = [i for i in arr if i > pivo]
    return quicksort2(menores) + iguais + quicksort2(maiores)

itens = [3,3,5,2,1,4]
print("Mais otimizado", quicksort2(itens)) # Saída esperada: Mais otimizado [1, 2, 3, 3, 4, 5]

# O ?
# Sem usar list comprehension e alterando a lista em si

def start_quicksort3(arr):
  quicksort3(arr, 0, len(arr) - 1);
  return arr

def quicksort3(arr, left, right):
  if left < right:
    pivo = partition(arr, left, right)
    quicksort3(arr, left, pivo - 1) # esquerda do pivot
    quicksort3(arr, pivo + 1 , right) # direita do pivot

def partition(arr, left, right):
  pivo = arr[right]
  i = left - 1

  for j in range(left, right):
    if arr[j] <= pivo:
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i+1], arr[right] = arr[right], arr[i+1] # Achou o lugar do pivo
  return i+1

itens = [3,3,5,2,1,4]
print("Usando partition", start_quicksort3(itens))