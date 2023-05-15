def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # anagrama basta usar o sort e verificar se são iguais
    # criar hashMap com key = sorted(str) e adicionar on array dele cada opção que seja anagrama
    # retornar o values 
    
    groupedAnagrams = {}

    for i in range(len(strs)):
        key = "".join(sorted(strs[i]))
        string = strs[i]
        if key not in groupedAnagrams:
            groupedAnagrams[key] = [string]
        else:
            groupedAnagrams[key].append(string)
            
    return groupedAnagrams.values()

print(groupAnagrams(["a"]))