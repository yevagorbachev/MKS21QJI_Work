# Yevgeniy Gorbachev
# SoftDev1 pd1
# K<n> -- <Title><Topic/Summary>
# 2019-09-16   

import csv #awww yeah
import random


occus = csv.reader(open("occupations.csv"))
lines = [pair for pair in occus]
lines = [(pair[0], float(pair[1])) for pair in lines[1:-2]]
occu_dict = dict(lines)
print('\n'.join(str(item) for item in occu_dict.items()))

def select_random(occupations):
    selected = random.random() * 100
    running_chance = 0
    for pair in occupations:
        running_chance += pair[1]
        if selected < running_chance:
            return pair[0]

def rand_occupations(trials):
    actual_chance = {}
    for pair in lines:
        actual_chance[pair[0]]=0
    # print(actual_chance)
    for i in range(trials):
        occu = select_random(lines)
        if occu != None:
            actual_chance[occu] += 100/trials
    print(actual_chance)

print(select_random(lines))