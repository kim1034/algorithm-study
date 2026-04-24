def solution(nums):
    answer = set(nums)
    if len(answer) < len(nums)/2:
        return len(answer)
    else:
        return len(nums)/2
        