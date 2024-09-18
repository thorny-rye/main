def custom_write(file_name, strings):
    file_name = "test.txt"
    file = open(file_name, "w", encoding="UTF-8")
    strings_positions = {}
    num_str = 0
    f = file.seek(0)
    for str in strings:
        file.write(f'{str}\n')
        num_str += 1
        key = (num_str, f)
        strings_positions[key] = str
        f = file.tell()
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
