
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
def quicksort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivo = arr[len(arr) // 2]
    menores = [i for i in arr if i < pivo]
    iguais = [i for i in arr if i == pivo]
    maiores = [i for i in arr if i > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)

itens = [3,3,5,2,1,4]
print("Mais otimizado", quicksort(itens)) # Saída esperada: Mais otimizado [1, 2, 3, 3, 4, 5]