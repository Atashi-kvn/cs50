def main():
    length = get_length()
    print_square(length)

def get_length():
    while True:
        length = int(input("What's the size of your square? "))
        if length > 0:
            break
    return length


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)

main()