def solution(n, arr1, arr2):
    result = []
    
    for a, b in zip(arr1, arr2): 
        a = bin(a)[2:].zfill(n) # 이진변환, 뒤 0채워넣기
        b = bin(b)[2:].zfill(n)
        hash_ = ''
        
        for x, y in zip(a, b):  # 한개씩 잘라 값 집어넣기
            x, y = int(x), int(y) 
            if x == y == 0:     # 둘다 0일때 제외 모두 #
                hash_ += ' '
            else:
                hash_ += '#'
        
        result.append(hash_)
    return result
