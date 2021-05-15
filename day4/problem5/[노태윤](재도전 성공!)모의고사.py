# 1/ 5~14 런타임 에러

def solution(answers):
    answer = []
    
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]

    a_divided = len(answer)//len(a)
    b_divided = len(answer)//len(b)
    c_divided = len(answer)//len(c)

    a.extend(a_divided*a)
    b.extend(b_divided*b)
    c.extend(c_divided*c)

    new_dict = {
        1:0,
        2:0,
        3:0
    }

    for i in range(len(answers)):
        if answers[i] == a[i] :
            new_dict[1]+=1
        if answers[i] == b[i] :
            new_dict[2]+=1
        if answers[i] == c[i] :
            new_dict[3]+=1
        
    sorted_set_in_list = sorted(new_dict.items(), key=lambda x: x[1],reverse=True)
    
    for i in range(len(sorted_set_in_list)) :
        if i == 0 :
            answer.append(sorted_set_in_list[i][0])
        else :
            if sorted_set_in_list[1][1] < sorted_set_in_list[0][1] :
                break
            elif sorted_set_in_list[i][1] == sorted_set_in_list[i-1][1] :
                answer.append(sorted_set_in_list[i][0])
                
    answer = sorted(answer)

    return answer

# =======================================================================================
# 재도전

def solution(answers):
    answer = []
    
    # 패턴 리스트로 담기
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]

    # 길이 조절
    a_divided = len(answers)//len(a)
    b_divided = len(answers)//len(b)
    c_divided = len(answers)//len(c)

    a.extend(a_divided*a)
    b.extend(b_divided*b)
    c.extend(c_divided*c)

    new_dict = {
        1:0,
        2:0,
        3:0
    }

    # answers 에 담긴 숫자 == 패턴 이면 아래 실행
    for i in range(len(answers)):
        if a[i] == answers[i]  :
            new_dict[1]+=1
        if b[i] == answers[i] :
            new_dict[2]+=1
        if c[i] == answers[i] :
            new_dict[3]+=1
    
    # max 값에 해당하는 key 값 리스트로 담고 오름차순 정렬
    answer = sorted([a[0] for a in new_dict.items() if a[1]==max(new_dict.values())])

    return answer

# Key Points
    # 처음에는 
    '''
    for i in range(len(answers)):
        if answers[i] == a[i] :
            new_dict[1]+=1
        if answers[i] == b[i] :
            new_dict[2]+=1
        if answers[i] == c[i] :
            new_dict[3]+=1
    '''
    # 이렇게 풀었음
    
    # 이러면 if 문 중 하나라도 True 면 if 문 실행하고 다시 for loop 돌게 됨
    
    '''
    for i in range(len(answers)):
        if a[i] == answers[i]  :
            new_dict[1]+=1
        if b[i] == answers[i] :
            new_dict[2]+=1
        if c[i] == answers[i] :
            new_dict[3]+=1
    '''
    # 이렇게 반대로 작성해야 함!
