"""
Đặt vấn đề:
Khi đăng ký các tài khoản, 
chúng ta thường cần phải chọn cho mình một username hợp lệ.
Username hợp lệ sẽ cần phải thoả những điều kiện khác nhau, cụ thể:
- Không được trùng với những người dùng đã đăng ký trước.
- Không được chứa các ký tự đặc biệt không được phép 
    (Ví dụ: '$', '%', '^', '*', '#', '$', '&', '!', '?')

Hãy viết một hàm kiểm tra username người dùng nhập vào để thoả các điều kiện trên. 
- Nếu chuỗi đó có ký tự không cho phép, hãy in ra màn hình 'Invalid username'
- Hãy thay thế các ký tự đó bằng chuỗi rỗng ''
"""
EXISTING_USERNAMES = [
    'nhoxpun', 'nhox_huy_vjp_pro',
    'han_doi_khong_cong_bang'
]


INVALID_CHARACTER = [
    '$', '%', '^',  
    '*', '#', '$', 
    '&', '!', '?'
]


def main():
    print('Input your username:')
    username = input()
    if username in EXISTING_USERNAMES:
        print(
            'Username {} already exists. Please use another account.'.format(
                username
            )
        )
        return
    for char in INVALID_CHARACTER:
        if char in username:
            print('Invalid username with character: {}'.format(char))
            username = username.replace(char, '')
    print('Username after clean: {}'.format(username))


if __name__ == '__main__':
    main()
