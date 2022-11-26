"""
Đặt vấn đề:
Tại Việt Nam chúng ta tính giá điện theo bậc thang. 
Tức sử dụng càng nhiều đơn giá trên một KWh càng tăng.

Hiện tại chúng ta đang có 6 bậc tương ứng với 6 mức giá. 
Mức giá được diễn giải như sau:
- Với 50 (kwh) đầu tiên sẽ tính theo đơn gia bậc 1 - 1678vnd/kwh
- Với 50 (kwh) tiếp theo, giá điện sẽ tính theo bậc 2 - 1734vnd/kwh
- Tương tự:
    + Với 100 kwh tiếp theo - Đơn giá bậc 3: 2014 vnd/kwh
    + Với 100 kwh tiếp theo - Đơn giá bậc 4: 2014 vnd/kwh
    + Với 100 kwh tiếp theo - Đơn giá bậc 5: 2014 vnd/kwh
- Sau khi hết số kwh của đơn giá bậc 5, tất cả các kwh tiếp theo
sẽ có đơn giá: 2927vnd/kwh

Hãy viết một hàm để tính giá tiền điện 
dựa trên số lượng điện người dùng nhập vào. 
"""

STAGE_1_PRICE: int = 1678
STAGE_2_PRICE: int = 1734
STAGE_3_PRICE: int = 2014
STAGE_4_PRICE: int = 2536
STAGE_5_PRICE: int = 2834
STAGE_6_PRICE: int = 2927

STAGE_1_AMOUNT: int = 50
STAGE_2_AMOUNT: int = STAGE_1_AMOUNT + 50
STAGE_3_AMOUNT: int = STAGE_2_AMOUNT + 100
STAGE_4_AMOUNT: int = STAGE_3_AMOUNT + 100
STAGE_5_AMOUNT: int = STAGE_4_AMOUNT + 100


def calculate_electric_bill(amount):
    total: float = 0
    if amount <= STAGE_1_AMOUNT:
        total = amount * STAGE_1_PRICE
    if amount > STAGE_1_AMOUNT and amount <= STAGE_2_AMOUNT:
        total = (
            STAGE_1_AMOUNT * STAGE_1_PRICE
            + (amount - STAGE_1_AMOUNT) * STAGE_2_PRICE
        )
    if amount > STAGE_2_AMOUNT and amount <= STAGE_3_AMOUNT:
        total = (
            STAGE_1_AMOUNT * STAGE_1_PRICE
            + STAGE_2_AMOUNT * STAGE_2_PRICE
            + (amount - STAGE_1_AMOUNT - STAGE_2_AMOUNT)
        )
    if amount > STAGE_3_AMOUNT and amount <= STAGE_4_AMOUNT:
        total = (
            STAGE_1_AMOUNT * STAGE_1_PRICE
            + STAGE_2_AMOUNT * STAGE_2_PRICE
            + STAGE_3_AMOUNT * STAGE_3_PRICE
            + (amount - STAGE_1_AMOUNT - STAGE_2_AMOUNT - STAGE_3_AMOUNT)
        )
    if amount > STAGE_4_AMOUNT and amount <= STAGE_5_AMOUNT:
        total = (
            STAGE_1_AMOUNT * STAGE_1_PRICE
            + STAGE_2_AMOUNT * STAGE_2_PRICE
            + STAGE_3_AMOUNT * STAGE_3_PRICE
            + STAGE_4_AMOUNT * STAGE_4_PRICE
            + (amount - STAGE_1_AMOUNT - STAGE_2_AMOUNT - STAGE_3_AMOUNT - STAGE_4_AMOUNT)
        )
    if amount > STAGE_5_AMOUNT:
        total = (
            STAGE_1_AMOUNT * STAGE_1_PRICE
            + STAGE_2_AMOUNT * STAGE_2_PRICE
            + STAGE_3_AMOUNT * STAGE_3_PRICE
            + STAGE_4_AMOUNT * STAGE_4_PRICE
            + STAGE_5_AMOUNT * STAGE_5_PRICE
            + (amount - STAGE_1_AMOUNT - STAGE_2_AMOUNT - STAGE_3_AMOUNT - STAGE_4_AMOUNT - STAGE_5_AMOUNT)
        )
    return total


def main():
    amount = None
    while not isinstance(amount, int):
        try:
            print('Enter your electric amount:')
            amount = int(input())
        except:
            amount = None
    else:
        total = calculate_electric_bill(amount)
        print('Total: {}'.format(total))
        
        
if __name__ == '__main__':
    main()