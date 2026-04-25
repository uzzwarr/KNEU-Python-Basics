"""
завдання 2:
побудувати діаграми розсіювання:
 - ВВП та кількість населення для країн ЄС у 2020 році;
 - ВВП на душу населення та середня тривалість життя для країн ЄС у 2020 р.;
 - для 2-ї діаграми розкрасити точки залежно від категорії:
   1 — вступили до 1986; 2 — 1986-2000; 3 — з 2004;
 - додати розмір точок як 3-тю змінну: витрати на охорону здоров'я на душу.
"""
 
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
 
import matplotlib.pyplot as plt
import numpy as np
 
 
EU_COUNTRIES = [
    ("Німеччина",   3806, 83.2,  45732, 81.3, 5986, 1957),
    ("Франція",     2715, 67.4,  40284, 82.7, 5468, 1957),
    ("Італія",      1886, 60.2,  31320, 82.3, 3255, 1957),
    ("Іспанія",     1281, 47.4,  27024, 83.3, 2741, 1957),
    ("Нідерланди",   913, 17.4,  52449, 82.3, 5765, 1957),
    ("Бельгія",      524, 11.5,  45558, 81.4, 5119, 1957),
    ("Австрія",      433,  9.0,  48121, 81.8, 5395, 1995),
    ("Швеція",       541, 10.4,  52028, 82.4, 5782, 1995),
    ("Данія",        356,  5.8,  61413, 81.6, 6673, 1973),
    ("Фінляндія",    269,  5.5,  48913, 82.0, 4578, 1995),
    ("Ірландія",     425,  5.0,  85000, 82.3, 5227, 1973),
    ("Португалія",   228, 10.3,  22136, 81.1, 2258, 1986),
    ("Греція",       188, 10.7,  17570, 82.2, 1731, 1981),
    ("Польща",       596, 37.9,  15727, 78.5, 1065, 2004),
    ("Чехія",        245, 10.7,  22897, 79.4, 2085, 2004),
    ("Угорщина",     155,  9.8,  15816, 76.9,  959, 2004),
    ("Румунія",      248, 19.2,  12917, 75.3,  683, 2007),
    ("Болгарія",      68,  6.5,  10462, 75.0,  623, 2007),
    ("Словаччина",   105,  5.5,  19091, 77.8, 1318, 2004),
    ("Хорватія",      57,  4.0,  14250, 78.5,  857, 2013),
    ("Словенія",      53,  2.1,  25238, 81.3, 2096, 2004),
    ("Литва",         56,  2.8,  20000, 76.0, 1190, 2004),
    ("Латвія",        34,  1.9,  17895, 75.5,  970, 2004),
    ("Естонія",       31,  1.3,  23846, 78.8, 1553, 2004),
    ("Люксембург",    73,  0.63,115873, 82.3, 6183, 1957),
    ("Мальта",        14,  0.52, 26923, 82.7, 2449, 2004),
    ("Кіпр",          24,  0.89, 26966, 82.7, 1800, 2004),
]
 
def _cat(y): return 1 if y <= 1986 else (2 if y <= 2000 else 3)
 
NAMES      = [c[0] for c in EU_COUNTRIES]
GDP        = [c[1] for c in EU_COUNTRIES]
POPULATION = [c[2] for c in EU_COUNTRIES]
GDP_PC     = [c[3] for c in EU_COUNTRIES]
LIFE_EXP   = [c[4] for c in EU_COUNTRIES]
HEALTH_EXP = [c[5] for c in EU_COUNTRIES]
JOIN_YEAR  = [c[6] for c in EU_COUNTRIES]
CATEGORY   = [_cat(y) for y in JOIN_YEAR]
 
GROUP3_NAMES = [c[0] for c in EU_COUNTRIES if _cat(c[6]) == 3]
GROUP3_GDPPC = [c[3] for c in EU_COUNTRIES if _cat(c[6]) == 3]
 
COUNTRIES_5 = ["Німеччина", "Франція", "Чехія", "Польща", "Румунія"]
GDP_PC_2010 = [40408, 38759, 19716, 12294,  7536]
GDP_PC_2015 = [41109, 36574, 17562, 12489,  8977]
GDP_PC_2020 = [45732, 40284, 22897, 15727, 12917]
 
