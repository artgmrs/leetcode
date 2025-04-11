# sliding window
#- normalmente usado pra resolver problemas que tenham como resultado sub arrays ou tamanho de sub-array ou sub string
#- while r++ while l++ (expandir com o R e retrair com o L)
#- cada vez que expandir, adicionar ou aumentar o contador
#- cada vez que retrair, retirar o character que vai sair do contador
#- como 


def maximumLengthSubstring(s: str):
    l, r = 0, 0
    _max = 1
    counter = {}

    counter[s[0]] = 1

    while r < len(s) - 1:
        r += 1
        if counter.get(s[r]):
            counter[s[r]] += 1
        else:
            counter[s[r]] = 1
        while counter[s[r]] == 3:
            counter[s[l]] -= 1
            l += 1
        _max = max(_max, r-l+1)
    
    return _max

a = "bcbbbcba"
print(maximumLengthSubstring(a))