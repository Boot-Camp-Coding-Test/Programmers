import re

def summer(new_list,index,summed=0) : 
    
    # new_list 마지막 index 에 도달하면 sum 반환
    if index == len(new_list) - 1 :
        return summed
    
    # 숫자 반환 ex) ('10T') 라면 10 반환 
    pattern = re.compile(r'\d+')
    number = int(pattern.findall(new_list[index])[0])
    if 'S' in new_list[index] : 
        number = number ** 1 # 'S' 가 있으면 1 제곱
    if 'D' in new_list[index] :
        number = number ** 2 # 'D' 가 있으면 2 제곱
    if 'T' in new_list[index] :
        number = number ** 3 # 'T' 가 있으면 3 제곱
    if '#' in new_list[index] :
        number = number * -1 # '#' 이 잇으면 -1 곱하기
    if '*' in new_list[index] :
        number = number * 2 # '*' 가 있으면 2 곱하기
    if '*' in new_list[index+1] :
        number = number * 2 # '*' 가 그 다음 index 에도 있으면 2 곱하기
    summed += number
    return summer(new_list,index+1,summed)

def solution(dartResult):
    answer = 0

    new_list = []
    
    # '1D2S10T*' 를 ['1D', '2S' , '10T*'] 형태로 변환시키기
    pattern = re.compile(r'\d+[A-Z]\*?\#?')
    matches = pattern.finditer(dartResult)
    for match in matches :
        new_list.append(match.group(0))
        
    # 마지막에 랜덤하게 아무거나 append (error 방지용)
    new_list.append('100')
    answer = summer(new_list,index=0,summed=0)

    return answer
