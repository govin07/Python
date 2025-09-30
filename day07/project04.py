str_input = input("Enter any penedrom string ").lower()

if str_input == str_input[::-1]:
    print("its penedrom")
else:
    print("its not a penedrom")