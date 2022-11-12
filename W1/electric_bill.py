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