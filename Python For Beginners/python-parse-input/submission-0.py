from typing import List

def read_integers() -> List[int]:
    message = input()
    new_message = message.split(',')
    # return new_message
    new_list = []

    for i in new_message:
        new_list.append(int(i))
    return new_list



   

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
