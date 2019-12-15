import csv
import sys
import json
import numpy as np

def get_deviation(x):
    pressures = get_pressures()
    mean = np.mean(pressures)
    std = np.std(pressures)
    answer = 50 - ((x - mean)*10/std)
    answer = round(answer, 2)

    return answer

def get_pressures():
    with open('./data/data.json') as f:
        json_object = json.load(f)
    
    pressures = []
    for x in json_object:
        if 'pressure' in x.keys():
            pressures.append(int(x['pressure']))
        else:
            print(x['year'], x['name'])
    pressures = np.array(pressures)
    return pressures