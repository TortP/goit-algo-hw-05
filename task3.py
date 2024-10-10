import timeit
import requests


# Функція для завантаження файлу з Google Drive
def download_file_from_google_drive(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"Файл збережено як {destination}")
    else:
        print(f"Не вдалося завантажити файл з {url}. Код статусу: {response.status_code}")

# Завантаження файлів з Google Drive
download_file_from_google_drive(
    'https://drive.google.com/uc?export=download&id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh',
    'article1.txt'
)
download_file_from_google_drive(
    'https://drive.google.com/uc?export=download&id=18BfXyQcmuinEI_8KDSnQm4bLx6yIFS_w',
    'article2.txt'
)

# Реалізація алгоритмів пошуку підрядків (КМП, Рабіна-Карпа, Боєра-Мура)
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = [0] * m
    j = 0
    compute_lps(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return True
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False

def compute_lps(pattern, m, lps):
    length = 0
    lps[0] = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

def rabin_karp_search(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    h = pow(d, m-1) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i+m] == pattern:
                return True
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return False

def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    bad_char = {}

    # Заповнення таблиці "поганих символів" для всіх символів у підрядку
    for i in range(m):
        bad_char[pattern[i]] = i

    s = 0  # зсув тексту щодо підрядка
    while s <= n - m:
        j = m - 1

        # Зменшуємо j поки символи pattern і text збігаються
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # Якщо шаблон повністю збігається з текстом
        if j < 0:
            return True
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return False

# Завантаження текстових файлів
with open('article1.txt', 'r', encoding='ISO-8859-1') as file:
    text1 = file.read()

with open('article2.txt', 'r', encoding='ISO-8859-1') as file:
    text2 = file.read()


# Вибір підрядків для тестування
existing_substring = "відомий фрагмент"
non_existing_substring = "неіснуючий фрагмент"

# Функція для вимірювання часу виконання алгоритмів
def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=10)

# Вимірювання часу для кожного алгоритму на першому тексті
kmp_time1_existing = measure_time(kmp_search, text1, existing_substring)
kmp_time1_non_existing = measure_time(kmp_search, text1, non_existing_substring)

rabin_karp_time1_existing = measure_time(rabin_karp_search, text1, existing_substring)
rabin_karp_time1_non_existing = measure_time(rabin_karp_search, text1, non_existing_substring)

boyer_moore_time1_existing = measure_time(boyer_moore_search, text1, existing_substring)
boyer_moore_time1_non_existing = measure_time(boyer_moore_search, text1, non_existing_substring)

# Вимірювання часу для кожного алгоритму на другому тексті
kmp_time2_existing = measure_time(kmp_search, text2, existing_substring)
kmp_time2_non_existing = measure_time(kmp_search, text2, non_existing_substring)

rabin_karp_time2_existing = measure_time(rabin_karp_search, text2, existing_substring)
rabin_karp_time2_non_existing = measure_time(rabin_karp_search, text2, non_existing_substring)

boyer_moore_time2_existing = measure_time(boyer_moore_search, text2, existing_substring)
boyer_moore_time2_non_existing = measure_time(boyer_moore_search, text2, non_existing_substring)

# Виведення результатів
print("Результати для тексту 1:")
print(f"KMP (existing): {kmp_time1_existing}, KMP (non-existing): {kmp_time1_non_existing}")
print(f"Rabin-Karp (existing): {rabin_karp_time1_existing}, Rabin-Karp (non-existing): {rabin_karp_time1_non_existing}")
print(f"Boyer-Moore (existing): {boyer_moore_time1_existing}, Boyer-Moore (non-existing): {boyer_moore_time1_non_existing}")

print("\nРезультати для тексту 2:")
print(f"KMP (existing): {kmp_time2_existing}, KMP (non-existing): {kmp_time2_non_existing}")
print(f"Rabin-Karp (existing): {rabin_karp_time2_existing}, Rabin-Karp (non-existing): {rabin_karp_time2_non_existing}")
print(f"Boyer-Moore (existing): {boyer_moore_time2_existing}, Boyer-Moore (non-existing): {boyer_moore_time2_non_existing}")