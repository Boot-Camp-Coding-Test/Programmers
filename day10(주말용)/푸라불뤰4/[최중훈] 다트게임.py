def solution(dartResult):
    answer = []
    sdt = {'S': 1, 'D': 2, 'T': 3}
    n = 0 # 문자열 리스트의 시작을 0으로 설정해주고 점수(숫자)가 아닐 경우 해당 인덱스부터 다시 시작하도록 설정해주면서 리스트를 살펴봄

    for i, j in enumerate(dartResult): 
        # 숫자가 시작하는 인덱스부터 sdt 딕셔너리값과 일치하는 인덱스까지 자른 다음 각각에 맞게 연산해 줌
        if j in sdt:
            answer.append(int(dartResult[n:i])**sdt[j]) 
        # 점수가 담긴 리스트에서 뒤에서 두개의 점수를 2배 해 줌. 첫번째 점수더라도 뒤에서부터 찾으면 인덱스 에러가 나지 않기 때문에 가능
        if j == '*':
            answer[-2:] = [x*2 for x in answer[-2:]]
        # 점수가 담긴 리스트에서 해당 점수에 -1을 곱해줌
        if j == '#':
            answer[-1] = answer[-1] * -1
        # 문자열이 점수가 아니라면 +1 씩해주면서 인덱스를 맞춰나감
        if not j.isdigit():
            n = i + 1

    return sum(answer)
