INVALID_CHARACTER = [
    '$', '%', '^',  
    '*', '#', '$', 
    '&', '!', '?'
]


def main():
    my_string = input()
    for char in INVALID_CHARACTER:
        my_string = my_string.replace(char, '')
    print('My string after clean: {}'.format(my_string))


if __name__ == '__main__':
    main()
