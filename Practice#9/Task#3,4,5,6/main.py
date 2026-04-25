"""
завдання 3: горизонтальна стовпчикова діаграма ВВП/душу для країн 3-ї групи (2020).
завдання 4: групова стовпчикова діаграма ВВП/душу за 2010, 2015, 2020 для 5 країн.
завдання 5: три кругових діаграми структури ВВП за регіонами (світ, Європа, Україна).
завдання 6: групова стовпчикова з накопиченням (структура ВВП) за 2010, 2020 для 5 країн.
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


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


# =============================================================
# завдання 3: горизонтальна стовпчикова діаграма
# =============================================================
colors3 = cm.tab20.colors[:len(GROUP3_NAMES)]

fig3, ax3 = plt.subplots(figsize=(10, 7))
bars = ax3.barh(GROUP3_NAMES, GROUP3_GDPPC, color=colors3, edgecolor="black", height=0.6)

ax3.set_xlabel("ВВП на душу населення (USD)", fontsize=12)
ax3.set_ylabel("Країна", fontsize=12)
ax3.set_title("ВВП на душу населення — країни 3-ї групи ЄС (2020)", fontsize=13)
ax3.legend(bars, GROUP3_NAMES, fontsize=8, loc="lower right")
ax3.grid(axis="x", linestyle=":", alpha=0.6)
plt.tight_layout()
plt.savefig("task3_matplotlib.png", dpi=150)
plt.close()

# =============================================================
# завдання 4: групова стовпчикова діаграма
# =============================================================
x4 = np.arange(len(COUNTRIES_5))
width = 0.25   # ширина стовпця

fig4, ax4 = plt.subplots(figsize=(12, 6))
b1 = ax4.bar(x4 - width, GDP_PC_2010, width, label="2010", color="#4C72B0", edgecolor="black")
b2 = ax4.bar(x4,          GDP_PC_2015, width, label="2015", color="#DD8452", edgecolor="black")
b3 = ax4.bar(x4 + width,  GDP_PC_2020, width, label="2020", color="#55A868", edgecolor="black")

ax4.set_xticks(x4)
ax4.set_xticklabels(COUNTRIES_5, fontsize=11)
ax4.set_ylabel("ВВП на душу населення (USD)", fontsize=12)
ax4.set_title("ВВП на душу населення за 2010, 2015, 2020 рр.", fontsize=14)
ax4.legend(fontsize=11)
ax4.grid(axis="y", linestyle=":", alpha=0.6)
plt.tight_layout()
plt.savefig("task4_matplotlib.png", dpi=150)
plt.close()

# =============================================================
# завдання 5: три кругових діаграми
# =============================================================
fig5, axes5 = plt.subplots(1, 3, figsize=(18, 7))

# діаграма 1 — Світ, з відображенням часток на секторах
axes5[0].pie(PIE_WORLD_VALUES, labels=PIE_WORLD_LABELS,
             autopct="%1.1f%%", startangle=90,
             colors=cm.Set3.colors[:len(PIE_WORLD_LABELS)])
axes5[0].set_title("Структура ВВП — Світ (2020)", fontsize=12)

# діаграма 2 — Європа, з тінню (об'ємна)
axes5[1].pie(PIE_EUROPE_VALUES, labels=PIE_EUROPE_LABELS,
             shadow=True, startangle=90,
             colors=cm.Pastel1.colors[:len(PIE_EUROPE_LABELS)])
axes5[1].set_title("Структура ВВП — Європа (2020)", fontsize=12)

# діаграма 3 — Україна, розрізана
explode3 = [0.08] * len(PIE_UKRAINE_VALUES)
axes5[2].pie(PIE_UKRAINE_VALUES, labels=PIE_UKRAINE_LABELS,
             explode=explode3, startangle=90,
             colors=cm.Set2.colors[:len(PIE_UKRAINE_LABELS)])
axes5[2].set_title("Структура ВВП — Україна (2020)", fontsize=12)

plt.tight_layout()
plt.savefig("task5_matplotlib.png", dpi=150)
plt.close()

# =============================================================
# завдання 6: групова стовпчикова з накопиченням
# =============================================================
x6 = np.arange(len(STACK_COUNTRIES))
width6 = 0.35
sectors = list(STACK_2010.keys())
palette = {"послуги": "#5B9BD5", "промисловість": "#ED7D31", "с/г": "#70AD47"}

fig6, ax6 = plt.subplots(figsize=(13, 7))

for year_data, offset, year_label in [
    (STACK_2010, -width6 / 2, "2010"),
    (STACK_2020,  width6 / 2, "2020"),
]:
    bottom = np.zeros(len(STACK_COUNTRIES))
    for sector in sectors:
        values = np.array(year_data[sector])
        bars = ax6.bar(x6 + offset, values, width6,
                       bottom=bottom,
                       label=f"{sector} ({year_label})",
                       color=palette[sector],
                       alpha=0.85 if year_label == "2020" else 0.5,
                       edgecolor="black", linewidth=0.5)
        bottom += values

ax6.set_xticks(x6)
ax6.set_xticklabels(STACK_COUNTRIES, fontsize=11)
ax6.set_ylabel("Частка у ВВП (%)", fontsize=12)
ax6.set_title("Структура ВВП (2010 vs 2020)", fontsize=14)
ax6.legend(fontsize=9, ncol=2, loc="lower right")
ax6.grid(axis="y", linestyle=":", alpha=0.6)
plt.tight_layout()
plt.savefig("task6_matplotlib.png", dpi=150)
plt.close()

print("збережено: task3–task6 matplotlib png")