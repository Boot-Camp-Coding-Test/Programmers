def solution(s):
    answer = ''
    ascii_list = []
    for i in s :
      
        # ascii 숫자로 변환 후 ascii_list 에 append
        ascii_list.append(ord(i))
    zipped_list = list(zip(s,ascii_list)) # 's' 와 'ascii_list' 합치기
    sorted_zipped_list = sorted(zipped_list,key=lambda x:x[1],reverse=True) # ascii 숫자를 기준으로 내림차순 정렬 
    for i in sorted_zipped_list :
        answer+=i[0] # 정렬된 string 담기
    return answer
