# 테스트 11 / 13~20 실패

import numpy as np

def find_length(a,b) : 
    dx = abs(b[0]-a[0])
    dy = abs(b[1]-a[1])
    return (dx**2 + dy**2) / 2

def solution(numbers,hand) : 
    answer=''
    phone_list = []
    a,b,c = 1,2,3
    for i in range(3) :
        phone_list.append([10,a,b,c])
        a+=3
        b+=3
        c+=3
    phone_list.insert(0,[10,10,10,10])
    phone_list.append([10,'*',0,'#'])
    phone_array = np.array(phone_list)

    left_coordinates = np.where(phone_array=='*')
    left_coord_list = [int(left_coordinates[0]),int(left_coordinates[1])]

    right_coordinates = np.where(phone_array=='#')
    right_coord_list = [int(right_coordinates[0]),int(right_coordinates[1])]

    for i in numbers : 
        if str(i) in ['1','4','7'] :
            answer+='L'
            left_coordinates = np.where(phone_array==str(i))
            left_coord_list = [int(left_coordinates[0]),int(left_coordinates[1])]
        elif str(i) in ['3','6','9'] :
            answer+='R'
            right_coordinates = np.where(phone_array==str(i))
            right_coord_list = [int(right_coordinates[0]),int(right_coordinates[1])]
        else :
            center_coordinates = np.where(phone_array==str(i))
            center_coord_list = [int(center_coordinates[0]),int(center_coordinates[1])]
            left_length = find_length(left_coord_list,center_coord_list)
            right_length = find_length(right_coord_list,center_coord_list)

            if left_length < right_length :
                answer+='L'
                left_coordinates = np.where(phone_array==str(i))
                left_coord_list = [int(left_coordinates[0]),int(left_coordinates[1])]
            
            elif left_length > right_length :
                answer+='R'
                right_coordinates = np.where(phone_array==str(i))
                right_coord_list = [int(right_coordinates[0]),int(right_coordinates[1])]
            
            if left_length == right_length :
                if hand.startswith('r') :
                    answer+='R'
                else :
                    answer+='L'

    return answer

# ==============================================================================================
# 재도전

# numpy 불러온 이유는 좌표값 받아오기 위해서
# np.where()
import numpy as np

# 거리 구하는 함수
def find_length(a,b) : 
    dx = abs(b[0]-a[0])
    dy = abs(b[1]-a[1])
    return dx+dy

def solution(numbers,hand) : 
    answer=''
    phone_list = []
    a,b,c = 1,2,3
    
    # 키패드 완성시키기
    # array([['10', '10', '10', '10'],
    #   ['10', '1', '2', '3'],
    #   ['10', '4', '5', '6'],
    #   ['10', '7', '8', '9'],
    #   ['10', '*', '0', '#']], dtype='<U21')
    
    # 이런 식으로 출력이 됨 ('*','#' 이 포함되어 있기 때문에 숫자열도 있지만 전체적으로 문자열이 된다)
    # numpy 특징(?) 인 것 같음
    for i in range(3) :
        phone_list.append([10,a,b,c])
        a+=3
        b+=3
        c+=3
    phone_list.insert(0,[10,10,10,10])
    phone_list.append([10,'*',0,'#'])
    phone_array = np.array(phone_list)

    # 초기 좌표값 지정해주기
    # 왼손은 '*' 에서 시작 / 좌표값 : (4,1)
    # 오른손은 '#' 에서 시작 / 좌표값 : (4,3)
    left_coordinates = np.where(phone_array=='*')
    left_coord_list = [int(left_coordinates[0]),int(left_coordinates[1])]
    # left_coordinates : (array([4]), array([1])
    # left_coord_list : [4,1]

    right_coordinates = np.where(phone_array=='#')
    right_coord_list = [int(right_coordinates[0]),int(right_coordinates[1])]
    # left_coordinates : (array([4]), array([3])
    # left_coord_list : [4,3]
    
    for i in numbers : 
        
        # 1,4,7 중 하나면 'L' append
        # 왼손 좌표값 업데이트
        if str(i) in ['1','4','7'] :
            answer+='L'
            left_coordinates = np.where(phone_array==str(i))
            left_coord_list = [int(left_coordinates[0]),int(left_coordinates[1])]
            
        # 3,6,9 중 하나면 'R' append
        # 오른손 좌표값 업데이트
        elif str(i) in ['3','6','9'] :
            answer+='R'
            right_coordinates = np.where(phone_array==str(i))
            right_coord_list = [int(right_coordinates[0]),int(right_coordinates[1])]
        
        # 나머지 2,5,8,0 이면 아래 실행
        else :
            
            # 중앙 좌표값 구하고 현재 왼손 & 현재 오른손 좌표값과의 거리 비교
            center_coordinates = np.where(phone_array==str(i))
            center_coord_list = [int(center_coordinates[0]),int(center_coordinates[1])]
            left_length = find_length(left_coord_list,center_coord_list)
            right_length = find_length(right_coord_list,center_coord_list)

            # 왼손 거리가 더 짧으면 아래 실행
            if left_length < right_length :
                answer+='L'
                left_coordinates = np.where(phone_array==str(i))
                left_coord_list = [int(left_coordinates[0]),int(left_coordinates[1])]
            
            # 오른손 거리가 더 짧으면 아래 실행
            elif left_length > right_length :
                answer+='R'
                right_coordinates = np.where(phone_array==str(i))
                right_coord_list = [int(right_coordinates[0]),int(right_coordinates[1])]
            
            # 왼손 거리 == 오른손 거리 이면 아래 실행
            elif left_length == right_length :
                if hand.startswith('r') :
                    answer+='R'
                    right_coordinates = np.where(phone_array==str(i))
                    right_coord_list = [int(right_coordinates[0]),int(right_coordinates[1])]
                else :
                    answer+='L'
                    left_coordinates = np.where(phone_array==str(i))
                    left_coord_list = [int(left_coordinates[0]),int(left_coordinates[1])]

    return answer

# Key Points
    # 문제를 잘 읽어보자....
    # 처음에는 거리라고 해서 당연히 삼각형으로 비유하자면 대각선 길이를 구하는 건 줄 알았다
    # 문제 설명에 '엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다' 라고 적혀 있음
    # 대각선 길이가 아니라 밑변과 높이의 합을 구하라는 의미 였음...
