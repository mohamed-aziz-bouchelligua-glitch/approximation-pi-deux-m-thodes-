from math import sqrt, pi

EPS = 10**-6

# Methode de Viete
a = sqrt(2)
p = a / 2
pi_viete = 2 / p
ancien_pi = 0

while abs(pi_viete - ancien_pi) > EPS:
    ancien_pi = pi_viete
    a = sqrt(2 + a)
    p = p * a / 2
    pi_viete = 2 / p

# Methode de Brent-Salamin
a = 1
b = 1 / sqrt(2)
t = 1 / 4
p = 1
pi_brent = (a + b)**2 / (4*t)
ancien_pi = 0

while abs(pi_brent - ancien_pi) > EPS:
    ancien_pi = pi_brent
    ancien_a = a
    a = (a + b) / 2
    b = sqrt(ancien_a * b)
    t = t - p * (ancien_a - a)**2
    p = 2 * p
    pi_brent = (a + b)**2 / (4*t)

print("Pi par Viete :", pi_viete)
print("Pi par Brent-Salamin :", pi_brent)
print("Valeur de reference :", pi)
