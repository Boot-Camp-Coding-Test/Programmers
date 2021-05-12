def check_dist(pos_from, pos_to):
    num_diff = abs(pos_from - pos_to)
    if num_diff%3 == 0 :
        return num_diff/3
    elif num_diff%3 == 1 :
        return int(num_diff/3)+1
    else :
        return int(num_diff/3)+2

def solution(numbers, hand):
    left_pos = 10
    right_pos = 12
    answer = []
    
    for num in numbers :
        if num in [1, 4, 7] :
            answer.append('L')
            left_pos = num
            
        elif num in [3, 6, 9] :
            answer.append('R')
            right_pos = num
        
        else :
            if num == 0:
                num = 11
            l_dist = check_dist(left_pos, num)
            r_dist = check_dist(right_pos, num)
            print('l:', l_dist, 'r:', r_dist)
            if l_dist == r_dist :
                if hand == 'left':
                    answer.append('L')
                    left_pos = num
                else :
                    answer.append('R')
                    right_pos = num
                # answer.append(hand[0].upper())
            elif l_dist < r_dist :
                answer.append('L')
                left_pos = num
            else :
                answer.append('R')
                right_pos = num
                
    answer = ''.join(answer)
    return answer
