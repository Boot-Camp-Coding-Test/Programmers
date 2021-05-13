#더 효율적인 코드 고민해보기..
def compare(a, b):
    if a==b :
        return 1
    else :
        return 0

def solution(answers):
    num_correct = [0]*3
    options_1 = [1, 2, 3, 4, 5]
    options_2 = [1, 3, 4, 5]
    options_3 = [3, 1, 2, 4, 5]

    # ans_1 = [options[i%5] if (i%5 != 0) else 5 for i in range(1, len(answers)+1)]
    ans_1 = [options_1[i%5] for i in range(len(answers))]
    ans_2 = [options_2[int(i/2)%4] if (i%2 != 0) else 2 for i in range(len(answers))]
    ans_3 = [options_3[int(i/2)%5] for i in range(len(answers))]

    for i in range(len(answers)) :
        num_correct[0] += compare(ans_1[i], answers[i])
        num_correct[1] += compare(ans_2[i], answers[i])
        num_correct[2] += compare(ans_3[i], answers[i])

    result = []
    max_correct = max(num_correct)
    for i in range(len(num_correct)) :
        if num_correct[i] == max_correct :
            result.append(i+1)

    return result
