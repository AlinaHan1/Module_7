import os
import time


def main():
    directory = '.'
    for root, dirs, files in os.walk(directory):  # позволяет рекурсивно обходить все директории
        # и получать полный список всех файлов в них
        print(f'>>root = "{root}", dirs = "{dirs}"')
        for file in files:
            filepath = os.path.join(root, file)
            # метод os.path.join() может объединять имена путей файлов или каталогов в один путь (вместо того, что бы
            # писать структуру пути вручную используют метод обработки путей модуля).
            filetime = os.path.getmtime(filepath)
            # метод os.path.getmtime() что бы получить время изменения файла,
            # этот метод возвращает время изменения файла как число с плавающей точкой
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            # принимает путь к файлу и возвращает размер в байтах
            parent_dir = os.path.dirname(root)
            # возвращает имя каталога в пути path
            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
                f' Время изменения: {formatted_time}, Родительская директория :{parent_dir}')


if __name__ == '__main__':
    main()
