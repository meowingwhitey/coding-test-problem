class Node:
    def __init__(self, data):
        self.data = data
        self.leaf = []
def calcSearchCount(node, word):
    cnt = 0
    i = 0
    while True:
        if len(node.leaf) == 0 or len(word) == i:
            if cnt <= 2 and len(node.leaf) >= 2:
                cnt = len(word) - 1
            break
        if len(node.leaf) > 1:
            cnt = i
        for j in range(len(node.leaf)):
            if node.leaf[j].data == word[i]:
                i = i + 1
                node = node.leaf[j]
                break
    return cnt + 1
def isLeafExist(node, char):
    for i in range(len(node.leaf)):
        if node.leaf[i].data == char:
            return node.leaf[i]
    return False
def addLeaf(node, char):
    temp = Node(char)
    node.leaf.append(temp)
    return temp
def solution(words):
    answer = 0
    root = Node(None)
    cur = root
    #Init Trie
    for i in range(len(words)):
        cur = root
        j = 0
        while j < len(words[i]):
            while True:
                if j >= len(words[i]):
                    break
                next_node = isLeafExist(cur, words[i][j])
                if next_node == False:
                    cur = addLeaf(cur, words[i][j])
                    j = j + 1
                    break
                else:
                    cur = next_node
                    j = j + 1
        addLeaf(cur, None)
    #Calc count
    for i in range(len(words)):
        answer = answer + calcSearchCount(root, words[i])
        #print(answer)
    return answer
