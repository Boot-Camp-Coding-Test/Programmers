def solution(n):
    fibo = [0, 1]
    
    for i in range(n):    
        fibo = fibo[::-1]
        fibo[1] += fibo[0]
        
    return fibo[0] % 1234567
  
  # memoization
  
  def solution(n, memo={}):
    if n in memo:
        return memo[n]
    elif n < 3:
        return 1
    else:
        value = solution(n - 1, memo) + solution(n - 2, memo)
        memo[n] = value
        
    return memo[n] % 1234567
