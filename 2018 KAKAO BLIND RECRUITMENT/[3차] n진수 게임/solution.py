#변환 할 숫자 n, 진법 base
#변환된 숫자 list로 반환
def decToNBase(n, base):
    preset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    i = 0
    converted = []
    while True:
        if n < base:
            converted.insert(0, preset[n])
            return converted
        #몫
        q = int(n / base)
        #나머지
        r = n % base
        converted.insert(0, preset[r])
        n = q
def solution(n, t, m, p):
    answer = []
    #현재 차례
    turn = 1
    #현재 숫자
    current_number = 0
    #n진법으로 변환된 숫자 리스트
    converted_number_list = 0
    while True:
        converted_number_list = decToNBase(current_number, n)
        #print(converted_number_list)
        for i in range(len(converted_number_list)):
            if turn == p:
                answer.append(converted_number_list[i])
            turn = turn + 1
            if turn > m :
                turn = 1
            if len(answer) == t:
                return ''.join(answer)
        current_number = current_number + 1
    return answer
