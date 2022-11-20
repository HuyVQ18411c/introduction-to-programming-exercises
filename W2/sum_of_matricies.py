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
    [1, 2, 3, 4],
    [4, 5, 6],
    [7, 8, 9]
]


def is_validate_matrix(matrix: list[list[int]]) -> bool:
    row_count = len(matrix)
    first_row_element_count = len(matrix[0])
    for i in range(1, row_count):
        if first_row_element_count != len(matrix[i]):
            print('Not able to calculate matricies')
            return False
    return True


def calculate_sum_of_matricies(first_matrix: list[list[int]], second_matrix: list[list[int]]):
    if len(first_matrix) != len(second_matrix):
        print('Not able to calculate matricies')
        return

    # Check if matricies is validated
    if not is_validate_matrix(first_matrix):
        return
    
    if not is_validate_matrix(second_matrix):
        return

    row_count = len(first_matrix)
    for i in range(row_count):
        if len(first_matrix[i]) != len(second_matrix[i]):
            print('Not able to calculate matricies')
            return
    
    sum: list[list[int]] = []

    for i in range(row_count):
        sum.append([])
        col_count = len(first_matrix[i])
        for k in range(col_count):
            sum[i].append(first_matrix[i][k] + second_matrix[i][k])
    return sum


def main():
    sum = calculate_sum_of_matricies(FIRST_MATRIX, SECOND_MATRIX)
    print(sum)


if __name__ == '__main__':
    main()
