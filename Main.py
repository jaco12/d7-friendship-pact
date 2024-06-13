import sys, csv

import Friend, Question
from CSVReader import *
from CSVWriter import *
from PreferenceListMaker import *

from matching import Player, SingleMatching
from matching.games import StableRoommates

"""TODO:
    1. Convert ints in questionResponses to Question instances
    2. Make question weight CSV file an optional CLI argument
"""
# Takes in CLI arg for CSV input
filename = sys.argv[1]

# List of all responses, as Friend instances
allFriends = readCSV(filename)

# Key: Friend
# Value: List of all other Friends, sorted from best to worst compatibility
prefList = createPreferenceList(allFriends)
    
# Use matching library to solve stable roommates problem
# https://daffidwilde.github.io/matching/
game = StableRoommates.create_from_dictionary(prefList)
result = game.solve()

# Writes matches to two CSV files--one for different-school matches, and one for same-school matches
writeToCSV(result,"diff_school_matches.csv", "same_school_matches.csv")