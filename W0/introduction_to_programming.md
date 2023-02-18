# Các kiến thức cơ bản
## Kiểu dữ liệu cơ sở (Primitive types):
Ghi chú: đây là các kiểu dữ liệu nói chung trong lập trình.
- byte: byte
- short: số nguyên 
- int: số nguyên
- long: số nguyên
- float: số thập phân
- double: số thập phân
- char: kí tự
- string: chuỗi các kí tự

Các kiểu dữ liệu này thường không được gán tường minh cho một biến được tạo trong Python.

Một số kiểu dữ liệu như số nguyên hay số thập phân có nhiều dạng biểu diễn, tuy nhiên trong Python chúng ta cũng sẽ không phải định nghĩa cho biến rõ ràng điều này. 

Tại sao cùng là số nguyên chúng ta lại có thể biểu diễn dưới nhiều dạng khác nhau? Phần lớn, chúng sẽ khác nhau về size (số lượng bytes sẽ chiếm trong bộ nhớ).

Ví dụ như với ngôn ngữ C:
<table>
    <tr>
        <th>Type</th>
        <th>Storage size (bytes - depends on OS)</th>
    </tr>
    <tr>
        <td>short</td>
        <td>2</td>
    </tr>
    <tr>
        <td>int</td>
        <td>4</td>
    </tr>
    <tr>
        <td>long</td>
        <td>8</td>
    </tr>
    <tr>
        <td>float</td>
        <td>4</td>
    </tr>
    <tr>
        <td>double</td>
        <td>8</td>
    </tr>
</table> 

Tuy nhiên với Python size của các kiểu dữ liệu sẽ khác so với những gì chúng ta đã thấy ở trên. Vì Python sẽ có `extra over-head implementation`. Nếu bạn tò mò bạn có thể đọc câu trả lời [này](https://stackoverflow.com/a/49318989) trên StackOverflow.

## Toán tử (Math operator)
Các toán tử trong lập trình nói chung có thể khá dễ dàng để nhận biết đặc biệt nếu bạn đã dùng qua MS Excel: +, -, *, /
Một số ví dụ:

```
Tổng: a = b + c
Hiệu: a = b - c
Nhân: a = b * c
Chia: a = b / c
```
Một số cách viết nhanh:
```
Tăng lên một đơn vị: a = a + 1 hoặc a += 1
Không phải Python: ++a, a++

Tương tự: a = a - 1 hoặc a -= 1
Không phải Python: --a, a--
```
Tuy nhiên trong lập trình các toán tử này các bạn có thể dùng nó với kiểu string thay vì chỉ với số.
```
a = 'hello'
b = 'world!'

c = a + b # Expected result c = 'hello world!'
```
Lưu ý: bạn không thể thực hiện toán tử `-` và `/` đối với chuỗi.

Nếu bạn tò mò về cú pháp `a++` hay `++a` này trong các ngôn ngữ khác: [Increment/Decrement Operator](https://www.programiz.com/article/increment-decrement-operator-difference-prefix-postfix)

## Hàm (Function)
Hàm, một cách để bạn tái sử dụng code của mình đã viết.
Thay vì chúng ta viết từ trên xuống dưới, chúng ta có thể bọc nó trong <b>Hàm</b>
Ví dụ trong Python
```
def add_two_number(a: int, b: int) -> int:
    return a + b

result = add_two_number(1, 2) # Expected result = 3
result = add_two_number(2, 3) # Expected result = 5
```

Từ ví dụ trên, chúng ta sẽ không cần viết lại phép toán cộng 2 số cho mỗi lần bạn muốn thực hiện phép toán này nữa.

Khi viết hàm bạn nên tuân thử quy tắc SRP (single responsibility principle): tức mỗi hàm được viết ra chỉ nên dùng để thực hiện 1 hành động, thao tác duy nhất. Đọc thêm [SRP](https://en.wikipedia.org/wiki/Single-responsibility_principle).

## Nếu bạn lần đầu học lập trình
Bạn nên biết kiểu dữ liệu `string` là tập hợp của một chuỗi các kí tự (char). 

Dưới góc độ của máy tính: khi các bạn khai báo một biến là kiểu string, tức bạn đang `allocate memory` liên tiếp. Với mỗi địa chỉ trên bộ nhớ bạn sẽ chứa vào trong đó 1 kí tự, và nó sẽ liên tiếp nhau tạo thành một chuỗi (một string). Do đó ta có thể hiểu string về bản chất là một mảng.

Mình cực kỳ khuyến khích bạn nên xem video sau để có thể hiểu sâu thêm: [CS50 - Memory](https://www.youtube.com/watch?v=AcWIE9qazLI&pp=ugMICgJ2aRABGAE%3D). 