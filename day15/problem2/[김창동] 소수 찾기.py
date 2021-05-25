from itertools import permutations

def solution(numbers):
    l, li = [], []

    for i in range(len(numbers)):   # 부분집합 추출
        l.append(list(permutations(numbers, i+1)))

    for i in sum(l, []):    # [(1, 2, 3), (2, 1, 3)] => [123, 213]
        a = ''
        for j in i:
            a += str(j)
        li.append(int(a))

    cnt = 0
    for i in list(set(li)): # 중복값 제거
          if is_prime(i):
            cnt += 1

    return cnt
    


def is_prime(n):
    if n >= 2:
        for i in range(2, n):
            if not (n % i):
                return False
              
    else:  # 0 & 1, 음수인 상황을 가정
        return False
    return True
