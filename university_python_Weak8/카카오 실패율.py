def solution(N, stages):
    answer = []
    count = []
    N_us = len(stages)
    for i in range(1,N+1):
        print(count)
        sum = stages.count(i)
        if sum == 0:
            count.append(0)
        else:
            count.append(sum / N_us)
            N_us -= stages.count(i)
    answer = sorted(range(len(count)),key = lambda x : count[x],reverse = True)
    for i in range(len(answer)):
        answer[i]+=1

    return answer
print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))