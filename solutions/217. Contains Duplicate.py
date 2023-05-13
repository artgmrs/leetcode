def containsDuplicate(nums: list[int]) -> bool:
    # criar um hashSet com os valores que já foram iterados para evitar duplicidade
    # iterar na lista verificando se o valor se encontra no map, se não tiver eu adiciono no map
    # retorno true se encontrar o valor no map
    # retorno false se depois da iteração nada tiver sido retornado

    hashSet = set()

    for n in nums:
        if n in hashSet:
            return True
        hashSet.add(n)
    return False
          
print(containsDuplicate([3,3]))