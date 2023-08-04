def productExceptSelf(nums: list[int]) -> list[int]:
    ans = []

    for i in nums:
        newList = nums.copy()
        newList.remove(i)
        prod = 1
        for n in newList:
            prod = n * prod
        ans.append(prod)

    return ans
            
print(productExceptSelf([1,2,3,4]))