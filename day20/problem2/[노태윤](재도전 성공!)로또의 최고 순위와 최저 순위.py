# test 14 실패

def solution(lottos, win_nums):
    answer = []
    common_number_counts = len(set(lottos) & set(win_nums))
    zero_counts = lottos.count(0)
    answer.append(7-(common_number_counts + zero_counts))
    if common_number_counts <= 1 :
        answer.append(6)
    else :
        answer.append(7-common_number_counts)
    return answer

# ===============================================================
# 재도전

def solution(lottos, win_nums):
    answer = []
    common_number_counts = len(set(lottos) & set(win_nums)) # 로또 번호와 당첨 번호 중 겹치는 숫자들의 길이 반환 -- A 라고 지정
    zero_counts = lottos.count(0) # 로또 번호 중 지워진 부분 (0 인 부분) 길이 반환 -- B 라고 지정
    if common_number_counts == 0 and zero_counts == 0 : 
        answer.append(6) # 만약 A 와 B 가 둘 다 0 이라면 (겹치는 것도 없고 지워진 부분이 없다면 그냥 6 append)
    else :
        answer.append(7-(common_number_counts + zero_counts)) # 그 외 7 - (A+B) append (최고 순위 append)
    if common_number_counts <= 1 :
        answer.append(6) # 만약 A 가 1보다 작다면 그냥 6 append (최소로 겹치는 게 1개 이하면 무조건 6등이라고 명시해 있음)
    else :
        answer.append(7-common_number_counts) # 그 외 7-A append
    return answer

# Key point
    # 로또 번호 & 당첨 번호 중 겹치는 것도 없고 지워진 부분도 없을 때의 예외 케이스를 생각하지 못했다
    # 무조건 일부분이 지워져 있어야 되는 것 아닌가..? 문제를 잘못 읽었나?
