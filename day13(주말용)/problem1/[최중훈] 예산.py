def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    else:
        answer = 0
        all_dept = list(sorted(d))
        print(all_dept)
        for i in all_dept:
            if budget >= i:
                answer += 1
                budget -= i
            else:
                break

        return answer
