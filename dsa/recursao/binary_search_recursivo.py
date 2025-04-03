def pesquisa(arr, needle):
  if len(arr) == 1:
    return True if arr[0] == needle else False
  
  high = len(arr) - 1
  low = 0
  middlePos = (low + high) // 2
  middleValue = arr[middlePos]

  if middleValue == needle:
    return True
  elif middleValue > needle:
    high = middlePos - 1
  else:
    low = middlePos + 1
    
  return pesquisa(arr[low:high+1], needle)

items = [1,3,6,7,9]

print(pesquisa(items, 10))