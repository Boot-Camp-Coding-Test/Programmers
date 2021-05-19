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
