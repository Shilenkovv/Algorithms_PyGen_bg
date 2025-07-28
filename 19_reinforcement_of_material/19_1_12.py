class SumHashTable:
    def __init__(self):
        self.prefix_sums = {}  # префикс -> сумма значений
        self.key_values = {}  # ключ -> текущее значение

    def insert(self, key: str, value: int) -> None:
        old_value = self.key_values.get(key, 0)
        diff = value - old_value
        self.key_values[key] = value

        # Обновляем суммы для всех префиксов key
        for i in range(len(key) + 1):
            prefix = key[:i]
            self.prefix_sums[prefix] = self.prefix_sums.get(prefix, 0) + diff

    def sum(self, prefix: str) -> int:
        return self.prefix_sums.get(prefix, 0)
