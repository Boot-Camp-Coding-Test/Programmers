# 1 & 3 런타임 에러

def decimal_to_binary(x,n,binary_string='') :
    if x == 1 and x % 2 == 1 :
        binary_string = '1'+binary_string
        length = n - len(binary_string)
        binary_string = '0' * length + binary_string
        return binary_string
    elif x == 1 and x % 2 == 0 :
        binary_string = '0' + binary_string
        length = n - len(binary_string)
        binary_string = '0' * length + binary_string
        return binary_string
    else :
        if x % 2 == 0 :
            binary_string = '0' + binary_string
            return decimal_to_binary(x//2,n,binary_string)
        else :
            binary_string = '1' + binary_string
            return decimal_to_binary(x//2,n,binary_string)

def solution(n, arr1, arr2):
    answer = []

    arr1_binary = []
    arr2_binary = []
    for i in range(n) : 
        arr1_binary.append(decimal_to_binary(arr1[i],n,binary_string=''))
        arr2_binary.append(decimal_to_binary(arr2[i],n,binary_string=''))

    for i in range(n) :
        new_str = ''
        for j in range(n) :
            if arr1_binary[i][j] == '0' and arr2_binary[i][j]== '0' :
                new_str+=' '
            else :
                new_str+='#'
        answer.append(new_str)
    return answer

# ================================================================================
# 재도전

def decimal_to_binary(x,n,binary_string='') :
    
    # x 가 0 일 때는 주어진 배열 길이만큼 '0' 곱하고 반환
    if x == 0 :
        binary_string = '0' * n
        return binary_string
    
    # 이진수로 바꿀 때 마지막 quotient 값이 1 이고 remainder 가 1 이면 아래 코드 실행
    # 그리고 배열길이 맞춰줘야하므로 나머지 자릿수에는 '0' 넣어주기
    if x == 1 and x % 2 == 1 :
        binary_string = '1'+binary_string
        length = n - len(binary_string)
        binary_string = '0' * length + binary_string
        return binary_string
    
    # 이진수로 바꿀 떄 마지막 quotient 값이 1 이고 remainder 가 0 이면 아래 코드 실행
    # 그리고 배열길이 맞춰줘야하므로 나머지 자릿수에는 '0' 넣어주기
    elif x == 1 and x % 2 == 0 :
        binary_string = '0' + binary_string
        length = n - len(binary_string)
        binary_string = '0' * length + binary_string
        return binary_string
    else :
        
        # 2로 나누어 떨어지면 아래 코드 실행
        if x % 2 == 0 :
            binary_string = '0' + binary_string
            return decimal_to_binary(x//2,n,binary_string)
        
        # 2로 나누어 떨어지지 않으면 아래 코드 실행
        else :
            binary_string = '1' + binary_string
            return decimal_to_binary(x//2,n,binary_string)

def solution(n, arr1, arr2):
    answer = []

    arr1_binary = []
    arr2_binary = []
    # 변환된 이진수 쌓기
    # ex
    # [0, 20, 28, 18, 11] --> ['00000', '10100', '11100', '10010', '01011']
    for i in range(n) : 
        arr1_binary.append(decimal_to_binary(arr1[i],n,binary_string=''))
        arr2_binary.append(decimal_to_binary(arr2[i],n,binary_string=''))

    for i in range(n) :
        new_str = ''
        
        # 두 이진수 array 비교해서 둘 다 '0' 인 곳이 있으면 공백 추가하기
        # '1' 이면 '#' 추가하기
        for j in range(n) :
            if arr1_binary[i][j] == '0' and arr2_binary[i][j]== '0' :
                new_str+=' '
            else :
                new_str+='#'
        answer.append(new_str)
    return answer

# Key Points
# 처음에 0 을 이진수로 변환해줄 때 error 가 발생했었음
# 예외처리 해주니까 제대로 돌아감 

# =========================================================================
# 3차 도전 + 간소화

def solution(n, arr1, arr2):
    answer = []
    for a,b in zip(arr1,arr2) :
        zipped = format(a|b,'b').zfill(n) # or operation 쓰고 2진수로 표현 --> 0 채우기
        zipped = zipped.replace('1','#') # '1' 을 '#' 으로 바꾸기
        zipped = zipped.replace('0',' ') # '0' 을 ' ' 으로 바꾸기
        answer.append(zipped)
    return answer

# Key points
    # int 형끼리 | (or) 또는 $ (and) operation 이 사용가능하다
    
    # ex)
    # 9 & 30 
        # 9 --> 2진수 --> 01001
        # 30 --> 2진수 --> 11110
        
        # and 는 둘이 같을 때만 1, 나머지는 0 반환 --> 01000 --> 10진수 --> 8
    
    # 9 | 30
        # or 는 둘 중 하나라도 1이면 1 반환, 나머지는 0 반환 --> 11111 --> 31
    
    # zfill()
        # '003'.zfill(5) 라고 하면 5 - len('003') 만큼 앞에 '0' 을 추가한다는 의미
        # ==> 00003
