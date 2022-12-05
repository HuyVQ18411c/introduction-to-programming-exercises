# Object oriented programming (OOP - Hướng đối tượng)
## Định nghĩa
Lập trình hướng đối tượng là một trong những phương pháp lập trình phổ biến nhất. Khác với functional oriented programming (Lập trình hướng chức năng), với OOP, chúng ta đưa những vật thể có những thuộc tính và phương thức (~~gần~~) giống nhau vào trong một <b>Object</b> để đại diện cho vật thể mà chúng ta nói tới.

Ví dụ: Xe máy

Xe máy là một trong những phương tiện phổ biến dùng để di chuyển tại Việt Nam. Với mỗi xe máy chúng ta có thể quan sát được chúng có điểm chung như sau:
- Có bánh xe (2 hoặc 4 bánh)
- Có màu sắc (đen, đỏ, trắng, ...)
- Có chức năng khởi động máy (để chạy)
- Có chức năng bật/tắt đèn

Và vô số các đặc tính chung khác. Dù nó có thể khác nhau về loại, tuy nhiên nhìn chung các thuộc tính này đều "chung loại". 

Để biểu diễn đối tượng này, trong lập trình, chúng ta có thể dùng OOP, và đưa nó vào một lớp (class). 
```
# Python
class Bike:
    def __init__(self, num_of_wheels: int, colour: str)
        # Đây là constructor. 
        self.num_of_wheels: int = num_of_wheels
        self.colour: str = colour

    def start_engine():
        do_something_to_start_engine()

    def turn_lights_on_off(turn_on: bool = False):
        if turn_on == True:
            turn_lights_on()
        else:
            turn_lights_off()
```

## Một số khái niệm cơ bản
Attributes (thuộc tính): các tính chất mô tả chung của một đối tượng. 

Methods (phương thức): các "actions" mà đối tượng thường làm.

Instance: một object (đối tượng) được tạo ra từ lớp. 

Constructor (hàm khởi tạo): hàm được gọi để tạo ra các instance của một lớp. 


