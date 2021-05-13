def solution(answers):
    answer = []
    
    a = []
    b = []
    c = []
    # 정답을 찍은 패턴에 맞게 10000문제 까지 채워주기
    while len(a) <= 10000:
        for i in [1,2,3,4,5]:
            a.append(i)   
        for i in [2,1,2,3,2,4,2,5]:
            b.append(i)
        for i in [3,3,1,1,2,2,4,4,5,5]:
            c.append(i)
    
    # 들어온 정답과 리스트의 길이 맞춰주기
    a = a[:len(answers)]
    b = b[:len(answers)]
    c = c[:len(answers)]
    
    # 세명의 정답지와 실제 정답을 비교해서 각 점수를 담은 리스트 생성 
    scores = []
    for each in [a,b,c]:
        count = 0
        for i,j in zip(each, answers):
            if i == j:
                count += 1
        scores.append(count)

    # 리스트 안에서 최대값을 찾고 최대값과 같은 사람을 찾음
    maxval = max(scores)
    for i in range(len(scores)):
        if scores[i] == maxval:
            answer.append(i + 1)
        
    return answer

### 통과는 됐지만 코드가 개판인거 같다 하하호홓 ###
