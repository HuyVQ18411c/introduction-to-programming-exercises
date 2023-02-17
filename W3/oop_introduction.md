## Available languages:
- [Tiếng Việt](#vietnamese)
- [English](#english)

# Object oriented programming (OOP - Hướng đối tượng)
## <a name="vietnamese"></a>Định nghĩa
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

## Một số tính chất quan trọng của OOP: 
### Xem thêm các ví dụ ở [`principles_of_oop.py`](https://github.com/HuyVQ18411c/introduction-to-programming-exercises/blob/python/W3/principles_of_oop.py)
Tính kế thừa (Inheritance):
- Đây là tính chất có thể nói được sử dụng rộng rãi và phổ biến nhất của OOP.
- Nó giúp chúng ta tuân theo nguyên tắc DRY trong lập trình (Don't repeat yourself).
- Trong lập trình: Tính kế thừa sẽ giúp cho những class (con) được kế thừa từ các lớp (cha) khác sẽ có được những thuộc tính (Attributes) cũng như các hàm (methods) của lớp mà nó kế thừa.
- Trong Python, chúng ta có thể đa kế thừa, và việc đa kế thừa sẽ theo nguyên tắc MRO (Method Resolution Order). Nguyên tắc này khá dễ hiểu có thể tạm hiểu là đến trước thì giành chỗ trước. Bạn nên tìm hiểu thêm về nguyên tắc này nếu muốn sử dụng hiệu quả đa kế thừa.

Tính bao đóng (Encapsulation):
- Tính chất này giúp người dùng sẽ không thấy hoặc thực thi được những hàm mà lập trình viên không muốn. (Hidden from user - giấu khỏi người dùng).
- Trong các ngôn ngữ như C#, Java chúng ta thường sử dụng những "Access modifiers" (tạm dịch: chỉ định truy cập - đừng dịch 🙂) là các từ khoá public, private, protected để xác định các thuộc tính/hàm có thể được truy cập bởi người dùng.
- Trong Python, chúng ta không có các từ khoá đó cụ thể, các lập trình viên thường tự hiểu với nhau sử dụng tiền tố `_` (underscore) hoặc `__` (double underscore).

Tính đa hình (Polymorphism):
- Tính chất này gắn liền với tính kế thừa.
- Khi 2 class cùng kế thừa từ 1 class, cùng có những thuộc tính nhưng khác nhau về giá trị, cùng có những methods những khác nhau về các thực thi, đó gọi là đa hình.

Tính trừu tượng (Abstraction):
- Một object có thể có thể là một đối tượng A, có thể là đối tượng B, nhưng chúng ta không cần biết nó là đối tượng gì, chỉ cần biết nó có những thuộc tính và có thể thực hiện những hành động nào. 
- Trong các ngôn ngữ static type chúng ta thường sẽ sử dụng abstract class, abstract method, interface để thực hiện điều này. 
- Trong các ngôn ngữ loose type như Python, chúng ta có thể assume rằng các object sẽ có những hàm và thuộc tính đó như abstraction. Chúng ta vẫn có thể sử dụng built-in package của Python để biểu diễn Abstract class.
----------

## <a name="english"></a>Definition
Object oriented programming is one of the most common ways to program, it's becomming a coding standard for every applications. Unlike functional oriented programing, OOP collects all the common attributes as well as methods of an object then brings it all to a class, which represent that object.

Ex: Animal

There are many types of animal around the world, each of them have their own unique characteristics and habitats. However, we can generalize many of these attributes.

In OOP world, we can demonstrate all of them in a class.
```
# Python
class Animal:
    def __init__(self, name: str, num_of_legs: int):
        self.name: str = name
        self.num_of_legs: int = num_of_legs

    def eat():
        eat_something()

    def sleep():
        print('Go to sleep')
```
## Basic concepts:

Attributes: characteristics that describe what does the object look like, which help you distinguish one from other instance of that class.

Methods: common 'actions' of that object.

Instance: object init from a class.

Constructor: a method that will be called on object initiation.
## Core principles of OOP:
### More example in [`principles_of_oop.py`](https://github.com/HuyVQ18411c/introduction-to-programming-exercises/blob/python/W3/principles_of_oop.py)
Inheritance:
- No, this is not money or property that someone gives you when they die. Nobody dies here. 
- This is the most-used and popular principle of OOP.
- It helps our code DRY (Don't repeat your self).
- In programming language: this principle will help an object to have attributes and methods of another objects without re-write it.
- In Python, we are able to use multiple inheritance, which will follow MRO (Method resolution order) rules. You may find it interesting, when you come to multiple inheritance. Others programming language also have this concepts, however their rules may different.

Encapsulation: 
- If you want to hide something (an attribute, a method, etc) from users, this principle is the way to go.
- In some programming language such as C#, Java they have "access modifiers" keywords (public, private, etc) to strictly support this principle. 
- In Python, we don't specify this strictly, Python programmers "tend to all agree" that if an attribute or method is marked with an underscore `_` or `__` double underscores it should not be accessed by users.

Polymorphism:
- This principle embraces inheritance.
- When two classes inherit the same class, with same set of attributes and methods, however different in values. They are siblings, they are polymorphism.

Abstraction:

Let start with an example for clarification:
You have a cooker with a set of functions, you know how to use it well, but you don't really know what makes it work. Those ready-for-uses functions of the cooker are abstractions, most users like us will not know about it's implementation, unless you are a machinist.
Same thing in programming:
- An object can be initiated  with class A, class B and can perform many actions, but when we use it, we may not need to know about how it was implemented.
- In many static typed languages, we can make this using interface, abstract class and method.
- In loosely typed languages like Python, we can assume a variable/parameter/object to have specific attributes or methods. Still, there are built-in package to help us achieve this.
# Reference
### Below are resources I find it really interesting to learn Python. Take a look if you have time:
- https://edube.org/learn/python-advanced-1/pcpp1-advanced-perspective-of-classes-and-oop: Wonderful course, to learn deeper about OOP and Python in general