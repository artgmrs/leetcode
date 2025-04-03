def binary_search(nums, n):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = int((lo+hi)/2)
        if nums[mid] == n:
            return True
        elif nums[mid] < n:
            lo = mid+1
        else:
            hi = mid
    return False

a = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(a, 4))

def binary_search_menor_ou_igual(nums, n):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = int((lo+hi)/2)
        if nums[mid] == n:
            return True
        elif nums[mid] < n:
            lo = mid+1
        else:
            hi = mid-1
    return False