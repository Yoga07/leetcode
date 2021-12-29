def grid_traveller(m, n, memo):
    if (m,n) in memo:
        return memo[(m,n)]

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0
    
    memo[(m,n)] = grid_traveller(m-1, n, memo) + grid_traveller(m, n-1, memo)

    return memo[(m,n)]

memo = {}
print(grid_traveller(1,1, memo)) # 1
print(grid_traveller(2,3, memo)) # 3
print(grid_traveller(3,2, memo)) # 3
print(grid_traveller(18,18, memo)) # 2333606220