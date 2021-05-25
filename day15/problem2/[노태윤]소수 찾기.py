from itertools import permutations

def isprime(N) :
    if N <= 1 :
        return False # 0 또는 1 이면 소수가 아니므로 False 반환

    for i in range(2,N) :
        if N % i == 0 :
            return False # 하나라도 나누어 떨어지면 소수가 아니므로 False 반환
    return True # 그 외에는 True 반환 (소수)

def solution(numbers):
    answer = 0
    total_permutations_list = []
    for i in range(1,len(numbers)+1) : # 1부터 numbers 의 length 까지 permutation 진행
        permutations_list = list(permutations(numbers,i))
        total_permutations_list.extend(list(map(lambda x : int("".join(x)),permutations_list))) # [('1','7') , ('1','3')] 이라고 치면 [17,13] 을 전체 permutation list 에 extend
        set_total_permutations_list = set(total_permutations_list) # 중복되는 것이 있을 수도 있으므로 set 로 중복 제거

    for i in set_total_permutations_list :
        if isprime(i) == True : # 소수면 answer +=1
            answer+=1

    return answer
