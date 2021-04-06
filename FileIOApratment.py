def load_matching_data(min_score, min_stories, min_units):
    file = open('apartment_building_evaluation.csv', 'r')
    match = []
    for line in file:
        info = line.split(',')
        if(min_score <= float(info[24]) and min_stories <= float(info[2]) and
           min_units <= float(info[3])):
            
            match.append({"address": info[26], "score": float(info[24]), 
                          "num_stories": int(float(info[2])), "num_units": int(float(info[3]))})
            
    file.close()
    return match

results = load_matching_data(85, 28, 300)
print(results)
print(len(results))

import json

def load_matching_data(min_score, min_stories, min_units):
    file = open('apartment_building_evaluation.csv', 'r')
    match = []
    for line in file:
        info = line.split(',')
        if(min_score <= float(info[24]) and min_stories <= float(info[2]) and
           min_units <= float(info[3])):
            
            match.append({"address": info[26], "score": float(info[24]), 
                          "num_stories": int(float(info[2])), "num_units": int(float(info[3]))})
            
    file.close()
    return match

def save_summary(results, filename):
    with open(filename, 'w') as file:
        json.dump(results, file)

results = load_matching_data(85, 28, 300)
save_summary(results, 'apartment_summary.json')
with open('apartment_summary.json', 'r') as file:
    for line in file:
        print(line)