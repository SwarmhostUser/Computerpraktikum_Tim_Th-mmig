import random

import Helper


def check1(WIDTH, HEIGHT, treffer, students):

    infection_list_gesunde = [[]]*(WIDTH*HEIGHT)
    infection_list_kranke = [[]] * (WIDTH * HEIGHT)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            for i in range(len(treffer[y * WIDTH + x])):
                if students[treffer[y * WIDTH + x][i]].contagious > 0 and students[treffer[y * WIDTH + x][i]].state == 1:
                    infection_list_kranke[y * WIDTH + x] = infection_list_kranke[y * WIDTH + x] + [students[treffer[y * WIDTH + x][i]].number]
                else:
                    infection_list_gesunde[y * WIDTH + x] = infection_list_gesunde[y * WIDTH + x] + [students[treffer[y * WIDTH + x][i]].number]

    return infection_list_gesunde, infection_list_kranke


def check2(hiroshima, treffer, students):

    infection_list = []

    for i in range(len(hiroshima)):
        case = 0
        for j in range(len(treffer[hiroshima[i]])):
            if students[treffer[hiroshima[i]][j]].contagious > 0 and students[treffer[hiroshima[i]][j]].state == 1:
                case = 1

        if case == 1:
            infection_list = infection_list + [hiroshima[i]]

    return infection_list


def infection(WIDTH, HEIGHT, infection_list_gesunde, infection_list_kranke, students, INFECTION_RATE, INFECTION_RATE_IF_VACC, mu_2, sigma_2):

    infection_rate_if_vaccination_2 = INFECTION_RATE_IF_VACC*INFECTION_RATE_IF_VACC

    for x in range(WIDTH):
        for y in range(HEIGHT):
            for i in range(len(infection_list_gesunde[y * WIDTH + x])):
                for j in range(len(infection_list_kranke[y * WIDTH + x])):

                    if students[infection_list_kranke[y * WIDTH + x][j]].incubation_period == 0:
                        infect_rate_in_inc = 1

                    else:
                        infect_rate_in_inc = 1 / students[infection_list_kranke[y * WIDTH + x][j]].incubation_period

                    # jetzt werden die verscheidenen fälle abgefragt je nachdem wer geimpft ist

                    if students[infection_list_kranke[y * WIDTH + x][j]].vaccinated == 1 and students[infection_list_gesunde[y * WIDTH + x][i]].vaccinated == 1:
                        if students[infection_list_kranke[y * WIDTH + x][j]].contagious*INFECTION_RATE*infection_rate_if_vaccination_2 > random.uniform(0, 1)*infect_rate_in_inc:
                            students[infection_list_gesunde[y * WIDTH + x][i]].state = 1
                            students[infection_list_gesunde[y * WIDTH + x][i]].incubation_period = Helper.get_incubation_period(mu_2, sigma_2)

                            students[infection_list_kranke[y * WIDTH + x][j]].rzero = students[infection_list_kranke[y * WIDTH + x][j]].rzero + 1

                    if students[infection_list_kranke[y * WIDTH + x][j]].vaccinated == 0 and students[infection_list_gesunde[y * WIDTH + x][i]].vaccinated == 1:
                        if students[infection_list_kranke[y * WIDTH + x][j]].contagious*INFECTION_RATE*INFECTION_RATE_IF_VACC > random.uniform(0, 1)*infect_rate_in_inc:
                            students[infection_list_gesunde[y * WIDTH + x][i]].state = 1
                            students[infection_list_gesunde[y * WIDTH + x][i]].incubation_period = Helper.get_incubation_period(mu_2, sigma_2)

                            students[infection_list_kranke[y * WIDTH + x][j]].rzero = students[infection_list_kranke[
                                y * WIDTH + x][j]].rzero + 1

                    if students[infection_list_kranke[y * WIDTH + x][j]].vaccinated == 1 and students[infection_list_gesunde[y * WIDTH + x][i]].vaccinated == 0:
                        if students[infection_list_kranke[y * WIDTH + x][j]].contagious*INFECTION_RATE*INFECTION_RATE_IF_VACC > random.uniform(0, 1)*infect_rate_in_inc:
                            students[infection_list_gesunde[y * WIDTH + x][i]].state = 1
                            students[infection_list_gesunde[y * WIDTH + x][i]].incubation_period = Helper.get_incubation_period(mu_2, sigma_2)

                            students[infection_list_kranke[y * WIDTH + x][j]].rzero = students[infection_list_kranke[
                                y * WIDTH + x][j]].rzero + 1

                    if students[infection_list_kranke[y * WIDTH + x][j]].vaccinated == 0 and students[infection_list_gesunde[y * WIDTH + x][i]].vaccinated == 0:
                        if students[infection_list_kranke[y * WIDTH + x][j]].contagious*INFECTION_RATE > random.uniform(0, 1)*infect_rate_in_inc*1:
                            students[infection_list_gesunde[y * WIDTH + x][i]].state = 1
                            students[infection_list_gesunde[y * WIDTH + x][i]].incubation_period = Helper.get_incubation_period(mu_2, sigma_2)

                            students[infection_list_kranke[y * WIDTH + x][j]].rzero = students[infection_list_kranke[
                                y * WIDTH + x][j]].rzero + 1
