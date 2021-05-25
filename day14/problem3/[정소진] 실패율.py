def solution(N, stages):

    last_stage = {key: 0 for key in range(1, N + 2)}

    for stage in stages:
        if stage in last_stage:
            last_stage[stage] += 1

    failure_late = {key: 0 for key in range(1, N + 1)}

    def calc_failure_late(failure_late, N, start = 1):
        if start == N + 1:
            return failure_late
        try:
            failure_late[start] = last_stage[start] / sum([last_stage[i] for i in range(start, N + 2) ])
        except:
            if last_stage[start] == 0:
                    failure_late[start] == 0
            else:
                failure_late[start] = last_stage[start] / last_stage[start]
        return calc_failure_late(failure_late, N, start + 1)
    
    calc_failure_late(failure_late, N, 1)

    result = sorted(failure_late, key = lambda x : -failure_late[x])

    return result
