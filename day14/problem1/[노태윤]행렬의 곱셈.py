import numpy as np

def solution(arr1, arr2):
    answer = np.dot(np.array(arr1),np.array(arr2)).tolist()
    return answer

# numpy 안쓰고 한번 풀어볼 것