PIE_WORLD_LABELS  = ["Азія", "Пн. Америка", "Європа", "Лат. Америка", "Африка", "Інше"]
PIE_WORLD_VALUES  = [34.5, 27.9, 22.1, 7.8, 3.1, 4.6]
PIE_EUROPE_LABELS = ["Зах. Європа", "Центр. Європа", "Сх. Європа", "Пн. Європа", "Пд. Європа"]
PIE_EUROPE_VALUES = [44.2, 18.3, 12.5, 13.7, 11.3]
PIE_UKRAINE_LABELS= ["Послуги", "Промисловість", "С/г", "Будівництво", "Інше"]
PIE_UKRAINE_VALUES= [55.4, 24.0, 10.2, 5.8, 4.6]
 
STACK_COUNTRIES = ["США", "Німеччина", "Туреччина", "Польща", "Україна"]
STACK_2010 = {"послуги":[76.8,68.8,63.7,64.5,58.3], "промисловість":[19.4,27.9,26.1,31.2,27.5], "с/г":[1.1,0.9,8.4,3.1,8.9]}
STACK_2020 = {"послуги":[77.6,68.6,53.9,57.3,55.4], "промисловість":[18.6,27.5,32.5,34.2,24.0], "с/г":[0.9,0.7,6.7,2.5,10.2]}
 
 
#  діаграма 1: ВВП vs населення
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.scatter(POPULATION, GDP, color="steelblue", edgecolors="navy",
            alpha=0.8, s=80, zorder=3)
 
# підписи країн
for i, name in enumerate(NAMES):
    ax1.annotate(name, (POPULATION[i], GDP[i]),
                 fontsize=7, ha="left", va="bottom",
                 xytext=(3, 3), textcoords="offset points")
 
ax1.set_xlabel("Населення (млн)", fontsize=12)
ax1.set_ylabel("ВВП (млрд USD)", fontsize=12)
ax1.set_title("ВВП та населення країн ЄС (2020)", fontsize=14)
ax1.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.savefig("task2a_matplotlib.png", dpi=150)
plt.close()
 
# діаграма 2: ВВП/душу vs тривалість життя
# кольори та підписи для категорій
cat_colors = {1: "royalblue", 2: "darkorange", 3: "seagreen"}
cat_labels = {1: "до 1986", 2: "1986–2000", 3: "з 2004"}
 
fig2, ax2 = plt.subplots(figsize=(11, 7))
 
for cat in [1, 2, 3]:
    # індекси країн поточної категорії
    idx = [i for i, c in enumerate(CATEGORY) if c == cat]
    # розмір точок пропорційний витратам на здоров'я (масштабування)
    sizes = [HEALTH_EXP[i] / 15 for i in idx]
    sc = ax2.scatter(
        [GDP_PC[i]   for i in idx],
        [LIFE_EXP[i] for i in idx],
        s=sizes,
        color=cat_colors[cat],
        alpha=0.75,
        edgecolors="black",
        linewidths=0.5,
        label=f"Категорія {cat} ({cat_labels[cat]})",
        zorder=3
    )
 
# підписи країн
for i, name in enumerate(NAMES):
    ax2.annotate(name, (GDP_PC[i], LIFE_EXP[i]),
                 fontsize=7, ha="left", va="bottom",
                 xytext=(3, 2), textcoords="offset points")
 
# умовне позначення розміру точок
for size_val in [500, 2000, 5000]:
    ax2.scatter([], [], s=size_val / 15, color="gray", alpha=0.5,
                label=f"Здоров'я {size_val} USD/душу")
 
ax2.set_xlabel("ВВП на душу населення (USD)", fontsize=12)
ax2.set_ylabel("Середня тривалість життя (роки)", fontsize=12)
ax2.set_title("ВВП/душу vs тривалість життя, розмір = витрати на здоров'я (ЄС, 2020)", fontsize=13)
ax2.legend(fontsize=9, loc="lower right")
ax2.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.savefig("task2b_matplotlib.png", dpi=150)
plt.close()
 
print("збережено: task2a_matplotlib.png, task2b_matplotlib.png")
