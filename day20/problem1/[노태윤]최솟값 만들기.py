def solution(A,B):
    answer = 0
    increasing_sort_list = sorted(A) # 오름차순 정렬
    decreasing_sort_list = sorted(B,reverse=True) # 내림차순 정렬
    for i in range(len(A)) : 
        answer+=increasing_sort_list[i]*decreasing_sort_list[i] # 곱해주고 더하기
    return answer
  
# Key point
  # A 리스트 오름차순 정렬 & B 리스트 내림차순 정렬
  # element 별로 곱해주고 더해주면 최솟값 만들 수 있음
  
  # A 를 내림차순 & B 를 오름차순 정렬 해줘도 상관 없음
