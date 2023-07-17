def findMatrixTranspose(matrix, noOfRows):
    for i in range(noOfRows):
        for j in range(i, noOfRows):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


def rotateMatrix(matrix, length):
    for i in range(length):
        matrix[i] = matrix[i][::-1]

    return matrix


if __name__ == "__main__":
    noOfRows = int(input("Enter the no.of rows : "))

    matrix = []
    for i in range(noOfRows):
        matrix.append(list(map(int, input().strip('[').strip(']').split(','))))

    matrix = findMatrixTranspose(matrix, noOfRows)

    print(rotateMatrix(matrix, noOfRows))
