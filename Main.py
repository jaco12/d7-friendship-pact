import sys, csv

import Friend, Question
from CSVReader import csvToFriendList
from CSVWriter import writeToCSV
from PreferenceListMaker import createPreferenceList

from matching import Player, SingleMatching
from matching.games import StableRoommates

"""TODO:
    1. Convert ints in questionResponses to Question instances
    2. Make question weight CSV file an optional CLI argument
"""
# Takes in CLI arg for CSV input and converts to list of Friend instances
filename = sys.argv[1]
allFriends = csvToFriendList(filename)

# Key: Friend
# Value: List of all other Friends, sorted from best to worst compatibility
prefList = createPreferenceList(allFriends)
    
# Use matching library to solve stable roommates problem
# https://daffidwilde.github.io/matching/
game = StableRoommates.create_from_dictionary(prefList)
result = game.solve()

writeToCSV(result, "diff_school_matches.csv", "same_school_matches.csv")