"""
Đặt vấn đề:
Mỗi cá nhân khi bán mình cho tư bản đều phải đóng 1 khoản
thuế thu nhập cá nhân được tính dựa trên lương gross của mình.

Diễn giải:
- Lương gross: lương trừ đi thuế, bảo hiểm, các khoản giảm trừ thuế theo luật.

Thuế thu nhập cá nhân được tính trên phần thu nhập thực nhận
sau khi đã trừ đi các khoản:
- Miễn trừ bản thân: 11 * 10^6 (vnd)
- Người phụ thuộc: 4.4 * 10^6/người (vnd)
- Bảo hiểm (xã hội, lao động, thất nghiệp): 10.5%/lương gross (vnd)

Người có phần thu nhập tính thuế càng lớn sẽ đóng thuế càng nhiều, cụ thể:
Bậc	| Thu nhập tính thuế/tháng (triệu đồng)	 |   Thuế suất
1	| Đến 05	                             |       5 %
2	| Trên 05 -> 10	                         |      10 %
3	| Trên 10 -> 18	                         |      15 %
4	| Trên 18 -> 32	                         |      20 %
5	| Trên 32 -> 52	                         |      25 %
6	| Trên 52 -> 80	                         |      30 %
7	| Trên 80	                             |      35 %

Hãy viết một hàm tính thuế thu nhập cá nhân tương ứng với lương người dùng nhập.
"""


def get_tax(amount: float):
    tax = 0

    if amount <= 0:
        return tax

    initial_amount = amount / 1000000

    if initial_amount <= 5:
        tax = initial_amount * 0.05

    if initial_amount > 5 and initial_amount <= 10:
        tax = initial_amount * 0.1 - 0.25

    if initial_amount > 10 and initial_amount <= 18:
        tax = initial_amount * 0.15 - 0.75
    
    if initial_amount > 18 and initial_amount <= 32:
        tax = initial_amount * 0.2 - 1.65
    
    if initial_amount > 32 and initial_amount <= 52:
        tax = initial_amount * 0.25 - 3.25

    if initial_amount > 52 and initial_amount <= 80:
        tax = initial_amount * 0.3 - 5.85

    if initial_amount > 80:
        tax = initial_amount * 0.35 - 9.85
    
    return tax * 1000000


def calculate_taxable_salary(total: float, dependencies: int=0):
    total = total / 1000000
    initial_removal = 11 + total * 0.105 + 4.4 * dependencies
    taxable_salary = total - initial_removal
    return taxable_salary * 1000000


def main():
    # https://web-platform-3vv8vx.stackblitz.io
    salary = None
    dependencies = None
    while (
        not isinstance(salary, float) and 
        not isinstance(dependencies, int)
    ):
        try:
            print('Input your salary')
            salary = float(input())
            print('Input your dependencies')
            dependencies = int(input())
        except:
            salary = None
            dependencies = None
    else:
        taxable_salary = calculate_taxable_salary(salary)
        tax = get_tax(taxable_salary)
        print('Tax: {}'.format(round(tax)))


if __name__ == '__main__':
    main()
    