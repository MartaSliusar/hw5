while True:

    import string
    letter = string.ascii_letters
    x = input("Введіть дві букви через дефіс: ")
    x1 = x[0]
    x2 = x[-1]

    start = letter.index(x1)
    end = letter.index(x2)
    result = letter[start:end+1]
    print(result)
