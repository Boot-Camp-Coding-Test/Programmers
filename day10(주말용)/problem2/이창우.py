def solution(absolutes, signs):
    answer = 0
    for ab, si in zip(absolutes,signs):
        answer += ab if si else -ab
    return answer
