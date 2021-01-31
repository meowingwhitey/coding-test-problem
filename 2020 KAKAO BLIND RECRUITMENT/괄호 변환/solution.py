def isBalanced(u):
    right = 0
    left = 0
    for i in range(len(u)):
        if u[i] == '(':
            left = left + 1
        else:
            right = right + 1
    if right == left:
        return True
    else:
        return False
def isCorrect(u):
    stack = 0
    for i in range(len(u)):
        if u[i] == '(':
            stack = stack + 1
        else:
            stack = stack - 1
        if stack < 0:
            return False
    if stack == 0:
        return True
    else:
        return False
def recursive(w):
    if not w:
        return w
    u = []
    v = []
    t = []
    for i in range(1, len(w)):
        u = w[0:i + 1]
        v = w[i + 1:]
        #만약 u가 균형잡힌 괄호 문자열이면 분리
        if isBalanced(u):
            if isCorrect(u):
                u = u + recursive(v)
                return u
            else:
                t.append('(')
                t = t + recursive(v)
                t.append(')')
                del u[0]
                del u[len(u) - 1]
                for i in range(len(u)):
                    if u[i] == ')':
                        u[i] = '('
                    else:
                        u[i] = ')'
                t = t + u
                return t
def solution(p):
    answer = []
    w = p
    #입력이 빈 경우
    if not w:
        #빈 문자열 반환
        return w
    if isCorrect(w):
        return ''.join(w)
    #문자열->리스트 변환
    w = list(w)
    answer = recursive(w)
    return ''.join(answer)
