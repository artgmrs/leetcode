# criar hashmap dos romanos
# verificar sempre a próxima posição, já que o número é lido da esquerda pra direita

input = input('Type the roman number: ')

def romanToInt(s: str) -> int:
    romansMap = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    count = 0

    for i in range(len(s)):
        if i == len(s) - 1:
            count += romansMap[s[i]]
            break

        if romansMap[s[i]] < romansMap[s[i + 1]]:
            count -= romansMap[s[i]]
        else:
            count += romansMap[s[i]]

    print(count)

romanToInt(input)
