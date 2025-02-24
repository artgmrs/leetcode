def binary_tree(items, needle):
  high = len(items) - 1
  low = 0

  while low <= high:
    middle = (high + low) // 2
    middleValue = items[middle]

    if middleValue == needle:
      return True
    elif middleValue > needle:
      high = middle - 1
    else:
      low = middle + 1

  return False

items = [1,3,6,7,9]

print(binary_tree(items, 20))