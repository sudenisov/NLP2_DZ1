
def GetData(dialogues_file_path = './data/dataset.txt'):
    # Список для хранения диалогов
    dialogues = []

    # Чтение диалогов из файла и удаление префиксов
    with open(dialogues_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        # Фильтрация строк, чтобы исключить пустые строки или строки без закрывающей скобки
        filtered_lines = [line.strip() for line in lines if ']' in line]

        # Обработка строк с диалогами
        for line in filtered_lines:
            parts = line.lstrip('[').split(']')
            if len(parts) > 1:
                dialogues.append(parts[1].strip())


    # Проверка на четность количества строк (должно быть четное)
    if len(dialogues) % 2 != 0:
        print("Ошибка: Нечетное количество строк в файле. Каждая реплика должна иметь свою пару.")
        exit()

    # Формирование списка диалогов Эльриана и Леонарда
    elrian_dialogues = dialogues[::2]
    leonard_dialogues = dialogues[1::2]
    return elrian_dialogues, leonard_dialogues
