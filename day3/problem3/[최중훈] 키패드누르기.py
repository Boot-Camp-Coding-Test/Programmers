def solution(numbers, hand):
    # 키패드를 좌표 형태의 배열로 생각
    arr = [
           [0,0], [0,1], [0,2],
           [1,0], [1,1], [1,2],
           [2,0], [2,1], [2,2],
           [3,0], [3,1], [3,2]
    ]

    # 인자로 받은 numbers를 좌표 형태 배열이 담긴 리스트로 생성
    arr_num = []
    for idx, number in enumerate(numbers):
        if number == 0:
            arr_num.append(arr[10])
        else:
            arr_num.append(arr[number-1])

    # 최초 손가락의 위치(left:*, right:#)
    left_before = arr[9]
    right_before = arr[11]
    
    answer = ''
    
    for i, j in enumerate(arr_num):
        # 왼손으로 눌러야만 하는 경우 1 4 7
        if j in [arr[0], arr[3], arr[6]]:
            answer += 'L'
            left_before = arr_num[i]
        
        # 오른손으로 눌러야만 하는 경우 3 6 9
        elif j in [arr[2], arr[5], arr[8]]:
            answer += 'R'
            right_before = arr_num[i]
        
        # 둘중에 더 가까운 손으로 누르는 경우 2 5 8 0
        else:            
            # 계속 테스트 통과에 실패해서 질문 게시판을 봤더니.. 문제를 내가 제대로 안 읽은게 문제였다.
            # 문제를 잘 읽도록 하자!
            # 루트고 제곱이고 뭐고 하지말고 한칸에 1임 걍 절대값 취해서 거리를 계산해야 했음
            left_distance = abs(left_before[0]-j[0]) + abs(left_before[1]-j[1])
            right_distance = abs(right_before[0]-j[0]) + abs(right_before[1]-j[1])
            
            # 계산된 거리를 바탕으로 어느 손을 사용할 지 확인
            if left_distance < right_distance:
                answer += 'L'
                left_before = arr_num[i]

            elif left_distance > right_distance:
                answer += 'R'
                right_before = arr_num[i]

            else:
                answer += hand[0].upper()
                if answer.endswith('L'):
                    left_before = arr_num[i]
                if answer.endswith('R'):
                    right_before = arr_num[i]        

    return answer
