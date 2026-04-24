def solution(a, b):
    A = str(a)
    B = str(b)
    sum1 = A + B
    sum2 = B + A
    if int(sum1) > int(sum2):
        return int(sum1)
    else:
        return int(sum2)
    