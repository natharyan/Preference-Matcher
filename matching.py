import csv
import numpy as np
import json

options = {
    0: ['8-10', '10-12', '12-2', '2-4', '4-6'],
    1: ['6-8', '8-10', '10-12', '12-2'],
    2: ['rarely', 'occasionally', 'neutral', 'frequently', 'always'],
    3: ['extremely', 'generally', 'somewhat', 'not']
}

# Link each name to a 5 dimensional array
preferences = {}
with open('matchmaking.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for i, row in enumerate(reader):
        preferences[row[2] + ':' + row[1]] = list(map(lambda s: options[row.index(s) - 3].index(s), row[3:8]))

print(preferences)


# Calculate the distance between polar coordinates
def calculate_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


# Rank the distances for each corresponding array
distances = {}
for i in preferences:
    tmp_preferences = preferences.copy()
    tmp_preferences.pop(i)
    distances[i] = sorted(tmp_preferences.keys(), key=lambda s: calculate_distance(preferences[i], preferences[s]))

print(distances)


def match(preference_dict):
    person_list = list(preference_dict.keys())
    n = len(person_list)

    def get_rankings(prefs):
        return {prefs[i]: i for i in range(len(prefs))}

    preferences = [[person_list.index(neighbor) for neighbor in preference_dict[person]] for person in person_list]

    proposals = [-1] * n  # Keeps track of the proposals each person has made
    rank = {}  # Keeps track of the rank of each person for the current chooser

    for i in range(n):
        rank[i] = get_rankings(preferences[i])

    matched = set()  # Keep track of matched individuals
    optimal_matching = []

    for proposer in range(n):
        if proposer not in matched:
            recipient = -1

            for preference in preferences[proposer]:
                if proposals[preference] == -1:
                    recipient = preference
                    break
                else:
                    current_suitor = proposals[preference]
                    if current_suitor not in matched:  # Check if the suitor is in matched
                        matched.remove(current_suitor)
                        matched.add(proposer)
                        proposals[preference] = proposer
                        recipient = preference

            if recipient != -1:
                matched.add(proposer)
                matched.add(recipient)
                proposals[recipient] = proposer
                proposals[proposer] = recipient
                optimal_matching.append((person_list[proposer], person_list[recipient]))

    return optimal_matching


matching = match(distances)

print(matching)

matching = {i + 1: pair for i, pair in enumerate(matching)}
with open('matches.json', 'w') as json_file:
    json.dump(matching, json_file)
with open('preferences.json', 'w') as json_file:
    json.dump(distances, json_file)
