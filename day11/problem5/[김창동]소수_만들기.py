from itertools import combinations

def solution(nums):
    nums = list(combinations(nums,3))
    prime_list = list(map(lambda x: sum(x), nums))
    
    return len([i for i in prime_list if is_prime(i)]) # 소수만 분류

def is_prime(n):
    if n >= 2:
        for i in range(2, n):
            if not (n % i):
                return False
    else:
        return False
    return True
  
 
# 이게 왜 안되는지 모르겠다.
def solution(nums):
    result = []
    
    for x in nums:
        a, b = nums.copy(), nums.copy()
        a.remove(x)
        b.remove(x)
        for y in a:
            b.remove(y)
            for z in b:
                if is_prime(x+y+z):
                    result.append(x+y+z)
    return len(list(set(result)))
