# https://www.youtube.com/watch?v=KLlXCFG5TnA
# criar um hash map das iterações que já foram feitas
# iterar sobre o array nums usando enumerate()
# a cada iteração, procurar pelo valor faltante no array (só funciona pois se tem certeza que o valor está lá)

def twoSum(nums: list[int], target: int) -> list[int]:
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
            
print(twoSum([2,7,11,15], 9))