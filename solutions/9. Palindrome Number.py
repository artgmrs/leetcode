# dá pra usar s[::-1] ou list(str(x)) + reverse(), o slice é mais demorado

def isPalindrome(x: int) -> bool:
    stringList = list(str(x))
    stringList.reverse()

    return "".join(stringList) == str(x)

print(isPalindrome(121))