"""
Đây là phần bài giải tham khảo cho Sample Test 1: Câu 2
"""
def print_triangle(width: int):
    # First of all we should double check
    # If the input height and width is a valid triangle
    for i in range(1, width + 1):
        print('*' * i)


if __name__ == '__main__':
    width = input('Nhập chiều dài:')
    while not width.isdigit() or int(width) <= 1:
        width = input('Nhập chiều dài:')
    else:
        print_triangle(int(width)) # Parse to int before passing to function
    
