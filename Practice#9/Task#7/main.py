"""
завдання 7:
виконати пп. 1–6 з використанням бібліотек plotly та seaborn.
plotly — інтерактивні html-графіки.
seaborn — статистична візуалізація поверх matplotlib.
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

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


# ============================================================
# PLOTLY — завдання 1: тригонометричні функції
# ============================================================
x = np.arange(-2 * np.pi, 2 * np.pi + 0.5, 0.5)
fig_p1 = go.Figure()
fig_p1.add_trace(go.Scatter(x=x, y=np.sin(x),      mode="lines+markers",
                            name="y1 = sin(x)",       line=dict(color="royalblue", dash="solid")))
fig_p1.add_trace(go.Scatter(x=x, y=np.sin(2*x/4),  mode="lines+markers",
                            name="y2 = sin(2x/4)",    line=dict(color="tomato",     dash="dash")))
fig_p1.add_trace(go.Scatter(x=x, y=np.cos(3*x/3),  mode="lines+markers",
                            name="y3 = cos(3x/3)",    line=dict(color="seagreen",   dash="dot")))
fig_p1.update_layout(title="Тригонометричні функції (Plotly)",
                     xaxis_title="x", yaxis_title="y",
                     width=900, height=500)
fig_p1.write_html("task1_plotly.html")

# ============================================================
# PLOTLY — завдання 2: scatter діаграми
# ============================================================
df_eu = pd.DataFrame({
    "Країна": NAMES, "ВВП": GDP, "Населення": POPULATION,
    "ВВП/душу": GDP_PC, "Тривалість": LIFE_EXP,
    "Здоров'я": HEALTH_EXP, "Категорія": [str(c) for c in CATEGORY],
    "Рік вступу": JOIN_YEAR
})

# scatter 1: ВВП vs населення
fig_p2a = px.scatter(df_eu, x="Населення", y="ВВП", text="Країна",
                     title="ВВП vs Населення ЄС (2020, Plotly)",
                     labels={"Населення": "Населення (млн)", "ВВП": "ВВП (млрд USD)"})
fig_p2a.update_traces(textposition="top center")
fig_p2a.write_html("task2a_plotly.html")

# scatter 2: ВВП/душу vs тривалість + категорія + розмір
fig_p2b = px.scatter(df_eu, x="ВВП/душу", y="Тривалість",
                     color="Категорія", size="Здоров'я", text="Країна",
                     title="ВВП/душу vs Тривалість життя (Plotly)",
                     labels={"ВВП/душу": "ВВП/душу (USD)",
                             "Тривалість": "Тривалість життя (роки)",
                             "Здоров'я": "Витрати на здоров'я (USD/душу)"},
                     color_discrete_map={"1": "royalblue", "2": "darkorange", "3": "seagreen"})
fig_p2b.update_traces(textposition="top center")
fig_p2b.write_html("task2b_plotly.html")

# ============================================================
# PLOTLY — завдання 3: горизонтальна стовпчикова
# ============================================================
fig_p3 = px.bar(x=GROUP3_GDPPC, y=GROUP3_NAMES, orientation="h",
                title="ВВП на душу — країни 3-ї групи ЄС (2020, Plotly)",
                labels={"x": "ВВП/душу (USD)", "y": "Країна"},
                color=GROUP3_NAMES)
fig_p3.write_html("task3_plotly.html")

# ============================================================
# PLOTLY — завдання 4: групова стовпчикова
# ============================================================
fig_p4 = go.Figure()
for values, year, color in [
    (GDP_PC_2010, "2010", "#4C72B0"),
    (GDP_PC_2015, "2015", "#DD8452"),
    (GDP_PC_2020, "2020", "#55A868"),
]:
    fig_p4.add_trace(go.Bar(name=year, x=COUNTRIES_5, y=values,
                            marker_color=color))
fig_p4.update_layout(barmode="group",
                     title="ВВП на душу 2010/2015/2020 (Plotly)",
                     yaxis_title="ВВП/душу (USD)", width=900)
fig_p4.write_html("task4_plotly.html")

# ============================================================
# PLOTLY — завдання 5: три кругових діаграми
# ============================================================
fig_p5 = make_subplots(rows=1, cols=3, specs=[[{"type": "pie"}] * 3],
                       subplot_titles=["Світ", "Європа", "Україна"])
