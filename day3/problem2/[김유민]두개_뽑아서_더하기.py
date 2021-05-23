# 반복문 사용
def solution1(numbers):
    answer = []
    for i in range(len(numbers)) :
        for j in range(i+1, len(numbers)) :
            num_sum = numbers[i] + numbers[j]
            if num_sum not in answer :
                answer.append(num_sum)
    return sorted(answer)

# 컴프리헨션
def solution2(numbers):
    answer = [numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(i+1, len(numbers))]
    answer = list(set(answer))
    return sorted(answer)
