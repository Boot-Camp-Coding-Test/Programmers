def solution(s, n):
    no_case_answer = ''
    s_lst = [x for x in s]
    tmp_case_lst = []
    for char in s_lst:
        tmp_case_lst.append(char.isupper())
        char = char.lower()
        if char.isspace():
            no_case_answer += char
        else:
            asci_num = ord(char) + n
            if asci_num > 122:
                asci_num = asci_num - 26
                no_case_answer += chr(asci_num)
            else:
                no_case_answer += chr(asci_num)

    answer = ''
    for i in range(len(tmp_case_lst)):
        if tmp_case_lst[i] == True:
            answer += no_case_answer[i].upper()
        else:
            answer += no_case_answer[i].lower()
        
    return answer
