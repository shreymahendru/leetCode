

def diagonal(matrix):
    dic = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            s = i+j
            try:
                if s % 2 != 0:
                    dic[s].append(matrix[i][j])
                else:
                    dic[s].insert(0, matrix[i][j])
            except KeyError:
                dic[s] = [matrix[i][j]]

    answer = []
    for i in dic.keys():
        answer.extend(dic[i])
    return answer

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print diagonal(matrix)
