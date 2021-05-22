import numpy as np

def solution(arr1, arr2):
    answer = np.sum([arr1, arr2], axis=0)
    return answer.tolist()
