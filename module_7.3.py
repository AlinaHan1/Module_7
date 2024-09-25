class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', '-']
                    for i in punctuation:
                        line = line.replace(i, '')
                    # REPLAСE() Возвращает копию строки, в которой все вхождения подстроки заменяются другой подстрокой.
                    # Метод может принимать 3 пар-а: old - старая подстрока которую нужно заменить.
                    # new - новая подстрока, которая заменит старую.
                    # count - сколько раз вы хотите заменить старую подстроку новой.
                    # Если число не указано, метол заменяет все вхождения старой подстроки новой.
                    # Возвращаемое значение - копия строки в которой старая подстрока заменяется новой.
                    # Исходная строка не изменяется.
                    # Если старая подстрока не найдена, возвращается копия исходной строки.
                    line = line.replace(' - ', ' ')
                    #  EXTEND() позволяет добавить новые элементы в конец списка. Он принимает в качестве пар-ра
                    #  итерируемый объект и объединяет его со списком.
                    #  В отличии от append(), extend() принимает в качестве пар-в итерируемые объектыЖ
                    #  списки, кортежи и строки. При этом объединяемые списки могут содержать объекты любых типов.
                    words.extend(line.split())
                # SPLIT() Используется для разбиения подстроки на список подстрок на основе указанного разделителя.
                # Синтаксис метода: 'строка.split([разделитель[maxsplit]])'.
                # Разделитель - не обязательный пар-р.
                # Если разделитель не указан, то разбивка будет по пробельным символам.
                # Пар-р maxsplit определяет максимальное кол-во разбиений. Так же не обязательный
                all_words[file_name] = words
        return all_words

    # Метод, где word искомое слово. Возвращает словарь, где ключ - название файла,
    # значение - позиция первого word в списке слов того файла.
    def find(self, word):
        position = {}
        for key, value in self.get_all_words().items():  # items() показывает ключ и значение
            if word.lower() in value:
                position[key] = value.index(word.lower()) + 1
        return position

    # Метод, где word искомое слово. Возвращает словарь, где ключ - название файла,
    # значение - кол-во слова word в списке слов того файла.
    def count(self, word):
        quantity = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            quantity[value] = words_count
        return quantity


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
