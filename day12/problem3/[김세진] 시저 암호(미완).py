def solution(s, n):
    a = [] #원래 문자열 넣을 리스트
    b = [] #바꾼 문자열 넣을 리스트
    
    for i in s: #문자열의 문자들을 리스트에 넣어줌
        a.append(i)

    for j in range(len(a)):
      # ord() : 문자를 아스키코드로 반환
      # chr() : 아스키코드를 문자로 반환
        if a[j] == 'z': #문자가 z일 경우 a+(n-1)를 출력
            b.append(chr(96+n))
        elif a[j] == 'Z': #문자가 Z일 경우 A+(n-1)를 출력
            b.append(chr(64+n))
        elif a[j] == ' ': #공백인 경우 공백 출력
            b.append(' ')
        else: #z가 아닌 경우 아스키코드에 n 더해줌
            code = ord(a[j]) + n
            b.append(chr(code))

    b = ''.join(b)
    
    return b


# 입출력 예시만 통과하고 나머지는 케이스 하나만 통과했다.
# z와 Z일 때 조건만 생각하고, n이 아주 클때의 경우는 간과해서 그런 것 같다.
# 머리가 안돌아가서.. 이건 이대로 놔두고 다음에 다시 생각해 봐야겠다 ㅠㅠ
