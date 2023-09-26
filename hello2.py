def main():
    x = get_int("what's x? ")
    print(f"x is {x}")

# try:
#     x = int(input("what's x? "))
# except ValueError:
#     print("x should be a whole number!")
# else:
#     print(f"x is {x}")



# while True:
#     try:
#         x = int(input("what's x? "))
#         break
#     except ValueError:
#         print("x should be a whole number!")

# print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("what's x? "))
#         except ValueError:
#             print("x should be a whole number!")
#         else:
#             return x     #break breaking will be handled by return 
      


# def get_int():
#     while True:
#         try:
#             return int(input("what's x? "))
#         except ValueError:
#             print("x should be a whole number!")   #can use pass to override prompting user with this line
        


main()