fig_p5.add_trace(go.Pie(labels=PIE_WORLD_LABELS,   values=PIE_WORLD_VALUES,
                         textinfo="label+percent", hole=0),    row=1, col=1)
fig_p5.add_trace(go.Pie(labels=PIE_EUROPE_LABELS,  values=PIE_EUROPE_VALUES,
                         textinfo="label", hole=0.3),          row=1, col=2)
fig_p5.add_trace(go.Pie(labels=PIE_UKRAINE_LABELS, values=PIE_UKRAINE_VALUES,
                         pull=[0.08]*5, textinfo="label"),     row=1, col=3)
fig_p5.update_layout(title="Структура ВВП (2020, Plotly)", width=1200, height=500)
fig_p5.write_html("task5_plotly.html")

# ============================================================
# PLOTLY — завдання 6: групова з накопиченням
# ============================================================
fig_p6 = go.Figure()
palette6 = {"послуги": "#5B9BD5", "промисловість": "#ED7D31", "с/г": "#70AD47"}
for sector in STACK_2010:
    fig_p6.add_trace(go.Bar(name=f"{sector} 2010", x=STACK_COUNTRIES,
                            y=STACK_2010[sector], marker_color=palette6[sector],
                            opacity=0.5))
    fig_p6.add_trace(go.Bar(name=f"{sector} 2020", x=STACK_COUNTRIES,
                            y=STACK_2020[sector], marker_color=palette6[sector],
                            opacity=0.9))
fig_p6.update_layout(barmode="stack",
                     title="Структура ВВП 2010 vs 2020 (Plotly)",
                     yaxis_title="Частка (%)", width=1000)
fig_p6.write_html("task6_plotly.html")

print("plotly html-файли збережено.")

# ============================================================
# SEABORN — завдання 1: тригонометричні функції
# ============================================================
sns.set_theme(style="darkgrid")
fig_s1, ax_s1 = plt.subplots(figsize=(12, 5))
ax_s1.plot(x, np.sin(x),     label="y1=sin(x)",     marker="o", markersize=4)
ax_s1.plot(x, np.sin(2*x/4), label="y2=sin(2x/4)",  marker="s", markersize=4, linestyle="--")
ax_s1.plot(x, np.cos(3*x/3), label="y3=cos(3x/3)",  marker="^", markersize=4, linestyle="-.")
ax_s1.set_title("Тригонометричні функції (Seaborn)", fontsize=14)
ax_s1.set_xlabel("x"); ax_s1.set_ylabel("y")
ax_s1.legend()
plt.tight_layout()
plt.savefig("task1_seaborn.png", dpi=150)
plt.close()

# ============================================================
# SEABORN — завдання 2: scatter діаграми
# ============================================================
cat_labels_map = {"1": "до 1986", "2": "1986–2000", "3": "з 2004"}
df_eu["Категорія_label"] = df_eu["Категорія"].map(cat_labels_map)

fig_s2a, ax_s2a = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df_eu, x="Населення", y="ВВП", ax=ax_s2a,
                color="steelblue", s=100, edgecolor="navy")
for _, row in df_eu.iterrows():
    ax_s2a.annotate(row["Країна"], (row["Населення"], row["ВВП"]), fontsize=7,
                    xytext=(3, 3), textcoords="offset points")
ax_s2a.set_title("ВВП vs Населення (Seaborn)")
plt.tight_layout(); plt.savefig("task2a_seaborn.png", dpi=150); plt.close()

fig_s2b, ax_s2b = plt.subplots(figsize=(11, 7))
# розмір через sizes — нормалізуємо витрати на здоров'я
sns.scatterplot(data=df_eu, x="ВВП/душу", y="Тривалість",
                hue="Категорія_label", size="Здоров'я",
                sizes=(50, 500), alpha=0.8, ax=ax_s2b, edgecolor="black")
for _, row in df_eu.iterrows():
    ax_s2b.annotate(row["Країна"], (row["ВВП/душу"], row["Тривалість"]),
                    fontsize=7, xytext=(3, 2), textcoords="offset points")
ax_s2b.set_title("ВВП/душу vs Тривалість життя (Seaborn)")
ax_s2b.legend(fontsize=9, loc="lower right")
plt.tight_layout(); plt.savefig("task2b_seaborn.png", dpi=150); plt.close()

