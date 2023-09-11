# task 16.1 (воно буде закоментованим, оскільки помилка не дасть змогу пройтись по іншим завданням)
'''
str = "qwerty"
str[0] = "8"  # буде помилка
'''

# task 16.2 (об'єднання рядків)
str = 'qwerty'
str2 = "asdf"
new_str = str + str2
print(new_str)


# task 16.3 (множення рядків)

str3 = str2 * 10
print(str3)


# task 16.4 (вставка символа у певне місце)

init_str = "foo bar"
pos = 3
added_char = "l"

upd_str = init_str[:pos] + added_char + init_str[pos:]
print(init_str, upd_str)


# task 16.5 (заміна символа)
changed_str = init_str[:pos] + added_char + init_str[pos+1:]
print(init_str, changed_str, init_str[5:])
