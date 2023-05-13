def isAnagram(s: str, t: str) -> bool:
    # return sorted(s) == sorted(t)

    # comparar len das duas
    # criar hashMap com a contagem de cada um dos caracteres
    # comparar a contagem dos dois e retornar false para a primeira que for falsa
      # usar dict.get(key, default) para evitar KeyError

    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
        
    return True

print(isAnagram("anagram", "nagaram"))