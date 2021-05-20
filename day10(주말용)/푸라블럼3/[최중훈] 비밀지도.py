from collections import deque

def get_binary(num):
    lst = []
    for i in range(num):
        lst.append(num % 2)
        num = num // 2
        if num == 0:
            break
        elif num == 1:
            lst.append(num)
            break
            
    return list(reversed(lst))

  
def solution(n, arr1, arr2):
    answer = []
    binary_arr1 = []
    binary_arr2 = []
    for i, j in zip(arr1, arr2):
        binary_arr1.append(get_binary(i))
        binary_arr2.append(get_binary(j))
    # print(binary_arr1)
    # print('====')
    # print(binary_arr2)
    
    for i in range(len(binary_arr1)):
        if len(binary_arr1[i]) != n:
            deq = deque(binary_arr1[i])
            for _ in range(n - len(binary_arr1[i])):
                deq.appendleft(0)
            binary_arr1[i] = list(deq)   

        if len(binary_arr2[i]) != n:
            deq = deque(binary_arr2[i])
            for _ in range(n - len(binary_arr2[i])):
                deq.appendleft(0)
            binary_arr2[i] = list(deq)
    # print(binary_arr1)
    # print('====')
    # print(binary_arr2)

    for i, j in zip(binary_arr1, binary_arr2):
        tmp_str = ''
        for m, n in zip(i, j):
            if m == 0 and n == 0:
                tmp_str += ' '
            else:
                tmp_str += '#'
        answer.append(tmp_str)

    return answer
  
  # ============================코드가 너무 비효율적인 것 같군======================================
