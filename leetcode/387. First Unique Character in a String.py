# Hashmaps são usados quando precisamos contabilizar a quantidade de alguma coisa
# no python usar o d.get(key) pra obter o valor e o d.items() pra obter a key e o value, dentro do for
def firstUniqChar(s: str) -> int:
    d = {}

    for i, ch in enumerate(s):
        if not d.get(ch):
            d[ch] = [i, 1]
        else:
            d[ch][1] += 1

    for key, value in d.items():
        if value[1] == 1:
            return value[0]
    
    return -1

a = "leetcode"
b = "loveleetcode"
c = "aabb"
print(firstUniqChar(c))