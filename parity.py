
       #
# x = int(input("What is x? "))

# if x % 2 == 0:
#     print(f"x = {x} which  is Even")
# else:
#    print(f"x = {x} which is Odd")




def main():
    x = int(input("What is x? "))
    if is_even(x):
        print(f"x = {x} which  is Even")
    
    else:
        print(f"x = {x} which is Odd")


# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


def is_even(n):
    #return True if n % 2 == 0 else False
    return n % 2 == 0



main()