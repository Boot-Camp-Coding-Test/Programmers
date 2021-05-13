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
