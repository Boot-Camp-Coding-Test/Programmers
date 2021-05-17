def solution(n, lost, reserve):
    answer = 0

    # 초기 리스트 설정
    training_list = [1 for i in range(n+2)]
    training_list[0] = 100
    training_list[-1] = 100
    

    for i in range(n+2) : 
        
        # reserve 에 있으면 2 로 설정
        if i in reserve : 
            training_list[i] = 2
        
        # lost 에 있으면 -1 (결국 체육복 없으면 0으로 잡힘)
        if i in lost : 
            training_list[i] -= 1

    # 첫번째 사람부터 마지막 사람까지
    for i in range(1, len(training_list)-1) :
      
        # 만약에 체육복이 없다면 아래 코드 진행
        if training_list[i] == 0 :
          
            # 왼쪽 사람 여분 있으면 아래 코드 진행
            if training_list[i-1] == 2 :
                training_list[i-1]-=1
                training_list[i]+=1
                continue
            
            # 오른쪽 사람 여분 있으면 아래 코드 진행
            if training_list[i+1] == 2 :
                training_list[i+1]-=1
                training_list[i]+=1

    # summing
    for i in range(1,len(training_list)-1) : 
        
        # 2 이더라도 1 증가
        if training_list[i]==2 : 
            answer+=1
        
        # 1 이면 1 증가
        elif training_list[i]==1:
            answer+=1
        else :
            continue

    return answer
