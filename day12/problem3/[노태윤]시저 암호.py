from string import ascii_lowercase,ascii_uppercase
# ascii_lowercase ==> 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase ==> 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def lower_uppercase(character,n,if_lowercase) :
    if if_lowercase == True :
        index = ascii_lowercase.index(character) # 만약 lowercase 라면 ascii_lowercase 에서 해당 문자의 index 값 반환
    else :
        index = ascii_uppercase.index(character) # 만약 uppercase 라면 ascii_uppercase 에서 해당 문자의 index 값 반환
    for i in range(n) :
        index+=1
        if index >= 26 :
            index-=26 # 만약 26을 넘어가면 -26 해줄 것 (알파벳이 26개 있기 때문)
    return index

def solution(s, n):
    answer = ''
    for i in s :
        if i == ' ' :
            answer+=' ' # empty space 면 똑같이 empty space 반환
            continue
        if i.islower() :
            index = lower_uppercase(i,n,if_lowercase=True) # lowercase 일 때 위치 이동후의 index 값 반환
            answer+=ascii_lowercase[index] # answer 에 이동 후의 문자 더하기
        else :
            index = lower_uppercase(i,n,if_lowercase=False) # uppercase 일 때 위치 이동후의 index 값 반환
            answer+=ascii_uppercase[index] # answer 에 이동 후의 문자 
    return answer
