def binary_search(arr, target, lo, hi):
    while lo < hi:
        mid = int((lo+hi)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid+1
        else:
            hi = mid
    return -1

# tem que estar ordenado
# verifica inicialmente qual o sub-array que o número buscado pode estar
# exponential é mais rápida que o binary_search em casos que a probabilidade do target estar no começo é maior
def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    
    i = 1

    while i < len(arr) and arr[i] < target:
        i *= 2

    if i < len(arr) and arr[i] == target:
        return i
    
    return binary_search(arr, target, i//2, min(i, len(arr) -1 ))


arr = [1,2,3,4,5,6,7,8,9,10]
result = exponential_search(arr, 12)
print(f"Target found at position {result}")  