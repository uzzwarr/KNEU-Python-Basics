import sys, io, re
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ============================================================
# завдання 4. частотний аналіз тексту
# ============================================================

text = """<p>The Python programming language, created in 1991, is POWERFUL!
Python is easy to read; Python is widely used. Version 3.12 & later
support many features... Learn Python, love Python!</p>"""


def clean_text(raw):
    # вилучаємо html-теги
    no_tags = re.sub(r"<[^>]+>", " ", raw)
    # вилучаємо числа
    no_digits = re.sub(r"\d+", " ", no_tags)
    # лишаємо тільки літери та пробіли (прибираємо пунктуацію й спецсимволи)
    no_punct = re.sub(r"[^a-zA-Zа-яА-ЯіїєґІЇЄҐ\s]", " ", no_digits)
    return no_punct


print("=" * 55)
print("завдання 4. частота слів")
print("=" * 55)

# 4а — очищення тексту від тегів, чисел, пунктуації
cleaned = clean_text(text)
# 4б — перетворюємо у нижній регістр
lowered = cleaned.lower()
# 4в — розбиваємо на список слів за пробілами
words = [w for w in lowered.split() if w]
# 4г — рахуємо частоту кожного слова
freq = dict(Counter(words))

print("\n4a-b) очищений текст (нижній регістр):")
print(f"  {lowered.strip()[:70]}...")

print("\n4c) список слів:")
print(f"  {words}")

print("\n4d) частотний словник:")
# виводимо словник, відсортований за спаданням частоти
for word, count in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0])):
    print(f"  {word:<14} -> {count}")