def solution(dartResult):
    answer=[]
    s=''
    for i in range(len(dartResult)):
        if dartResult[i].isdecimal() :
            if s==1 and int(dartResult[i])==0:
                s=10
            else :
                if type(s)==int:
                    answer.append(s) 
                s = int(dartResult[i])
                
        else :
            if dartResult[i]=='S':
                s **= 1
            elif dartResult[i]=='D':
                s **= 2
            elif dartResult[i]=='T':
                s **= 3
            elif dartResult[i]=='*':
                if len(answer)==0:
                    s*=2
                else :
                    s*=2
                    answer[-1]*=2
            elif dartResult[i]=='#':
                s*=-1
            
            if i==len(dartResult)-1:
                answer.append(s)
            
    return sum(answer)


