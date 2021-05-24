# 
import re
def solution(dartResult):
    ch= list(re.sub('[0-9]','',dartResult))
    num = re.split("[SDT#*]",dartResult)
    number = [int(i) for i in num if i!='']
    for i in range(len(number)):
        if (i*2)+1 >= len(ch):
            ch.append(' ')
            break
        if ch[(i*2)+1] not in ['*','#']:
            ch.insert((2*i)+1, ' ')
    a,b = [ch[i] for i in range(len(ch)) if i%2==0], [ch[i] for i in range(len(ch)) if i%2==1]
    idx, answer = 0, 0
    for i,j in zip(a,b):
        if idx == 0:
            now = number[idx]
            prior=1
        else:
            now = number[idx]
            prior = number[idx-1]

        if i == 'S':
            now = now
        elif i=='D':
            now = pow(now,2)
        elif i=='T':
            now = pow(now,3)

        if j ==' ':
            answer += now
            idx+=1
        elif j=='#':
            answer += -now
            idx += 1
        elif j=='*':
            answer += now*2+prior
            idx += 1
    print(answer)
    return answer

# solution('1S2D*3T')
# solution('1D2S#10S')
# solution('1D2S0T')
# solution('1S*2T*3S')
solution('1D#2S*3S')
