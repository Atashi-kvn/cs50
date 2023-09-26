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
    #for @ row in the square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #printing the brick, mult by 2 to compensate for the dimations of # to be close to a square.
            print("#"*2, end="")
        print()




main()