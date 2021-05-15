import numpy as np

def solution(arr):
    # numpy array 로 바꾸기
    numpy_array = np.array(arr)
    
    # np.mean 활용
    mean_value = np.mean(numpy_array)
    
    # 만약 소수점 자리 끝이 '0' 이면 int 형으로 변환
    if str(mean_value)[-1] == '0':
        answer = int(mean_value)
        
    # 나머지는 그냥 float 형으로 반환
    else :
        answer = mean_value
        
    return answer
