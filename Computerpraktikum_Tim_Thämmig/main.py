import random
import matplotlib.pyplot as plot
import pandas
import numpy
import matplotlib.animation as animation
from tkinter import *

import Helper
import person
import visual


#   VERSION 2.5.0 Final Version

#   Python 3.13
#   mathplotlib 3.10.8
#   numpy 2.3.5
#   pandas 2.3.3


def __main__(ITERATIONEN, WIDTH, HEIGHT, INFECTION_RATE, INFECTION_RATE_INF, VACC_START, VACCINATION_RATE, GENESUNGS_RATE, DEATH_RATE, INFECTION_RATE_PERSON, mu_2, sigma_2, QUARANTANE, HERDENIMMUNITAT, anz_agenten):

    #STATIC VARIABLES

    INFECTION_RATE_IF_VACC = 0.36       # alpha‾
    RATE_NATURAL_DEATH = 0.000034        # gamma 3^

    # INITIALISING AGENTS

    students = [person.Person(0, random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1), Helper.age_setter(), INFECTION_RATE_PERSON, 0, 0) for _ in range(anz_agenten)]

    for i in range(1):
        students.append(person.Person(1, random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1), 40, 1, 0, 1))

    #ADDITIONAL DATASTRUCTURES

    kranke = [0]*ITERATIONEN
    gesunde = [0]*ITERATIONEN
    tote = [0]*ITERATIONEN
    geimpfte = [0]*ITERATIONEN

    # DATEN AUSLESEN AUS EXCEL TABELLE

    todesdaten_alter = pandas.read_excel("statistischer-bericht-sterbefaelle-2022.ods", sheet_name="12613-02", usecols="A, B", skiprows=4)
    todesdaten_alter_array = todesdaten_alter.to_numpy()
    todesdaten_alter_wk = Helper.excel_to_wk(todesdaten_alter_array)

    # INITIALISING PLOT/ANIMATION

    fig_geskra = plot.figure()
    ax_geskra = fig_geskra.add_subplot(2, 2, 1)     # x,y,z heißt x*y großes feld, z'ter subplot
    ax_feld = fig_geskra.add_subplot(2, 2, 2)

    #SZENARIEN

    if HERDENIMMUNITAT != -1:
        person.herdenimmunitat(students, HERDENIMMUNITAT)

    # CALL ANIMATION FUNCTION

    ani = animation.FuncAnimation(fig_geskra, visual.update, fargs=(WIDTH, HEIGHT, students, kranke, gesunde, tote, geimpfte, todesdaten_alter_wk, RATE_NATURAL_DEATH, ax_geskra, ax_feld, VACC_START, VACCINATION_RATE, GENESUNGS_RATE, DEATH_RATE, INFECTION_RATE, INFECTION_RATE_INF, INFECTION_RATE_IF_VACC, QUARANTANE, HERDENIMMUNITAT, ITERATIONEN, mu_2, sigma_2), frames=ITERATIONEN, interval=0, repeat=False)

    plot.show()


def read_input_field():

    ITERATIONEN = int(eingabefeld_iterationen.get())
    b = int(eingabefeld_b.get())
    h = int(eingabefeld_h.get())
    alpha = float(eingabefeld_alpha.get())
    beta = float(eingabefeld_beta.get())
    gamma_1 = float(eingabefeld_gamma_1.get())
    gamma_2 = float(eingabefeld_gamma_2.get())
    kappa = int(eingabefeld_kappa.get())
    delta = float(eingabefeld_delta.get())
    mu_2 = float(eingabefeld_mu_2.get())
    sigma_2 = float(eingabefeld_sigma_2.get())

    anz_agenten = int(eingabefeld_anz_agenten.get())
    Delta_person = float(eingabefeld_Delta_person.get())

    QUARANTANE = float(eingabefeld_quarantane.get())
    HERDENIMMUNITAT = float(eingabefeld_herdenimmunitat.get())

    fenster.quit()

    __main__(ITERATIONEN, b, h, alpha, beta, kappa, delta, gamma_1,
             gamma_2, Delta_person, mu_2, sigma_2, QUARANTANE, HERDENIMMUNITAT, anz_agenten)


# INTERFACE

fenster = Tk()
fenster.title("Eingabefenster für die Simulation")

# labels

my_label_iterationen = Label(fenster, text="Iterationen")
my_label_b = Label(fenster, text="Spielfeldbreite b:")
my_label_h = Label(fenster, text="Spielfeldhöhe h:")
my_label_alpha = Label(fenster, text=u"Übertragungswarscheinlichkeit der Krankheit \u03B1 :")
my_label_beta = Label(fenster, text=u"Wkt. von der Inkubationszeit zum infizierten Status \u03B2 :")
my_label_gamma_1 = Label(fenster, text=u"Genesungswkt. \u03B3 1:")
my_label_gamma_2 = Label(fenster, text=u"Sterbewkt. nach infizieren der Krankheit \u03B3 2:")
my_label_kappa = Label(fenster, text=u"Tag des Impfstarts (ohne Impfung = -1) \u03BA :")
my_label_delta = Label(fenster, text=u"Impfwarscheinlichkeit der Krankheit \u03B4 :")
my_label_mu_2 = Label(fenster, text=u"Mittelwert der Inkubationszeit \u03BC :")
my_label_sigma_2 = Label(fenster, text=u"Standardabweichung der Inkubationszeit \u03C3 :")

