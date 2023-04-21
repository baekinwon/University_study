def solution(lottos, win_nums):
    answer = []
    sum = 0
    zero_plus = 0
    if lottos in win_nums:
        answer = [1,1]
    else:
        for i in range(len(win_nums)):
            sum += lottos.count(win_nums[i])
            zero_plus = lottos.count(0)
        count = [sum+zero_plus,sum]
        for i in range(len(count)):
            if count[i] == 6:
                count[i] = 1
            elif count[i] == 5:
                count[i] = 2
            elif count[i] == 4:
                count[i] = 3
            elif count[i] == 3:
                count[i] = 4
            elif count[i] == 2:
                count[i] = 5
            else:
                count[i] = 6
        answer = count
    return answer

print(solution([44, 1, 0, 0, 31, 25]	, [31, 10, 45, 1, 6, 19]))