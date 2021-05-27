# 정확성 테스트 1 / 3~7 / 9~13
# 효율성 1~5 .. ㅠㅠ

def solution(people, limit):
    answer = 0
    sorted_people = sorted(people,reverse=True)
    while sorted_people :
        if len(sorted_people) >= 2 :
            if sorted_people[0] + sorted_people[1] > limit :
                del sorted_people[0]
                answer+=1
            elif sorted_people[0] + sorted_people[1] <= limit :
                del sorted_people[0:2]
                answer+=1
        else :
            del sorted_people[0]
            answer+=1

    return answer
