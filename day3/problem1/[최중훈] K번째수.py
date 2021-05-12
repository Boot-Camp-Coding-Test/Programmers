def solution(array, commands):

    result = []
    for lst in commands:
        cut =  array[lst[0]-1:lst[1]]
        cut.sort()
        result.append(cut[lst[2]-1])
    
    return result
