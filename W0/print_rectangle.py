def print_rectangle(height: int, width: int):
    # You can either do this
    for i in range(height):
        print('*' * width)

    print()
    # Or this
    for row in range(height):
        for col in range(width):
            if col < width - 1:
                print('*', end='')
            if col == width - 1:
                print('*')


if __name__ == '__main__':
    print_rectangle(5, 10)