# 테스트 5~7 / 11~12 실패

def sorting(sorted_list,starting_index,ending_index) :
    sorted_list[starting_index:ending_index+1] = sorted(sorted_list[starting_index:ending_index+1])
    return sorted_list

def solution(strings, n):
    answer = []
    sorted_list = sorted(strings,key=lambda x : x[n])
    starting_index = 0
    ending_index = 0
    for i in range(1,len(sorted_list)) :
        if sorted_list[i][n] == sorted_list[i-1][n] : 
            ending_index+=1
        else :
            if ending_index - starting_index == 0 :
                starting_index = i
                ending_index = i
                continue
            sorted_list = sorting(sorted_list,starting_index,ending_index)
            starting_index = i
            ending_index = i

    return sorted_list

# ===========================================================================================================
# 재도전

def solution(strings, n):
    ordered_strings = sorted(strings) # 전체적인 sorting
    answer = sorted(ordered_strings,key=lambda x : x[n]) # 인덱스 별 sorting
    return answer

# Key points

# sorted 함수 정렬 과정
    # 왼쪽부터 진행
    
    # Ex)
    # strings =['sun','bed','car','run','gun','bar','bun']
    # sorted(strings,key=lambda x : x[1]) ==> ['car', 'bar', 'bed', 'sun', 'run', 'gun', 'bun']
    
        # 왼쪽부터 1번 index 를 기준으로 오름차순으로 정렬
        # 가장 먼저 'a' 가 포함된 'car' --> 'bar'
        # 그 다음 'e' 가 포함된 'bed' 
        # 그 다음 'u' 가 포함된 (왼쪽부터 차례대로 찾기) 'sun' --> 'run' --> 'gun' --> 'bun'
        
    # 이렇게 되버리면 'car', 'bar' 순서가 맞지 않음 (문제 요구 사항 : index 값에 같은 문자면 사전순으로 정렬)
    # 뒤에 'sun' , 'run' , 'gun' , 'bun' 도 순서가 맞지 않음
    
    # 처음부터 사전순으로 정렬하면 해결됨
    
    # ordered_strings = sorted(strings) ==> ['bar', 'bed', 'bun', 'car', 'gun', 'run', 'sun']
    # sorted(ordered_strings,key=lambda x : x[n]) ==> ['bar', 'car', 'bed', 'bun', 'gun', 'run', 'sun']
    
    # 왼쪽부터 오른쪽으로 순차적으로 검색 후 정렬한다! (key=lambda 쓸때만 그런거 같다)
