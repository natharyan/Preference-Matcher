import csv
import numpy as np
import json

options = {0: ['8-10', '10-12', '12-2', '2-4', '4-6'],
 1: ['6-8', '8-10', '10-12', '12-2'],
 2: ['rarely', 'occasionally', 'neutral', 'frequently','always'],
 3: ['extremely', 'generally', 'somewhat', 'not']}

# link each name to a 5 dimensional array
candidates = {}
rel = 'matches/'
with open(rel+'matchmaking.csv','r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for i,row in enumerate(reader):
        candidates[row[2]+':'+row[1]] = list(map(lambda s: options[row.index(s) - 3].index(s),row[3:8]))
print(candidates)

# calculate the distance between polar coordinates
def calculate_distance(p1,p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# rank the distances for each corresponding array
distances = {}
for i in candidates:
    tmp_candidates = candidates.copy()
    tmp_candidates.pop(i)
    distances[i] = sorted(tmp_candidates.keys(),key=lambda s: calculate_distance(candidates[i],candidates[s]))
    
print(distances)

def irving(roommates_dict):
    person_list = list(roommates_dict.keys())
    n = len(person_list)

    def get_rankings(prefs):
        return {prefs[i]: i for i in range(len(prefs))}

    roommates = [[person_list.index(neighbor) for neighbor in roommates_dict[person]] for person in person_list]

    proposals = [-1] * n  # Keeps track of the proposals each person has made
    rank = {}  # Keeps track of the rank of each roommate for each person

    for i in range(n):
        rank[i] = get_rankings(roommates[i])

    matched = set()  # Keep track of matched individuals
    stable_matching = []

    for proposer in range(n):
        if proposer not in matched:
            recipient = -1

            for roommate in roommates[proposer]:
                if proposals[roommate] == -1:
                    recipient = roommate
                    break
                else:
                    current_suitor = proposals[roommate]
                    if current_suitor not in matched:  # Check if the suitor is in matched
                        matched.remove(current_suitor)
                        matched.add(proposer)
                        proposals[roommate] = proposer
                        recipient = roommate

            if recipient != -1:
                matched.add(proposer)
                matched.add(recipient)
                proposals[recipient] = proposer
                proposals[proposer] = recipient
                stable_matching.append((person_list[proposer], person_list[recipient]))

    return stable_matching

matching = irving(distances)

print(matching)
rel = 'matches/'
matching = {i+1:pair for i,pair in enumerate(matching)}
with open(rel+'matches.json','w') as json_file:
    json.dump(matching,json_file)
with open(rel+'preferences.json','w') as json_file:
    json.dump(distances,json_file)