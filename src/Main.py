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
    3. CSVReader should skip commas within double quotation marks when stripping responses
"""

"""Notes:
    1. Having a whole section for majors inflates the compatibility score because people will usually just answer 1 or 7 and it will be a perfect match with people of the same major
        Alternative methods:
            - Change academic major questions to True/False
            - Add weights to all questions and decrease the weights for the academic majors
            - Keep the current way, because having an inflated compatbility score looks better, otherwise the score would be generally much lower [CHOSE THIS OPTION]
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

writeToCSV(result, "output/diff_school_matches.csv", "output/same_school_matches.csv")