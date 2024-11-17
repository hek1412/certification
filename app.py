import os
import sys
from datetime import datetime

def count_files_in_directory(directory_path): # Возвращает количество файлов в указанной директории.
    file_count = 0
    try:
        for root, dirs, files in os.walk(directory_path):
            file_count += len(files)
    except Exception:
        pass # Игнорируем ошибки
    return file_count

def get_top_10_files_by_size(directory_path): # Возвращает топ-10 файлов по размеру в указанной директории
    file_sizes = []
    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    size = os.path.getsize(file_path) / 1024  # Размер в КБ
                    file_sizes.append((size, file_path))
                except Exception:
                    pass  # Игнорируем ошибки
    except Exception:
        pass # Игнорируем ошибки

    file_sizes.sort(reverse=True, key=lambda x: x[0]) # Сортируем файлы по размеру в порядке убывания
    return file_sizes[:10] # берем топ-10

def main():
    user_name = os.getenv('USER_NAME', 'User')
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nПривет, {user_name}! Текущая дата и время: {current_time}")

    # Указание директории для обработки (если закомментировано, то в корневом каталоге)
    # path = '.'  # Текущая директория
    path = locals().get('path', '/')

    # Подсчёт количества файлов
    num_files = count_files_in_directory(path)
    print(f"Количество файлов в директории '{path}': {num_files}")

    # Вывод топ-10 файлов по размеру (в Кб)
    top_files = get_top_10_files_by_size(path)
    print("\nТоп-10 файлов по размеру: ")
    for index, (size, file_path) in enumerate(top_files, start=1):
        print(f"{index}. {file_path} - {size:.2f} KB")

if __name__ == "__main__":
    main()