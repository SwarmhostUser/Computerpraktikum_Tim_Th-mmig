import random
import os
import math

import person


def r_movement_radius(age):

    if age > 80:
        return 1

    elif age > 40:
        age = age - 40

    sigma = 15*age/40
    g = random.gauss(40, sigma)

    if abs(g - 40) > 40:
        return 4

    elif abs(g - 40) > 30:
        return 3

    elif abs(g - 40) > 20:
        return 2

    else:
        return 1


def wkv_todesrate(todesdaten_alter_wk, RATE_NATURAL_DEATH, age):

    if age == 0:
        return RATE_NATURAL_DEATH*todesdaten_alter_wk[0][1]

    if 1 <= age < 30:
        return RATE_NATURAL_DEATH * todesdaten_alter_wk[1][1] / 30

    if age >= 30:
        zeile = age-28            # zeile 2 ist alter 30-31 zeile 3 ist alter 31-32
        return RATE_NATURAL_DEATH * todesdaten_alter_wk[zeile][1]


def excel_to_wk(todesdaten_alter_array):

    todesdaten_alter_wk = todesdaten_alter_array

    for i in range(len(todesdaten_alter_array)):
        todesdaten_alter_wk[i][1] = todesdaten_alter_array[i][1]/33785      # wk für 80 ist 1 dann wird mehr

    return todesdaten_alter_wk


def current_working_directory():

    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory

    return print("Files in %r: %s" % (cwd, files))


def return_type(objekt):

    return print(type(objekt))


def debug_1(liste):

    for i in range(len(liste)):
        print(range(len(liste)))
        print("Hello")


def infection_rate(kranke, i):

    if i == 0:
        return 0.0

    else:
        return abs(kranke[i]-kranke[i-1])/person.Person.anz_personen


def get_incubation_period(mu_2, sigma_2):

    incubation = math.floor(random.gauss(mu_2, sigma_2))

    if incubation <= 1:
        return 1

    return incubation


def age_setter():

    if 94/1000 > random.uniform(0, 1):
        return 5
    if 97/1000 > random.uniform(0, 1):
        return 15
    if 170/1000 > random.uniform(0, 1):
        return 25
    if 187/1000 > random.uniform(0, 1):
        return 35
    if 132/1000 > random.uniform(0, 1):
        return 45
    if 148/1000 > random.uniform(0, 1):
        return 55
    if 102/1000 > random.uniform(0, 1):
        return 65
    if 49/1000 > random.uniform(0, 1):
        return 75
    if 21/1000 > random.uniform(0, 1):
        return 85
    else:
        return 45

