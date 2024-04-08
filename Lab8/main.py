def remove_duplicates(arr):
    # Сортируем массив (можно выбрать любой алгоритм сортировки)
    arr.sort()

    # Проходимся по массиву и удаляем дубликаты
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            del arr[i]
        else:
            i += 1

if __name__ == "__main__":
    # Пример использования
    arr = [3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    print("Исходный массив:", arr)
    remove_duplicates(arr)
    print("Массив без дубликатов:", arr)

