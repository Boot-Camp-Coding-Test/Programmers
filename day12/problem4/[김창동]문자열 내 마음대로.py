def solution(strings, n):
    initial = [str_[n] for str_ in strings]     # 인덱스 글자 추출
    dict_, list_ = {}, []
    
    for i in range(len(strings)):
        if initial[i] in dict_.keys():          # 이니셜이 중복될때
            dict_[initial[i]].append(strings[i])# chaining 개념
        else:
            dict_[initial[i]] = [strings[i]]    # 중복처리를 위한 [값] 저장
    
    for i in sorted(dict_.items()):
        i[1].sort()
        list_.append(i[1])
    
    return sum(list_, [])   # 2차원 => 1차원