# ============================================================
# SEABORN — завдання 3: горизонтальна стовпчикова
# ============================================================
df_g3 = pd.DataFrame({"Країна": GROUP3_NAMES, "ВВП/душу": GROUP3_GDPPC})
fig_s3, ax_s3 = plt.subplots(figsize=(10, 7))
sns.barplot(data=df_g3, x="ВВП/душу", y="Країна", hue="Країна", palette="tab20", legend=False,
            ax=ax_s3, edgecolor="black")
ax_s3.set_title("ВВП/душу — країни 3-ї групи (Seaborn)")
plt.tight_layout(); plt.savefig("task3_seaborn.png", dpi=150); plt.close()

# ============================================================
# SEABORN — завдання 4: групова стовпчикова
# ============================================================
df4 = pd.DataFrame({
    "Країна": COUNTRIES_5 * 3,
    "ВВП/душу": GDP_PC_2010 + GDP_PC_2015 + GDP_PC_2020,
    "Рік": ["2010"] * 5 + ["2015"] * 5 + ["2020"] * 5
})
fig_s4, ax_s4 = plt.subplots(figsize=(12, 6))
sns.barplot(data=df4, x="Країна", y="ВВП/душу", hue="Рік",
            palette=["#4C72B0", "#DD8452", "#55A868"], ax=ax_s4, edgecolor="black")
ax_s4.set_title("ВВП/душу за 2010/2015/2020 (Seaborn)")
ax_s4.set_ylabel("ВВП/душу (USD)")
plt.tight_layout(); plt.savefig("task4_seaborn.png", dpi=150); plt.close()

# ============================================================
# SEABORN — завдання 5: кругові (seaborn не підтримує pie,
# використовуємо matplotlib з sns палітрами)
# ============================================================
sns.set_palette("Set2")
fig_s5, axes_s5 = plt.subplots(1, 3, figsize=(18, 7))
pal1 = sns.color_palette("Set3",  len(PIE_WORLD_VALUES))
pal2 = sns.color_palette("Pastel1", len(PIE_EUROPE_VALUES))
pal3 = sns.color_palette("Set2",  len(PIE_UKRAINE_VALUES))

axes_s5[0].pie(PIE_WORLD_VALUES,   labels=PIE_WORLD_LABELS,   autopct="%1.1f%%", colors=pal1)
axes_s5[0].set_title("Світ (2020)")
axes_s5[1].pie(PIE_EUROPE_VALUES,  labels=PIE_EUROPE_LABELS,  shadow=True,       colors=pal2)
axes_s5[1].set_title("Європа (2020)")
axes_s5[2].pie(PIE_UKRAINE_VALUES, labels=PIE_UKRAINE_LABELS,
               explode=[0.08]*5, colors=pal3)
axes_s5[2].set_title("Україна (2020)")
plt.suptitle("Структура ВВП (Seaborn палітра)", fontsize=14)
plt.tight_layout(); plt.savefig("task5_seaborn.png", dpi=150); plt.close()

# ============================================================
# SEABORN — завдання 6: stacked bar через pandas + seaborn палітру
# ============================================================
sectors = list(STACK_2010.keys())
pal6 = sns.color_palette("muted", 3)

fig_s6, axes_s6 = plt.subplots(1, 2, figsize=(14, 6), sharey=True)
for ax, year_data, year_lbl in [
    (axes_s6[0], STACK_2010, "2010"),
    (axes_s6[1], STACK_2020, "2020"),
]:
    bottom = np.zeros(len(STACK_COUNTRIES))
    for j, sector in enumerate(sectors):
        vals = np.array(year_data[sector])
        ax.bar(STACK_COUNTRIES, vals, bottom=bottom,
               color=pal6[j], label=sector, edgecolor="black", linewidth=0.5)
        bottom += vals
    ax.set_title(f"Структура ВВП {year_lbl} (Seaborn)", fontsize=12)
    ax.set_ylabel("Частка (%)")
    ax.legend(fontsize=9)
plt.tight_layout(); plt.savefig("task6_seaborn.png", dpi=150); plt.close()

print("seaborn/matplotlib png-файли збережено.")