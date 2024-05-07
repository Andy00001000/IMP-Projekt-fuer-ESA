import time
import customtkinter as ctk
import time
import datetime
import tkinter as tk
import math
import numpy as np



def calculator_main():
    
    def calculate_and_plot(): 
        print("Test")

        dp = float(dp_entry.get().replace(",","."))
        ve = float(ve_entry.get().replace(",","."))
        dm = float(dm_entry.get().replace(",","."))
        dt = float(dt_entry.get().replace(",","."))
        cw = float(cw_entry.get().replace(",","."))
        p = float(p_entry.get().replace(",","."))
        A = float(A_entry.get().replace(",","."))
        v = float(v_entry.get().replace(",","."))
        h = float(h_entry.get().replace(",","."))
        p0 = float(p0_entry.get().replace(",","."))
        g = float(g_entry.get().replace(",","."))
        M = float(M_entry.get().replace(",","."))
        R = float(R_entry.get().replace(",","."))
        varm = float(varm_entry.get().replace(",","."))
        T = float(T_entry.get().replace(",","."))
        a = float(a_entry.get().replace(",","."))
        s = float(s_entry.get().replace(",","."))
        FL = float(FL_entry.get().replace(",","."))
        F = float(F_entry.get().replace(",","."))
        G = float(G_entry.get().replace(",","."))
        m = float(m_entry.get().replace(",","."))
        ME = float(ME_entry.get().replace(",","."))
        e = float(e_entry.get().replace(",","."))
        r = float(r_entry.get().replace(",","."))
        ml = float(ml_entry.get().replace(",","."))
        mN = float(mN_entry.get().replace(",","."))
        mT = float(mT_entry.get().replace(",","."))
        mP = float(mP_entry.get().replace(",","."))

        #Konstanten
        """"
        p0 = 1.225 #kg pro m^3
        g = 9.81
        R = #scipy.R
        G = 
        e = 
        """
        # Konstanten
        p0 = 1.225  # kg pro m^3
        g = 9.81
        R = 287.05  # J/(kg*K)
        G = (6.67430*math.e)-11  # m^3/(kg*s^2)
        e = math.e

        #I Newton
        dp = dm * ve

        #B Pascal

        temp1 = -((g*M*h) / (R*T))

        p = p0*pow(math.e, temp1)

        FL = 1/2*cw*p*A*v*v

        #W Braun
        dmT = -mP * dt

        mT = mT - dmT

        m = ml + mN + mT

        #Galileo Galilei
        F = G * ((ME*m)/(r*r))

        g = (G * M)/(r*r)

        def rocket_height(t, T, m, cd, A, mi):
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

        



    def button_callback():
        print("button clicked")
        calcapp.destroy()
        import main_ui

    def calculate_button():
        print("button clicked")
        calculate_and_plot()
        

    calcapp = ctk.CTk()
    calcapp.geometry("400x150")

    #constants:
    








    dp_label = ctk.CTkLabel(calcapp, text="Delta Impuls:") #delta impuls
    dp_label.grid(row=0, column=0)
    dp_entry = ctk.CTkEntry(calcapp)
    dp_entry.grid(row=0, column=1)

    ve_label = ctk.CTkLabel(calcapp, text="Geschwindigkeit des Ausströmenden gases:") #Geschwindigkeit
    ve_label.grid(row=1, column=0)
    ve_entry = ctk.CTkEntry(calcapp)
    ve_entry.grid(row=1, column=1)

    dm_label = ctk.CTkLabel(calcapp, text="Delta Masse:") #delta masse
    dm_label.grid(row=2, column=0)
    dm_entry = ctk.CTkEntry(calcapp)
    dm_entry.grid(row=2, column=1)

    dt_label = ctk.CTkLabel(calcapp, text="Delta Zeit:") #delta zeit
    dt_label.grid(row=3, column=0)
    dt_entry = ctk.CTkEntry(calcapp)
    dt_entry.grid(row=3, column=1)

    cw_label = ctk.CTkLabel(calcapp, text="Strömungswiderstandsbeiwert:") #Strömungswiderstandsbeiwert
    cw_label.grid(row=4, column=0)
    cw_entry = ctk.CTkEntry(calcapp)
    cw_entry.grid(row=4, column=1)

    p_label = ctk.CTkLabel(calcapp, text="Luftdichte:") #Luftdichte
    p_label.grid(row=5, column=0)
    p_entry = ctk.CTkEntry(calcapp)
    p_entry.grid(row=5, column=1)

    A_label = ctk.CTkLabel(calcapp, text="Frontfläche:") #Frontfläche
    A_label.grid(row=6, column=0)
    A_entry = ctk.CTkEntry(calcapp)
    A_entry.grid(row=6, column=1)

    v_label = ctk.CTkLabel(calcapp, text="Geschwindigkeit:") #Geschwindigkeit
    v_label.grid(row=7, column=0)
    v_entry = ctk.CTkEntry(calcapp)
    v_entry.grid(row=7, column=1)

    h_label = ctk.CTkLabel(calcapp, text="Höhe:") #Höhe
    h_label.grid(row=8, column=0)
    h_entry = ctk.CTkEntry(calcapp)
    h_entry.grid(row=8, column=1)

    p0_label = ctk.CTkLabel(calcapp, text="Luftdichte:") #Luftdichte auf Meereshöhe
    p0_label.grid(row=9, column=0)
    p0_entry = ctk.CTkEntry(calcapp)
    p0_entry.grid(row=9, column=1)

    g_label = ctk.CTkLabel(calcapp, text="Erdbeschleunigung:") #Erdbeschleunigung
    g_label.grid(row=10, column=0)
    g_entry = ctk.CTkEntry(calcapp)
    g_entry.grid(row=10, column=1)

    M_label = ctk.CTkLabel(calcapp, text="Die mittlere molare Masse der Luft:") #M die mittlere molare Masse der Luft
    M_label.grid(row=11, column=0)
    M_entry = ctk.CTkEntry(calcapp)
    M_entry.grid(row=11, column=1)

    R_label = ctk.CTkLabel(calcapp, text="Die allgemeine Gaskonstante:") #die allgemeine Gaskonstante
    R_label.grid(row=12, column=0)
    R_entry = ctk.CTkEntry(calcapp)
    R_entry.grid(row=12, column=1)

    varm_label = ctk.CTkLabel(calcapp, text="Geschwindigkeit:") #Geschwindigkeit von Armstrong
    varm_label.grid(row=13, column=0)
    varm_entry = ctk.CTkEntry(calcapp)
    varm_entry.grid(row=13, column=1)

    T_label = ctk.CTkLabel(calcapp, text="Temperatur der Luft:") #Temperatur der Luft
    T_label.grid(row=14, column=0)
    T_entry = ctk.CTkEntry(calcapp)
    T_entry.grid(row=14, column=1)

    a_label = ctk.CTkLabel(calcapp, text="Beschleunigung:") #Beschleunigung
    a_label.grid(row=15, column=0)
    a_entry = ctk.CTkEntry(calcapp)
    a_entry.grid(row=15, column=1)

    s_label = ctk.CTkLabel(calcapp, text="Zurückgelegte Strecke:") #Zurückgelegte Strecke s
    s_label.grid(row=16, column=0)
    s_entry = ctk.CTkEntry(calcapp)
    s_entry.grid(row=16, column=1)

    FL_label = ctk.CTkLabel(calcapp, text="Luftwiederstand:") #Luftwiederstand
    FL_label.grid(row=17, column=0)
    FL_entry = ctk.CTkEntry(calcapp)
    FL_entry.grid(row=17, column=1)

    F_label = ctk.CTkLabel(calcapp, text="Gravitationskraft:") #Gravitationskraft
    F_label.grid(row=18, column=0)
    F_entry = ctk.CTkEntry(calcapp)
    F_entry.grid(row=18, column=1)

    G_label = ctk.CTkLabel(calcapp, text="Gravitationskonstante:") #Gravitationskonstante
    G_label.grid(row=19, column=0)
    G_entry = ctk.CTkEntry(calcapp)
    G_entry.grid(row=19, column=1)

    m_label = ctk.CTkLabel(calcapp, text="Masse des Objekts:") #Masse des Objekts
    m_label.grid(row=20, column=0)
    m_entry = ctk.CTkEntry(calcapp)
    m_entry.grid(row=20, column=1)

    ME_label = ctk.CTkLabel(calcapp, text="Masse der Erde:") #Masse der Erde
    ME_label.grid(row=21, column=0)
    ME_entry = ctk.CTkEntry(calcapp)
    ME_entry.grid(row=21, column=1)

    e_label = ctk.CTkLabel(calcapp, text="konstante Exponentialfunktion:") #konstante Exponentialfunktion
    e_label.grid(row=22, column=0)
    e_entry = ctk.CTkEntry(calcapp)
    e_entry.grid(row=22, column=1)

    r_label = ctk.CTkLabel(calcapp, text="Abstand Objekt bis Mittelpunkt zur Erde:") #Abstand Objekt bis Mittelpunkt zur Erde
    r_label.grid(row=23, column=0)
    r_entry = ctk.CTkEntry(calcapp)
    r_entry.grid(row=23, column=1)

    ml_label = ctk.CTkLabel(calcapp, text="Leerlaufmasse der Rakete:") #Leerlaufmasse der Rakete
    ml_label.grid(row=24, column=0)
    ml_entry = ctk.CTkEntry(calcapp)
    ml_entry.grid(row=24, column=1)

    mN_label = ctk.CTkLabel(calcapp, text="Nutzlastmasse:") #Nutzlastmasse
    mN_label.grid(row=25, column=0)
    mN_entry = ctk.CTkEntry(calcapp)
    mN_entry.grid(row=25, column=1)

    mT_label = ctk.CTkLabel(calcapp, text="Treibstoffmasse:") #Treibstoffmasse
    mT_label.grid(row=26, column=0)
    mT_entry = ctk.CTkEntry(calcapp)
    mT_entry.grid(row=26, column=1)

    mP_label = ctk.CTkLabel(calcapp, text="Massenfluss des Treibstoffs:") #Massenfluss des Treibstoffs
    mP_label.grid(row=27, column=0)
    mP_entry = ctk.CTkEntry(calcapp)
    mP_entry.grid(row=27, column=1)

    

    button = ctk.CTkButton(calcapp, text="Home", command=button_callback)
    calcbutton = ctk.CTkButton(calcapp, text="Calculate", command=calculate_button)



    calcbutton.grid(row = 28, column=1)
    button.grid(row = 29, column=1)

    calcapp.mainloop()



