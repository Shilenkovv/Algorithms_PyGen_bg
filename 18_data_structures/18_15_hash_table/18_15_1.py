# Вспомогательный класс для удобного представления пар хеш-таблицы
class Pair:
    def __init__(self, key, value):
        self.key = key  # Ключ
        self.value = value  # Значение


class HashTable:
    def __init__(self):
        self.size = 0  # Количество пар в таблице
        self.capacity = 10  # Вместимость таблицы
        self.buckets = [[] for _ in range(self.capacity)]  # Массив бакетов

    # Хеш-функция
    def hash_func(self, key):
        return abs(hash(key)) % self.capacity

    # Коэффициент заполнения таблицы
    def load_factor(self):
        return self.size / self.capacity

    # Увеличение вместимости таблицы вдвое
    def resize(self):
        old_buckets = self.buckets  # Сохраняем текущий массив бакетов
        self.capacity *= 2  # Удваиваем вместимость
        self.buckets = [[] for _ in range(self.capacity)]  # Создаем новый массив бакетов
        self.size = 0  # Сбрасываем счетчик пар

        # Перемещаем все существующие пары в новый массив бакетов
        for bucket in old_buckets:
            for pair in bucket:
                self.insert(pair.key, pair.value)

    # Добавление новой пары
    def insert(self, key, value):
        # Проверяем необходимость увеличения вместимости таблицы
        if self.load_factor() > 0.7:
            self.resize()

        index = self.hash_func(key)  # Определяем индекс бакета
        bucket = self.buckets[index]  # Получаем бакет

        # Проверяем, есть ли уже в бакете пара с таким ключом
        for pair in bucket:
            if pair.key == key:
                # Если пара есть, обновляем ее значение и завершаем работу
                pair.value = value
                return

        # Если пары нет, создаем новую пару и добавляем ее в бакет
        pair = Pair(key, value)
        bucket.append(pair)
        self.size += 1

    # Поиск значения по ключу
    def find(self, key):
        index = self.hash_func(key)  # Определяем индекс бакета
        bucket = self.buckets[index]  # Получаем бакет

        # Ищем в бакете пару с нужным ключом
        for pair in bucket:
            if pair.key == key:
                # Если пара есть, возвращаем ее значение
                return pair.value

        # Если пары нет, возвращаем None
        return None

    # Удаление пары по ключу
    def remove(self, key):
        index = self.hash_func(key)  # Определяем индекс бакета
        bucket = self.buckets[index]  # Получаем бакет

        # Ищем в бакете пару с нужным ключом
        for pair in bucket:
            if pair.key == key:
                # Если пара есть, удаляем ее и завершаем работу
                bucket.remove(pair)
                self.size -= 1
                return
