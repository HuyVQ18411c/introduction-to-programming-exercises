# Introduction to programming
## Sample test 1
### Câu 1: Hãy vẽ lưu đồ ứng với bài toán ở câu 5.
### Câu 2: Hãy chỉ ra những đoạn code không cần thiết/sai trong chương trình dưới đây code ứng với input và output cho trước.
```
Input 1.1: 5
Input 1.2: [1, 2, 5, 6, 8, 9, 10, 5, 3, 4, 5, 5, 2, 4, 11, -5]

Output 1: 3
Output 1.1: [2, 7, 10, 11]
------------
Input 2.1: 0
Input 2.2: [0, 19, 13, 3, 0, 8, 4, 15, 11, 1, 18, 12, 2, 14, 0, 16, 17, 7, 9, 10, 0, 6, 5, 0]

Output 2.1: 5
Output 2.2: [0, 4, 14, 20, 23]
```
Code: 
```
def do_something(input1: int, input2: list[int]):
    output1 = len(input2)
    output2 = []

    if input1 < 0:
        return # Do nothing
    
    for i in range(input2):
        if input2[i] != input1:
            output1 -= 1
        else:
            output2.append(i + 1)

    print(output1) # print the result
    print(output2) # print the result

    return output1, output2
``` 
### Câu 3: Hãy in ra màn hình console ứng với yêu cầu sau:
### Từ bàn phím người dùng nhập vào chiều dài ứng với 2 cạnh góc vuông của hình tam giác cân, hãy in ra hình tam giác sử dụng dấu sao (*) để biểu diễn tam giác này. 

### Câu 4: Hãy viết chương trình ứng với yêu cầu sau đây. Tìm dãy số tăng liên tiếp dài nhất có trong list. Nếu 2 số cạnh nhau liên tiếp trong list bằng nhau, đó vẫn tính là 1 dãy tăng. 

### Câu 5: Đọc mô tả bài toán và đưa ra cách tính cách giải phù hợp bằng Python
### Cho 3 ma trận hãy tính tích của các ma trận đó

