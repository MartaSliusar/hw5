import random
lst = []

for i in range(random.randint(3, 10)):
    lst.append(random.randint(0, 10))

my_list = [lst[0], lst[2], lst[-2]]
print(f"{lst} == {my_list}")