def canSum(targetSum, numbers, memo) -> bool:
    ops = []

    if targetSum == 0:
        return True

    if targetSum <= 0:
        return False

    for number in numbers:
        iter = targetSum - number
        res = canSum(iter, numbers)
        ops.append(res)

    if True in ops:
        return True
    else: 
        return False

memo = {}
print(canSum(8, [2, 3, 5], memo)) # True
print(canSum(7, [2, 3], memo)) # True
print(canSum(7, [5, 4, 3 ,7], memo)) # True
print(canSum(7, [2, 4], memo)) # False
print(canSum(300, [7, 14], memo)) # False