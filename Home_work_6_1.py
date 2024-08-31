import string

user_input = input('Введіть діапазон літер через дефіс: ')

start, end = user_input.split('-')

# print(start)
# print(end)

all_d = string.ascii_letters

result = all_d[all_d.index(start):all_d.index(end)+1]
print(result)