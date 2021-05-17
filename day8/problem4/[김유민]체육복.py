def solution(n, lost, reserve):
    num_clothes = [1]*n

    #여벌 체육복 적용
    for i in reserve :
        num_clothes[i-1] += 1
    
    #체육복 분실 적용
    for i in lost :
        num_clothes[i-1] -= 1

    print(num_clothes)
    #체육복 대여 적용
    for i in range(n) :
        if num_clothes[i] == 0 :
            if (num_clothes[i-1] == 2) and (i != 0) :
                num_clothes[i-1] -= 1
                num_clothes[i] += 1

            elif i != n-1 :
                if num_clothes[i+1] == 2 :
                    num_clothes[i+1] -= 1
                    num_clothes[i] += 1

    
    return n - num_clothes.count(0)
