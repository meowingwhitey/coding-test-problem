#사전 내에 msg 검색
def searchDic(dic, msg):
    for i in range(len(dic)):
        if dic[i] == msg:
            return i
    return -1
#사전에 msg 등록
def registerDic(dic, msg):
    dic.append(msg)
def solution(msg):
    #압축 색인번호
    answer = []
    #사전
    dic = []
    #사전 생성
    for i in range(ord("A"), ord("Z") + 1):
        dic.append(chr(i))
    i = 0
    while True:
        if i >= len(msg):
            break
        j = len(msg)
        while True:
            #사전에서 마지막 인덱스~끝까지 검색
            t = searchDic(dic, msg[i : i + j])
            #만약 있으면 추가해줌
            if t != -1:
                registerDic(dic,msg[i : i + j + 1])
                answer.append(t + 1)
                i = i + j
                break
            #없으면 기존 msg에서 한글자를 줄인 후 다시 탐색
            else:
                j = j - 1
    return answer
