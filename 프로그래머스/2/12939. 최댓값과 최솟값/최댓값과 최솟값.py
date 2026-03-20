def solution(s):
    l = s.split()
    answer = list(map(int, l))
    return f"{min(answer)} {max(answer)}"
    