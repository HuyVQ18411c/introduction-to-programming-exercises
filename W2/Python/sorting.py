"""
Đặt vấn đề:

Khi sử dụng các trang web hay các thiết bị điện tử, chúng ta thường có
chức năng sắp xếp, thứ mà sẽ cung cấp cho người dùng khả năng tìm kiếm
các thông tin mình mong muốn một cách nhanh chóng và hiệu quả nhất. 

Ví dụ có thể kể đến danh bạ điện thoại, thường theo mặc định,
các thiết bị sẽ sắp xếp theo thứ tự các chữ cái theo bảng chữ cái. 

Hãy sắp xếp mảng gồm các số nguyên theo thứ tự từ nhỏ đến lớn.
"""

TEST_DATA: list[list[int]] = [
    [6, 5, 2, 4, 7, 10, 9],
    [1, 3, 6, 5, 4, 2, 0],
    [10, 13, 6, 8, 20, 11, 15, 17],
    [11, 11, 10, 8, 12, 17, 6, 5]
]


def sort(array: list[int]):
    """Sort an array"""
    for i in range(0, len(array)):
        for k in range(i + 1, len(array)):
            if array[i] > array[k]:
                value = array[i]
                array[i] = array[k]
                array[k] = value

    return array # sorted


def main():
    for array in TEST_DATA:
        sorted_array = sort(array)
        print('My final sorted array:', sorted_array)


if __name__ == '__main__':
    main()
