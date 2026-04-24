def solution(numbers, target):
    answer = [0]
    def dfs(index, current_sum):
        if index == len(numbers):
            if target == current_sum:
                answer[0] += 1
            return
        dfs(index+1, numbers[index]+current_sum)
        dfs(index+1, -numbers[index]+current_sum)
    dfs(0,0)
    return answer[0]