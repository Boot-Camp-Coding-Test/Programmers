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
