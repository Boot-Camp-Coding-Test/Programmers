def solution(numbers):
    answer = []
    print(numbers)
    # 0~ 끝까지
    # 1부터 끝까지
    for i in range(len(numbers)):
      if i != len(numbers)-1:
        for j in range(i+1, len(numbers)):
          if numbers[i] + numbers[j] not in answer:
            answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer
