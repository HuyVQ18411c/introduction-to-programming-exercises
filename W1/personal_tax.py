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
    