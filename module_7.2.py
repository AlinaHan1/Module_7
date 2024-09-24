from pprint import pprint


def custom_write(file_name, strings):
    string_position = {}
    file_name = 'test.txt'
    file = open(file_name, 'a', encoding='utf-8')
    for i, string in enumerate(strings, start=1):
        position = file.tell()
        file.write(f'{string}\n')
        string_position[(i, position)] = string
    file.close()
    return string_position


info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
# enumerate применяется для итерируемых объектов(список относится к таковым) и создает объект генератор,
# который генерирует кортежи, состоящие из двух элементов - индекса элемента и самого элемента
# используется для упрощения прохода по коллекциям в цикле, когда кроме самих элементов требуется их индекс
