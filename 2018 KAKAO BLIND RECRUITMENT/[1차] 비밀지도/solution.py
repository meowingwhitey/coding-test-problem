def decToBinList(length, n):
    n = str(bin(n))
    n = n[2:]
    n = list(n)
    for i in range(length - len(n)):
        n.insert(0, "0")
    return n
def solution(n, arr1, arr2):
    answer = []
    #빈 맵으로 초기화
    for i in range(n):
        answer.append([])
        for j in range(n):
            answer[i].append(' ')
    #첫번째 지도
    for i in range(len(arr1)):
        t = decToBinList(n, arr1[i])
        for j in range(len(answer[i])):
            if t[j] == "1":
                answer[i][j] = "#"
    #두번째 지도
    for i in range(len(arr2)):
        t = decToBinList(n, arr2[i])
        for j in range(len(answer[i])):
            if t[j] == "1":
                answer[i][j] = "#"
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
    return answer
