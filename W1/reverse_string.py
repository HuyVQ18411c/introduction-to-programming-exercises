def reverse_string(my_string: str):
    reversed_string = ''
    for char in my_string:
        reversed_string = char + reversed_string
    return reversed_string


def main():
    print('Input string you want to reverse:')
    my_string = input()
    reversed_string = reverse_string(my_string)

    print(
        'String after reversing ====> {}'.format(
            reversed_string
        )
    )


if __name__ == '__main__':
    main()
