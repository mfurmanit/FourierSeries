import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Parametr indywidualny, numer albumu - 160732
p = 1.320

# Okres
T = 2

# Pulsacja lub częstość kołowa
w = 2 * np.pi / T


# Definicje funkcji
def s(t):
    return p * t ** 2


def s1(t):
    return s(t) * np.cos(np.pi * t)


def s2(t):
    return s(t) * np.cos(2 * np.pi * t)


# Definicje współczynników
# bN = 0 bo funkcja jest parzysta

a0 = 2 / T * quad(s, -1, 1)[0]
a1 = 2 / T * quad(s1, -1, 1)[0]
a2 = 2 / T * quad(s2, -1, 1)[0]


# Funkcja wyznaczająca szereg Fouriera
def fourierSeries(t):
    fourier = a0 / 2 + a1 * np.cos(np.pi * t) + a2 * np.cos(2 * np.pi * t)
    return fourier


# Wypisanie wspólczynników
print("Współczynnik a0 jest równy " + str(a0))
print("Współczynnik a1 jest równy " + str(a1))
print("Współczynnik a2 jest równy " + str(a2))

# Rysowanie wykresu w przedziale (-3,3)
t = np.linspace(-3, 3, 100)
fig, ax = plt.subplots()
ax.plot(t, s(t), t, fourierSeries(t))
ax.grid(True)
ax.legend(['Bazowa', 'Aproksymacja'])
ax.set_title('Wykresy funkcji')
plt.show()
