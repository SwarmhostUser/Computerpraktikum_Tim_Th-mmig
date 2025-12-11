import random

import Helper


class Person:

    anz_personen = 0

    def __init__(self, state, pos_x, pos_y, age, contagious, vaccinated, patientzero):

        self.state = state                  #0 ist gesund 1 ist krank 2 ist tot
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.age = age
        self.contagious = contagious        #ansteckungswarscheinlichkeit
        self.incubation_period = 0          #anzahl der tage welche man noch in inkubationszeit ist
        self.vaccinated = vaccinated        #0 = nicht geimpft 1= geimpft
        self.movement_radius = Helper.r_movement_radius(age)    # BEWEGUNGSRADIUS WIRD ABHÄNGIG VOM ALTER BERECHNET MIT MU = 40 UND SIGMA = 15*age/40
        self.number = Person.anz_personen
        self.patientzero = patientzero      #1 ist patien0
        self.rzero = 0

        Person.anz_personen = Person.anz_personen + 1


def check(WIDTH, HEIGHT, students):

    anztreffer = [0]*(WIDTH*HEIGHT)
    treffer = [[]]*(WIDTH*HEIGHT)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            for i in range(Person.anz_personen):
                if students[i].pos_x == x and students[i].pos_y == y:

                    anztreffer[y*WIDTH+x] += 1
                    treffer[y*WIDTH+x] = treffer[y*WIDTH+x] + [students[i].number]      # students[i].number = i

    hiroshima = []

    for i in range(WIDTH * HEIGHT):
        if anztreffer[i] >= 2:
            hiroshima.append(i)

    return hiroshima, treffer, anztreffer           #gibt tupel wieder


def move(students, WIDTH, HEIGHT):

    # AM RAND KÖNNEN DIE PERSONEN SICH NUR IN BESTIMMTE RICHTUNGEN BEWEGEN DIE VERSCHIEDENEN CASES SIND HIER

    for i in range(Person.anz_personen):

        case = 0

        for j in range(0, students[i].movement_radius):
            if students[i].pos_x == 0:
                students[i].pos_x = students[i].pos_x + random.randint(0, 1)
                case = 1

            if students[i].pos_x == WIDTH-1:
                students[i].pos_x = students[i].pos_x + random.randint(-1, 0)
                case = 1

            if students[i].pos_y == 0:
                students[i].pos_y = students[i].pos_y + random.randint(0, 1)
                case = 2
            if students[i].pos_y == HEIGHT-1:
                students[i].pos_y = students[i].pos_y + random.randint(-1, 0)
                case = 2

            if case == 1:
                students[i].pos_y = students[i].pos_y + random.randint(-1, 1)
            if case == 2:
                students[i].pos_x = students[i].pos_x + random.randint(-1, 1)
            if case == 0:
                students[i].pos_x = students[i].pos_x + random.randint(-1, 1)
                students[i].pos_y = students[i].pos_y + random.randint(-1, 1)


def death(students, todesdaten_alter_wk, RATE_NATURAL_DEATH):

    for i in range(len(students)):
        if Helper.wkv_todesrate(todesdaten_alter_wk, RATE_NATURAL_DEATH, students[i].age) > random.uniform(0, 1):

            students[i].state = 2
            students[i].movement_radius = 0
            students[i].pos_x = -1
            students[i].pos_y = -1
            students[i].contagious = 0


def vaccination(students, VACCINATION_RATE):

    for i in range(len(students)):
        if students[i].state == 0 and students[i].vaccinated == 0:
            if VACCINATION_RATE > random.uniform(0, 1):
                students[i].vaccinated = 1


def genesen(students, GENESUNGS_RATE):

    for i in range(len(students)):
        if students[i].state == 1 and students[i].incubation_period == 0 and students[i].patientzero == 0:
            if GENESUNGS_RATE > random.uniform(0, 1):
                students[i].state = 0


def reduction_incubation_period(students, INFECTION_RATE_INF):

    for i in range(len(students)):

        if students[i].incubation_period == 1:
            students[i].incubation_period = 0

            if INFECTION_RATE_INF < random.uniform(0, 1):
                students[i].state = 0

        if students[i].incubation_period != 0 and students[i].incubation_period != 1:
            students[i].incubation_period = students[i].incubation_period - 1


def disease_death(students, DEATH_RATE):

    for i in range(len(students)):
        if students[i].state == 1 and students[i].incubation_period == 0 and students[i].patientzero == 0:
            if random.uniform(0, 1) < DEATH_RATE:

                students[i].state = 2
                students[i].movement_radius = 0
                students[i].pos_x = -1
                students[i].pos_y = -1
                students[i].contagious = 0


def quarantane(students, QUARANTANE):

    for i in range(len(students)):
        if students[i].state == 1 and students[i].incubation_period == 0 and students[i].patientzero == 0:
            students[i].contagious = QUARANTANE


def herdenimmunitat(students, HERDENIMMUNITAT):

    for i in range(len(students)):
        if random.uniform(0, 1) < HERDENIMMUNITAT:
            students[i].vaccinated = 1


def calculation_rzero(students):

    summe = 0

    for i in range(len(students)):
        summe = summe + students[i].rzero

    summe = summe/(len(students)+1)

    return summe
