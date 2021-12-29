def fib(n ,memo) -> int:
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fib(n-1, memo) + fib(n-2, memo)

    return memo[n]

memo = {}
print(fib(6, memo)) # 8
print(fib(7, memo)) # 13
print(fib(8, memo)) # 21
print(fib(50, memo)) # 12586269025