my_label_anz_agenten = Label(fenster, text=u"Anzahl der Agenten:")
my_label_Delta_person = Label(fenster, text=u"Infektionswarscheinlichkeit der Agenten \u0394 :")

my_label_quarantane = Label(fenster, text=u"Quarantäne (ohne Szenario = -1):")
my_label_herdenimmunitat = Label(fenster, text=u"Herdenimmunität (ohne Szenario = -1):")

# eingabe

eingabefeld_iterationen = Entry(fenster, bd=5, width=40)
eingabefeld_b = Entry(fenster, bd=5, width=40)
eingabefeld_h = Entry(fenster, bd=5, width=40)
eingabefeld_alpha = Entry(fenster, bd=5, width=40)
eingabefeld_beta = Entry(fenster, bd=5, width=40)
eingabefeld_gamma_1 = Entry(fenster, bd=5, width=40)
eingabefeld_gamma_2 = Entry(fenster, bd=5, width=40)
eingabefeld_kappa = Entry(fenster, bd=5, width=40)
eingabefeld_delta = Entry(fenster, bd=5, width=40)
eingabefeld_mu_2 = Entry(fenster, bd=5, width=40)
eingabefeld_sigma_2 = Entry(fenster, bd=5, width=40)

eingabefeld_anz_agenten = Entry(fenster, bd=5, width=40)
eingabefeld_Delta_person = Entry(fenster, bd=5, width=40)

eingabefeld_quarantane = Entry(fenster, bd=5, width=40)
eingabefeld_herdenimmunitat = Entry(fenster, bd=5, width=40)

start_button = Button(fenster, text="Start der Simulation", command=read_input_field)

exit_button = Button(fenster, text="Beenden", command=fenster.quit)

# STANDARD SET

eingabefeld_iterationen.insert(END, "1000")
eingabefeld_b.insert(END, "33")
eingabefeld_h.insert(END, "33")
eingabefeld_alpha.insert(END, "0.085")
eingabefeld_beta.insert(END, "1")
eingabefeld_gamma_1.insert(END, "0.01")
eingabefeld_gamma_2.insert(END, "0.015")
eingabefeld_kappa.insert(END, "-1")
eingabefeld_delta.insert(END, "0.005")
eingabefeld_mu_2.insert(END, "5.8")
eingabefeld_sigma_2.insert(END, "0.8")

eingabefeld_anz_agenten.insert(END, "1000")
eingabefeld_Delta_person.insert(END, "1")

eingabefeld_quarantane.insert(END, "-1")
eingabefeld_herdenimmunitat.insert(END, "-1")

# Nun fügen wir die Komponenten unserem Fenster hinzu

my_label_iterationen.grid(row = 0, column = 0)
my_label_b.grid(row = 1, column = 0)
my_label_h.grid(row = 2, column = 0)
my_label_alpha.grid(row = 3, column = 0)
my_label_beta.grid(row = 4, column = 0)
my_label_gamma_1.grid(row = 5, column = 0)
my_label_gamma_2.grid(row = 6, column = 0)
my_label_kappa.grid(row = 7, column = 0)
my_label_delta.grid(row = 8, column = 0)
my_label_mu_2.grid(row = 9, column = 0)
my_label_sigma_2.grid(row = 10, column = 0)

my_label_anz_agenten.grid(row = 11, column = 0)
my_label_Delta_person.grid(row = 12, column = 0)

my_label_quarantane.grid(row = 13, column = 0)
my_label_herdenimmunitat.grid(row = 14, column = 0)

eingabefeld_iterationen.grid(row = 0, column = 1)
eingabefeld_b.grid(row = 1, column = 1)
eingabefeld_h.grid(row = 2, column = 1)
eingabefeld_alpha.grid(row = 3, column = 1)
eingabefeld_beta.grid(row = 4, column = 1)
eingabefeld_gamma_1.grid(row = 5, column = 1)
eingabefeld_gamma_2.grid(row = 6, column = 1)
eingabefeld_kappa.grid(row = 7, column = 1)
eingabefeld_delta.grid(row = 8, column = 1)
eingabefeld_mu_2.grid(row = 9, column = 1)
eingabefeld_sigma_2.grid(row = 10, column = 1)

eingabefeld_anz_agenten.grid(row = 11, column = 1)
eingabefeld_Delta_person.grid(row = 12, column = 1)

eingabefeld_quarantane.grid(row = 13, column = 1)
eingabefeld_herdenimmunitat.grid(row = 14, column = 1)

start_button.grid(row = 15, column = 0)
exit_button.grid(row = 15, column = 1)

fenster.mainloop()

