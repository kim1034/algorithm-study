def solution(my_string):
    answer = ''
    i = len(my_string) - 1
    while i >= 0:
        answer += my_string[i]
        i -= 1
    return answer