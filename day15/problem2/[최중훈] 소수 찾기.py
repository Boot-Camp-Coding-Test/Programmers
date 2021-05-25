from itertools import permutations

def solution(s):
    # 문자열 길이가 1이면 바로 소수인지 확인하고 return
    if len(s) == 1:
        if (int(s) == 2) or (int(s) % 2 != 0):
            return 1
        else:
            return 0
    # 문자열 길이 != 1
    else:    
        lst = [i for i in s]
        n = len(s)
        permu_lst = []
        for i in range(1, n+1):
            permu_lst.append(list(permutations(lst, i))) # permutations 사용해서 중복값을 허용하는 모든 경우의 수 찾기

        num_lst = []
        for arr in permu_lst:
            for tup in arr:
                num = int(''.join(tup)) # perrmutations로 구한 튜플 -> 정수 변환
                if num not in num_lst: # 중복값이 매우 많기 때문에 담아서 set하는 거보다 애초에 확인하고 담는게 더 빠름
                    num_lst.append(num)
        
        # print(num_lst)
        # print(len(num_lst))
        
        answer = []
        for num in num_lst: # 조합가능한 모든 경우의 수 중에서 소수인 것 찾기
            count = 0 # 소수인지 확인을 위한 count, 나누어 떨어지는 수가 있으면 +1
            sqrt = int(num ** (1/2)) # 2,10이 시간초과 뜸.. 해결책 >>> 주어진 수의 제곱근 이하까지만 나누어보아도 소수인지 확인 가능함!
            if num != 0 and num != 1:
                for denominator in range(2, sqrt + 1):
                    if num % denominator == 0:
                        count += 1
                if count == 0: # 2부터 제곱근(num)이하의 수로 나누어 떨어지는게 없으면 소수임
                    answer.append(num)
        
        # print(answer)
        # print(len(answer))

        return len(answer)
