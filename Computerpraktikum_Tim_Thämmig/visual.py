import numpy

import person
import infection


def bauen_der_m(WIDTH, HEIGHT, students):

    mat = [[0] * HEIGHT for _ in range(WIDTH)]

    for x in range(WIDTH):
        for y in range(HEIGHT):
            sum_feld = 0
            for i in range(person.Person.anz_personen):
                if students[i].pos_x == x and students[i].pos_y == y:
                    sum_feld = sum_feld + students[i].state
            sum_feld = sum_feld/person.Person.anz_personen
            mat[x][y] = sum_feld

    return mat


def gesundheits_check(i, students, kranke, gesunde, tote, geimpfte):

    anz_krank = 0
    anz_gesund = 0
    anz_tote = 0
    anz_geimpfte = 0

    for j in range(len(students)):
        if students[j].state == 0:      #0 = gesund 1 = krank 2=tot
            anz_gesund = anz_gesund + 1

        if students[j].state == 1:
            anz_krank = anz_krank + 1

        if students[j].state == 2:
            anz_tote = anz_tote + 1

        if students[j].vaccinated == 1:
            anz_geimpfte = anz_geimpfte + 1

    gesunde[i] = anz_gesund
    kranke[i] = anz_krank
    tote[i] = anz_tote
    geimpfte[i] = anz_geimpfte

    return anz_gesund, anz_krank, anz_tote, anz_geimpfte, kranke, gesunde, tote, geimpfte


def update(i, WIDTH, HEIGHT, students, kranke, gesunde, tote, geimpfte, todesdaten_alter_wk, RATE_NATURAL_DEATH, ax_geskra, ax_feld, VACC_START, VACCINATION_RATE, GENESUNGS_RATE, DEATH_RATE, INFECTION_RATE, INFECTION_RATE_INF, INFECTION_RATE_IF_VACC, QUARANTANE, HERDENIMMUNITAT, ITERATIONEN, mu_2, sigma_2):

    #SZENARIEN

    if QUARANTANE != -1:
        person.quarantane(students, QUARANTANE)

    #R0 BERECHNUNG

    #if i == 100 or i == 200 or i == 300 or i == 400 or i == 500 or i == 600 or i == 700 or i == 800 or i == 900 or i == 999:
    #    rzero = person.calculation_rzero(students)
    #    print(rzero)

    # DATENSTRUKTUREN BAUEN

    anz_gesund, anz_krank, anz_tote, anz_geimpfte, kranke, gesunde, tote, geimpfte = gesundheits_check(i, students, kranke, gesunde, tote, geimpfte)
    hiroshima, treffer, anztreffer = person.check(WIDTH, HEIGHT, students)
    infection_list_gesunde, infection_list_kranke = infection.check1(WIDTH, HEIGHT, treffer, students)
    infection_list = infection.check2(hiroshima, treffer, students)

    # INFIZIEREN; BEWEGEN; STERBEN; GENESEN

    infection.infection(WIDTH, HEIGHT, infection_list_gesunde, infection_list_kranke, students, INFECTION_RATE, INFECTION_RATE_IF_VACC, mu_2, sigma_2)
    person.move(students, WIDTH, HEIGHT)
    person.death(students, todesdaten_alter_wk, RATE_NATURAL_DEATH)
    person.genesen(students, GENESUNGS_RATE)
    person.reduction_incubation_period(students, INFECTION_RATE_INF)
    person.disease_death(students, DEATH_RATE)

    # IMPFUNG

    if VACC_START != -1 and i > VACC_START:
        person.vaccination(students, VACCINATION_RATE)

    # GRAPH

    ax_geskra.clear()
    ax_geskra.plot(kranke, label="Kranke")
    ax_geskra.plot(gesunde, label="Gesunde")
    ax_geskra.plot(tote, label="Tote")
    ax_geskra.plot(geimpfte, label="Geimpfte")
    ax_geskra.set(xlabel='Zeit')
    ax_geskra.set(ylabel='Anz. Personen')
    ax_geskra.legend(loc="upper right")
    #ax_geskra.legend(title="gamma_2=0,03")

    ax_geskra.set_xlim([0, ITERATIONEN-1])
    ax_geskra.set_ylim([0, person.Person.anz_personen])

    # wieder aktivieren für das 2- feld

    mat = bauen_der_m(WIDTH, HEIGHT, students)
    ax_feld.clear()
    ax_feld.pcolormesh(mat)

    x = numpy.arange(0, WIDTH-1, 1)
    y = numpy.arange(0, HEIGHT-1, 1)
    z = numpy.random.rand(WIDTH, HEIGHT)


