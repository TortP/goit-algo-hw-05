import sys


sys.stdout.reconfigure(encoding='utf-8')

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Перевіряємо, чи існує вже ключ, якщо так - оновлюємо значення
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Вставляємо нову пару ключ-значення
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                print(f"Ключ '{key}' успішно видалено.")
                return True
        print(f"Ключ '{key}' не знайдено.")
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Індекс {i}: {bucket}")

# Тестування хеш-таблиці
hash_table = HashTable()

# Вставляємо ключі та значення
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("cherry", 30)
hash_table.insert("date", 40)

# Відображаємо вміст хеш-таблиці перед видаленням
print("Хеш-таблиця до видалення:")
hash_table.display()

# Отримуємо значення за ключами
print("\nЗначення для ключа 'banana':", hash_table.get("banana"))  # Очікується: 20
print("Значення для ключа 'cherry':", hash_table.get("cherry"))  # Очікується: 30

# Видаляємо ключ 'banana'
hash_table.delete("banana")

# Спробуємо знову отримати значення для 'banana'
print("\nЗначення для ключа 'banana' після видалення:", hash_table.get("banana"))  # Очікується: None

# Відображаємо вміст хеш-таблиці після видалення
print("\nХеш-таблиця після видалення:")
hash_table.display()
