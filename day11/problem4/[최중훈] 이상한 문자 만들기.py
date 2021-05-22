def solution(s):
    answer = ''
    s_lst = s.split(' ')
    print(s_lst)

    for word in s_lst:
        for i in range(len(word)):
                if i % 2 == 0:
                    answer += word[i].upper()
                else:
                    answer += word[i].lower()
        
        answer += ' '

    return answer[:-1]
