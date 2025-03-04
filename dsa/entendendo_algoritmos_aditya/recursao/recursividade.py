# Uma função recursiva deve possuir um caso base e um caso recursivo
# A falta do caso base faz a função ser executada em loop infinito 

def fat(x):
  if x == 1:
    return 1
  
  return x * fat(x-1)

print(fat(5))