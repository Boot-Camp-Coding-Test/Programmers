def solution(numbers, hand):
    answer, left, right = '', [1, 4], [3, 4]    # 시작위치
    
    for n in numbers:
        loc = find_loc(n) # 위치 찾기
        if n in [1, 4, 7]:
            value = 'L'
        elif n in [3, 6, 9]:
            value = 'R'
        else:
            value = comparison(left, right, loc)  # 2, 5, 8, 0
        
        if not value:       # 양손의 거리가 같아 0을 반환 받았을때
            value = hand[0].upper()
        
        if value == 'L':    # 엄지의 위치변경
            left = loc
        else:
            right = loc
        
        answer += value
    return answer
  

def find_loc(n):        # 번호의 위치파악
    height = 0
    key = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ['*', 0, '#']
      ]
    
    for line in key:
        height += 1     # 높이 추적
        
        if n in line:   # 해당 높이의 라인에 값이 있을때
            width = line.index(n) + 1
            return [width, height]

        
        
def comparison(left, right, loc):    # 절댓값을 통한 거리비교
    left_distance = abs(loc[0] - left[0]) + abs(loc[1] - left[1])
    right_distance = abs(loc[0] - right[0]) + abs(loc[1] - right[1])

    if left_distance < right_distance:
        return 'L'
    elif left_distance > right_distance:
        return 'R'
    else:
        return 0
