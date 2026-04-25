"""
завдання 1:
побудувати в одній системі координат лінійні графіки функцій:
    y1 = sin(x)
    y2 = sin(2x / 4)
    y3 = cos(3x / 3)
на інтервалі x ∈ [-2π; 2π] з кроком 0.5.
використовуючи параметри діаграми:
 - додати лінії сітки та маркери;
 - додати легенду та текст анотації;
 - змінити колір ліній;
 - змінити стиль ліній та розмір графіку.
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import numpy as np
import matplotlib.pyplot as plt

# масив значень x з кроком 0.5 на інтервалі [-2π, 2π]
x = np.arange(-2 * np.pi, 2 * np.pi + 0.5, 0.5)

# обчислення функцій
y1 = np.sin(x)
y2 = np.sin(2 * x / 4)
y3 = np.cos(3 * x / 3)

# розмір фігури
fig, ax = plt.subplots(figsize=(12, 6))

# побудова графіків з різними кольорами, стилями ліній та маркерами
ax.plot(x, y1, color="royalblue",  linestyle="-",  marker="o", markersize=5, label=r"$y_1 = \sin(x)$")
ax.plot(x, y2, color="tomato",     linestyle="--", marker="s", markersize=5, label=r"$y_2 = \sin(2x/4)$")
ax.plot(x, y3, color="seagreen",   linestyle="-.", marker="^", markersize=5, label=r"$y_3 = \cos(3x/3)$")

# сітка
ax.grid(True, linestyle=":", alpha=0.7)

# підписи осей та заголовок
ax.set_xlabel("x", fontsize=13)
ax.set_ylabel("y", fontsize=13)
ax.set_title("Графіки тригонометричних функцій", fontsize=15)

# легенда
ax.legend(fontsize=12)

# текст анотації у точці максимуму y1
max_idx = np.argmax(y1)
ax.annotate(
    f"max y1 = {y1[max_idx]:.2f}",
    xy=(x[max_idx], y1[max_idx]),
    xytext=(x[max_idx] + 0.5, y1[max_idx] - 0.3),
    arrowprops=dict(arrowstyle="->", color="royalblue"),
    fontsize=10,
    color="royalblue"
)

plt.tight_layout()
plt.savefig("task1_matplotlib.png", dpi=150)
plt.show()
print("графік збережено: task1_matplotlib.png")