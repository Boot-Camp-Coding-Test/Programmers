def solution(n):
    sorted_list = sorted(list(str(n)),reverse=True)
    answer= int("".join(sorted_list))
    return answer
  
# Key Points
# ['5' , '2' , '1', '3'] 이렇게 string 형태가 담긴 리스트에도 sorted() / sort() 가 적용됨 ㅎㄷㄷ 
