def shift_register(number):
    number += 1
    return number


i = 0


while True:
    print(shift_register(i))