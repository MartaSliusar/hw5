while True:
    number = int(input("Введіть число: "))
    if number <= 0:
        print("Введіть ціле додатнє число!")
    else:
        while number > 9:
            result = 1
            for el in str(number):
                result *= int(el)
                number = result
        print(number)

