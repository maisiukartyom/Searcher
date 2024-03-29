import csv

def search_csv(file_path, search_string):
    # Открываем CSV файл для чтения
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        # Создаем список для хранения найденных записей
        found_records = []
        
        # Проходим по каждой записи в CSV файле
        for row in csvreader:
            # Проверяем, содержит ли поле "text" введенную строку
            if search_string in row['text']:
                # Если да, то добавляем эту запись в список найденных записей
                found_records.append(row)
        
        # Сортируем найденные записи по полю 'creation_date'
        found_records.sort(key=lambda x: x['created_date'])
        
        # Возвращаем первые 20 записей
        return found_records[:20]


if __name__ == "__main__":
    file_path = 'posts.csv'  # Путь к вашему CSV файлу
    search_string = input("Введите строку для поиска: ")

    # Вызываем функцию поиска и выводим результат
    results = search_csv(file_path, search_string)
    
    if results:
        print("Результаты поиска:")
        for record in results:
            print(record)
    else:
        print("Ничего не найдено.")
