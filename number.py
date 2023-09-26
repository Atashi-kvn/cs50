def main():
    x = get_int("what's x? ")
    print(f"x is {x}")

    

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x should be a whole number!")   #can use pass to override prompting user with this line
        




main()