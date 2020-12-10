def searchDic(dic, s):
    for i in range(len(dic)):
        if dic[i] == s:
            return i
    return -1
def compressString(s, n):
    compressed = ""
    i = 0
    while True:
        j = 1
        while True:
            if s[i + (j - 1) * n : i + j * n] == s[i + j * n:i + (j + 1) * n]:
                j = j + 1
            else:
                if j > 1:
                    #기존 압축된 문자열 + 새로운 문자 압축 횟수 + 새로운 문자 + 이후 남은 문자
                    compressed = compressed + str(j) + s[i + (j - 1) * n : i + j * n]
                else:
                    compressed = compressed + s[i + (j - 1) * n : i + j * n]
                i = i + j * n
                break
        if i >= len(s):
            break
    return compressed
def solution(s):
    answer = 1001
    compressed = []
    for i in range(1, int(len(s)/2) + 2):
        compressed = compressString(s, i)
        if len(compressed) < answer:
            answer = len(compressed)
            print(compressed)
    return answer
