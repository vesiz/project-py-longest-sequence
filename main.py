import sys


def readFile(file):
    _file = open(file, "r")
    lines = _file.read().rstrip().split("\n")

    # get matrix dimensions and create an empty one
    matrix = [[0] * int(lines[0].split(" ")[0]) for k in range(int(lines[0].split(" ")[1]))]
    lines.pop(0)

    for i, line in enumerate(lines):
        matrix[i] = line.split(" ")

    _file.close()

    return matrix


# check if cell (i, j) is valid
def isValid(matrix, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix)


def findSequence(matrix, i, j, helperMatrix):
    if not isValid(matrix, i, j):
        return None

    # matrix to memorize the sequence so far
    helperMatrix[i][j] = matrix[i][j]
    sequence = 0

    # recur top cell if its value is equal to the value at `(i, j)`
    if i > 0 and matrix[i - 1][j] == matrix[i][j] and helperMatrix[i - 1][j] == 0:
        sequence = findSequence(matrix, i - 1, j, list(map(list, helperMatrix)))
    # recur right cell if its value is equal to the value at `(i, j)`
    if j + 1 < len(matrix) and matrix[i][j + 1] == matrix[i][j] and helperMatrix[i][j + 1] == 0:
        sequence = findSequence(matrix, i, j + 1, list(map(list, helperMatrix)))

    # recur bottom cell if its value is equal to the value at `(i, j)`
    if i + 1 < len(matrix) and matrix[i + 1][j] == matrix[i][j] and helperMatrix[i + 1][j] == 0:
        sequence = findSequence(matrix, i + 1, j, list(map(list, helperMatrix)))

    # recur left cell if its value is equal to the value at `(i, j)`
    if j > 0 and matrix[i][j - 1] == matrix[i][j] and helperMatrix[i][j - 1] == 0:
        sequence = findSequence(matrix, i, j - 1, list(map(list, helperMatrix)))

    return sequence + 1 if sequence else 1


def findLongestSequence(matrix):
    result = None
    res_size = -sys.maxsize

    # find the longest sequence starting from from each cell (i, j)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            helperMatrix = [[0] * len(matrix) for k in range(len(matrix))]

            sequenceCount = findSequence(matrix, i, j, helperMatrix)

            if sequenceCount > res_size:
                result = sequenceCount
                res_size = sequenceCount

    return result


def IO():
    print()
    print("Please provide from 1 to 4 test files to calculate their longest sequence each.")
    print("Write the files' names separated by space:")

    fileNames = input()

    return list(filter(lambda x: x != "", fileNames.split(" ")))


def main():
    fileNamesList = IO()

    while len(fileNamesList) > 4 or len(fileNamesList) < 1:
        fileNamesList = IO()

    for fileName in fileNamesList:
        print()
        try:
            matrix = readFile(f"tests/{fileName}")
        except FileNotFoundError as err:
            print(f"A file with the name '{fileName}' can't be found.")
        else:
            result = findLongestSequence(matrix)
            print(f"The length of the longest sequence in file '{fileName}' is {result}.")


if __name__ == '__main__':
    main()
