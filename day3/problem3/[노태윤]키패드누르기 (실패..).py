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
