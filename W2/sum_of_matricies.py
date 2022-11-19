"""
Giả sử các ma trận có thể được biểu diễn dưới dạng sau:
[1, 2, 3]
[1, 2, 3] (Ma trận 3x3 - Gồm 3 mảng, mỗi mảng chứa 3 số nguyên) 
[1, 2, 3]
Hãy tính tổng của các ma trận cùng chiều
"""
FIRST_MATRIX = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

SECOND_MATRIX = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def calculate_sum_of_matricies(first_matrix: list[list[int]], second_matrix: list[list[int]]):
    if len(first_matrix) != len(second_matrix):
        print('Not able to calculate matricies')
        return

    n = len(first_matrix)
    for i in range(n):
        if len(first_matrix[i]) != len(second_matrix[i]):
            print('Not able to calculate matricies')
            return
    
    sum: list[list[int]] = []

    for i in range(n):
        sum.append([])
        for k in range(len(first_matrix[i])):
            sum[i].append(first_matrix[i][k] + second_matrix[i][k])
    return sum


def main():
    sum = calculate_sum_of_matricies(FIRST_MATRIX, SECOND_MATRIX)
    print(sum)


if __name__ == '__main__':
    main()
