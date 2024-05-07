import numpy as np

def rocket_height(t, T, m, cd, A, mi):
    g = 9.81  # Erdbeschleunigungskonstante in m/s^2
    def integrand1(t_prime):
        return np.log(mi / m(t_prime))
    def integrand2(t_prime):
        return (g * (T(t_prime) - m(t_prime) * g)) / (2 * cd * A * rho(t_prime) * (mi - m(t_prime)))
    
    def height_integral1(t):
        dt = 0.01  # Schrittweite für die numerische Integration
        t_values = np.arange(0, t, dt)
        integral = np.trapz(integrand1(t_values), t_values)
        return integral
    def height_integral2(t):
        dt = 0.01  # Schrittweite für die numerische Integration
        t_values = np.arange(0, t, dt)
        integral = np.trapz(integrand2(t_values), t_values)
        return integral
    
    h = (T(t) / (m(t) * g)) * height_integral1(t) - height_integral2(t)
    return h

# Beispielwerte für Funktionen: T, m, rho
def T(t):
    # Beispiel: lineare Abnahme der Schubkraft
    return 20000 - 100 * t

def m(t):
    # Beispiel: exponentielle Abnahme der Masse
    return 1000 * np.exp(-0.1 * t)

def rho(t):
    # Beispiel: konstante Luftdichte
    return 1.2

# Beispielwerte für Konstanten
cd = 0.75  # Strömungswiderstandsbeiwert
A = 10  # Querschnittsfläche der Rakete in m^2
mi = 10000  # Startmasse der Rakete in kg

# Zeitpunkt, zu dem die Flughöhe berechnet werden soll
t = 100  # Beispiel: Zeitpunkt 100 Sekunden nach dem Start

# Berechnung der Flughöhe
height = rocket_height(t, T, m, cd, A, mi)
print("Flughöhe der Rakete nach {} Sekunden: {} Meter".format(t, height))