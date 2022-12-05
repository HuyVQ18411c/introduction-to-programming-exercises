"""
Đặt vấn đề:
Trong các website hay mobile apps của các sàn Thương mại điện tử nói chung như Shopee hay Tiki
Chúng ta thường thấy các đối tượng Cart (giỏ hàng) và Product (sản phẩm).

Hãy thiết kế 2 đối tượng Cart và Product với các attributes và methods sau: 
Giỏ hàng có thể có những thuộc tính sau: 
Attributes:
- Mã giỏ hàng
- Tổng giá trị của các sản phẩm trong giỏ hàng
- Sản phẩm có trong giỏ hàng
Methods:
- Tính tổng tiền
- Thêm hàng vào giỏ hàng

Sản phẩm có thể có những thuộc tính sau:
- Mã
- Đơn giá
- Số lượng
- Cập nhật giá
- Cập nhật số lượng
"""
class Product:
    def __init__(self, id, price, quantity, name) -> None:
        self.id = id
        self.price = price
        self.quantity = quantity
        self.name = name

    def update_price(self, new_price):
        self.price = new_price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def __repr__(self) -> str:
        return '(Id: {}, Name: {})'.format(self.id, self.name)


class Cart:
    def __init__(self, id) -> None:
        self.id = id
        self.total_amount = 0
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def calculate_amount(self):
        total: float = 0
        for product in self.products:
            price = product.price
            quantity = product.quantity
            total += price*quantity
        self.total_amount = total


if __name__ == '__main__':
    shirt = Product(id = 1, price = 10000, quantity=3, name='Shirt')
    pants = Product(id = 2, price = 20000, quantity=2, name='Pants')

    my_cart = Cart(id = 1)
    my_cart.add_product(shirt)

    print(my_cart.products)
    print('Amount:', my_cart.total_amount)

    my_cart.calculate_amount()
    print('Calculated amount:', my_cart.total_amount)

    my_cart.add_product(pants)
    my_cart.calculate_amount()
    print('Calculated amount 2:', my_cart.total_amount)
