# def main():
#     x = int(input('Enter any number? '))
#     print(isEven(x))
#     # print('hello')

# def isEven(x):
#     if x % 2 == 0:
#         return f"{x} is Even "
#     else:
#         return f"{x} is Odd "


def match(name):
    match name:
        case "Govind":
            print(f"hello {name}")
        case "Aditya":
            print(f"Ahello {name}")


print(match("Aditya"))
# main()