def solution(numbers, hand):
    answer = ''
    location = {1:[1,1],
        2:[1,2],
        3:[1,3],
        4:[2,1],
        5:[2,2],
        6:[2,3],
        7:[3,1],
        8:[3,2],
        9:[3,3],
        0:[4,2],
        'L':[4,1],
        'R':[4,3]}

    result = str()
    hand = hand
    for i in numbers:
        if location[i][-1] == 1:
            result += 'L'
            location['L'] = location[i]

        elif location[i][-1] == 3:
            result += 'R'
            location['R'] = location[i]

        else :
            dist_from_loc_L = sum([abs(a-b) for a,b in zip(location['L'], location[i])])
            dist_from_loc_R = sum([abs(a-b) for a,b in zip(location['R'], location[i])])

            if dist_from_loc_L == dist_from_loc_R:
                result += hand[0].upper()
                location[hand[0].upper()] = location[i]
            elif dist_from_loc_L < dist_from_loc_R:
                result += 'L'
                location['L'] = location[i]
            else:
                result += 'R'
                location['R'] = location[i]
    answer = result    
    return answer
