import customtkinter as ctk
import math
import numpy as np
import matplotlib.pyplot as plt

def calculator_main():
    
    def calculate_and_plot():
        # Eingabewerte aus den Feldern lesen und konvertieren
        mP = float(mP_entry.get().replace(",", "."))
        t_total = float(t_total_entry.get().replace(",", "."))
        cw = float(cw_entry.get().replace(",", "."))
        A = float(A_entry.get().replace(",", "."))
        v = float(v_entry.get().replace(",", "."))
        h = float(h_entry.get().replace(",", "."))
        T = float(T_entry.get().replace(",", "."))
        m = float(m_entry.get().replace(",", "."))
        ME = float(ME_entry.get().replace(",", "."))
        r = float(r_entry.get().replace(",", "."))
        ml = float(ml_entry.get().replace(",", "."))
        mN = float(mN_entry.get().replace(",", "."))
        mT = float(mT_entry.get().replace(",", "."))

        # Konstanten
        p0 = 1.225  # kg/m^3
        g = 9.81  # m/s^2
        R = 287.05  # J/(kg*K)
        G = 6.67430e-11  # m^3/(kg*s^2)

        # Berechnungen
        dt = t_total / 1000  # Delta Zeit
        dm = mP * dt  # Delta Masse

        # Initialisierung der Listen für Zeit, Höhe und Geschwindigkeit
        times = [0]
        heights = [h]
        velocities = [v]

        while mT > 0 and heights[-1] >= 0:
            # Berechnung der Luftdichte in der aktuellen Höhe
            p = p0 * math.exp(-((g * ME * heights[-1]) / (R * T)))

            # Berechnung des Luftwiderstandes
            FL = 0.5 * cw * p * A * velocities[-1] ** 2

            # Schubkraft
            dp = dm * velocities[-1] / dt

            # Gravitationskraft
            F_gravity = m * g

            # Gesamtkraft
            F_net = dp - FL - F_gravity

            # Beschleunigung
            a = F_net / m

            # Geschwindigkeits- und Höhenänderung
            new_velocity = velocities[-1] + a * dt
            new_height = heights[-1] + new_velocity * dt

            # Neue Zeit
            new_time = times[-1] + dt

            # Update der Treibstoffmasse
            mT -= mP * dt
            m = ml + mN + mT

            # Speichern der neuen Zeit, Höhe und Geschwindigkeit
            times.append(new_time)
            heights.append(new_height)
            velocities.append(new_velocity)

        # Plot des Höhe-Zeit-Diagramms
        plt.figure(figsize=(10, 6))
        plt.subplot(2, 1, 1)
        plt.plot(times, heights, marker='o', linestyle='-', color='b')
        plt.title('Höhe-Zeit-Diagramm')
        plt.xlabel('Zeit (s)')
        plt.ylabel('Höhe (m)')
        plt.grid(True)

        # Plot des Geschwindigkeits-Zeit-Diagramms
        plt.subplot(2, 1, 2)
        plt.plot(times, velocities, marker='o', linestyle='-', color='r')
        plt.title('Geschwindigkeit-Zeit-Diagramm')
        plt.xlabel('Zeit (s)')
        plt.ylabel('Geschwindigkeit (m/s)')
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    def button_callback():
        print("button clicked")
        calcapp.destroy()
        import main_ui

    def calculate_button():
        print("button clicked")
        calculate_and_plot()

    calcapp = ctk.CTk()
    calcapp.geometry("400x600")

    # Eingabefelder und Labels
    t_total_label = ctk.CTkLabel(calcapp, text="Gesamtzeit (s):")
    t_total_label.grid(row=0, column=0)
    t_total_entry = ctk.CTkEntry(calcapp)
    t_total_entry.grid(row=0, column=1)

    cw_label = ctk.CTkLabel(calcapp, text="Strömungswiderstandsbeiwert:")
    cw_label.grid(row=1, column=0)
    cw_entry = ctk.CTkEntry(calcapp)
    cw_entry.grid(row=1, column=1)

    A_label = ctk.CTkLabel(calcapp, text="Frontfläche (m^2):")
    A_label.grid(row=2, column=0)
    A_entry = ctk.CTkEntry(calcapp)
    A_entry.grid(row=2, column=1)

    v_label = ctk.CTkLabel(calcapp, text="Anfangsgeschwindigkeit (m/s):")
    v_label.grid(row=3, column=0)
    v_entry = ctk.CTkEntry(calcapp)
    v_entry.grid(row=3, column=1)

    h_label = ctk.CTkLabel(calcapp, text="Anfangshöhe (m):")
    h_label.grid(row=4, column=0)
    h_entry = ctk.CTkEntry(calcapp)
    h_entry.grid(row=4, column=1)

    T_label = ctk.CTkLabel(calcapp, text="Temperatur der Luft (K):")
    T_label.grid(row=5, column=0)
    T_entry = ctk.CTkEntry(calcapp)
    T_entry.grid(row=5, column=1)

    m_label = ctk.CTkLabel(calcapp, text="Gesamtmasse (kg):")
    m_label.grid(row=6, column=0)
    m_entry = ctk.CTkEntry(calcapp)
    m_entry.grid(row=6, column=1)

    ME_label = ctk.CTkLabel(calcapp, text="Masse der Erde (kg):")
    ME_label.grid(row=7, column=0)
    ME_entry = ctk.CTkEntry(calcapp)
    ME_entry.grid(row=7, column=1)

    r_label = ctk.CTkLabel(calcapp, text="Abstand Objekt bis Mittelpunkt zur Erde (m):")
    r_label.grid(row=8, column=0)
    r_entry = ctk.CTkEntry(calcapp)
    r_entry.grid(row=8, column=1)

    ml_label = ctk.CTkLabel(calcapp, text="Leerlaufmasse der Rakete (kg):")
    ml_label.grid(row=9, column=0)
    ml_entry = ctk.CTkEntry(calcapp)
    ml_entry.grid(row=9, column=1)

    mN_label = ctk.CTkLabel(calcapp, text="Nutzlastmasse (kg):")
    mN_label.grid(row=10, column=0)
    mN_entry = ctk.CTkEntry(calcapp)
    mN_entry.grid(row=10, column=1)

    mT_label = ctk.CTkLabel(calcapp, text="Treibstoffmasse (kg):")
    mT_label.grid(row=11, column=0)
    mT_entry = ctk.CTkEntry(calcapp)
    mT_entry.grid(row=11, column=1)

    mP_label = ctk.CTkLabel(calcapp, text="Massenfluss des Treibstoffs (kg/s):")
    mP_label.grid(row=12, column=0)
    mP_entry = ctk.CTkEntry(calcapp)
    mP_entry.grid(row=12, column=1)

    button = ctk.CTkButton(calcapp, text="Home", command=button_callback)
    calcbutton = ctk.CTkButton(calcapp, text="Calculate", command=calculate_button)

    calcbutton.grid(row=13, column=1)
    button.grid(row=14, column=1)

    calcapp.mainloop()

if __name__ == "__main__":
    calculator_main()
