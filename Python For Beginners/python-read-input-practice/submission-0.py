def add_two_numbers() -> int:
    user_input = input()
    numbers = user_input.split(',')

    new_list = []
    for i in numbers:
        new_list.append(int(i))
    return(sum(new_list))




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
