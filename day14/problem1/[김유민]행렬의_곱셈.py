def solution(arr1, arr2):
    answer = [[] for i in range(len(arr1))]

    new_arr2= [[] for i in range(len(arr2[0]))]
    for row in arr2:
        for i in range(len(arr2[0])) :
            new_arr2[i].append(row[i])
    print(new_arr2)

    for i1, row1 in enumerate(arr1) :
        for row2 in new_arr2 :
            num = 0
            for j in range(len(row1)) :
                num += row1[j] * row2[j]
            answer[i1].append(num)
    
    return answer
