def main():
    number = get_number()
    print_column(number)

def get_number():
    while True:
        n = int(input("What's the hight? "))
        if n > 0:
            break
    return n


def print_column(height):
    print("#\n" * height, end="")



main()