"""
Đặt vấn đề:
Trong kinh doanh nói chung, chúng ta thường có những thống kê doanh thu
trong từng tháng, từng quý. Với một công ty ổn định và trong điều kiện lý tưởng, 
chúng ta sẽ "thường" thấy công ty có doanh số bán hàng năm sẽ tương đối
giống nhau ứng với từng tháng. 
Ví dụ: 
Số liệu kinh doanh suốt 5 năm của một công ty A thu được kết quả:
- 4 tháng đầu năm doanh số của công ty này có xu hướng tăng dần và đạt cao nhất vào đầu tháng 5. 
==> Rất có thể năm 2023 cũng sẽ có khoảng thời gian tương tự, từ đó các công ty cần chuẩn bị cho tình huống này.
------
Bài toán:
Cho số liệu kinh doanh 12 tháng trong 5 năm của một công ty. 

Hãy tìm dãy số tăng dài nhất có trong một tập hợp các số tự nhiên tháng bắt đầu cũng như kết thúc của dãy tăng đó
Sau đó in ra màn hình.
Note: 
- Với 2 tháng cạnh nhau có số liệu bằng nhau, nó vẫn tính là một dãy tăng.

Ví dụ: 
Input: [4, 1, 3, 5, 6, 7, 4, 3, 4, 3, 4, 3]
Output: 5 (2 - 6)
Trong đó:
- 5 là chiều dài dãy tăng dài nhất.
- (2 - 6) là tháng bắt đầu -> kết thúc của dãy tăng đó. 
"""

FIGURES = [
    # [4, 1, 3, 5, 6, 7, 4, 3, 4, 3, 4, 3],
    [4, 1, 3, 5, 8, 7, 2, 3, 3, 3, 3, 3]
    # [4, 1, 3, 5, 6, 7, 4, 3, 4, 3, 4, 3]
    # [4, 1, 3, 5, 6, 7, 4, 3, 4, 3, 4, 3]
    # [4, 1, 3, 5, 6, 7, 4, 3, 4, 3, 4, 3]
]

def find_longest_ascending_chain_of_numbers(figure: list[int]):
    prev_max_path: int = 0
    prev_max_path_start_month: int = 1
    prev_max_path_end_month: int = 1

    max_path: int = 1
    max_path_start_month: int = 1
    max_path_end_month: int = 1
    prev_num: int = figure[0]
    for i in range(1, len(figure)):
        print(i)
        if max_path == 1: # 
            max_path_start_month = i - 1
        if prev_num <= figure[i]:
            max_path += 1
        else:
            max_path_end_month = i - 1
            if prev_max_path <= max_path:
                prev_max_path = max_path
                max_path = 1
                prev_max_path_start_month = max_path_start_month + 1
                prev_max_path_end_month = max_path_end_month + 1
            else:
                max_path = 1

        prev_num = figure[i]

    return prev_max_path, prev_max_path_start_month, prev_max_path_end_month


def main():
    for figure in FIGURES:
        max_path, start_month, end_month = find_longest_ascending_chain_of_numbers(figure)
        print('{} ({} - {})'.format(max_path, start_month, end_month))


if __name__ == '__main__':
    main()
