"""
Hàm (Function) một block code được viết nhằm những lợi ích
- Tái sử dụng code
- Phân nhỏ chương trình thành các thành phần nhỏ hơn
- Giúp tăng sự tường minh khi đọc code
Trong Python, hàm được định nghĩa sử dụng từ khoá `def`
------------------
Function is a block of code can be used for many purposes:
- Prevent repeated code
- Seperate your application into smaller parts
- Improve code readability
In Python, function is defined using `def` keyword.
"""
def sum_two_int(a: int, b: int) -> int:
    return a + b

# Let's re-use!
sum_two_int(1, 2)
sum_two_int(3, 2)
sum_two_int(4, 3)
sum_two_int(5, 4)

"""
Ví dụ cho việc phân nhỏ chương trình:
Example for code seperation:
def make_tyres():
    # code for making tyres

def make_engine():
    # code for making engine

def manufacturing():
    # code for manufacturing

def make_a_car():
    make_tyres()
    make_engine()
    manufacturing()
"""