while True:
    lst = input("Введіть числа через кому").split(',')
    number = []
    zero = []
    for el in lst:
        el = int(el)
        if el == 0:
            zero.append(el)
        else:
            number.append(el)
    result = number + zero
    print(result)

