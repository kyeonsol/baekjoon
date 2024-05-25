def solution(pn):
    answer = ''
    answer += '*'*(len(pn)-4)
    answer += pn[-4:]
    return answer