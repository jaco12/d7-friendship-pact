import sys
import csv
from matching import Player
from matching.games import StableRoommates
from matching import SingleMatching

class Friend( object ):
    """Encapsulates information about each survey response."""
    def __init__(self, name, email, school, questions):
        self.name = name
        self.email = email
        self.school = school
        # Array of ints--each int is the person's answer (1-7) for each question on the survey
        self.questions = questions 
        
    def __repr__(self):
        return f"{self.name}"    
    
    def __str__(self):
        return f"{self.name}"

# CONSTANTS: Each corresponds to an index of the array outputted by line.strip().split(',')
CONST_NAME = 1
CONST_EMAIL = 2
CONST_SCHOOL = 3

# List of all responses, as Friend objects
allFriends = []
# Key: Friend
# Value: List of all other Friends
prefList = {}

def calculateCompatibility(friend1, friend2):
    # Calculate difference of answers between both people for each question
    total = len(friend1.questions) * 6
    score = 0
    
    for i in range(len(friend1.questions)):
        score += abs(friend1.questions[i] - friend2.questions[i])

    compatibility = round((1 - (score / total)) * 100, 4)    
    return compatibility

def compatibilityToStr(compatibility):
    # Format compatibility as a percentage and returns string
    # If compatibility is a whole number, remove decimal point
    return (str(int(compatibility)) + '%') if (compatibility).is_integer() else (str(round(compatibility, 2)) + '%')

# Reading from CSV file into list of Friend objects
with open(sys.argv[1], 'r') as file:
    # Skip header
    next(file)
    for line in file:
        response = line.strip().split(',')
        
        # Create int array of person's answer (1-7) for each question on the survey
        questionResponses = []
        for i in range(4, len(response)):
            questionResponses.append(int(response[i]))
        
        # Create new Friend instance
        friend = Friend(response[CONST_NAME], 
                        response[CONST_EMAIL], 
                        response[CONST_SCHOOL], 
                        questionResponses)
        allFriends.append(friend)

# Convert allFriends list into a dict
for person in allFriends:
    allOtherFriends = []
    
    # Prefer people from other schools vs. same-school
    for friend in allFriends:
        if person.school != friend.school:
            compatibility = calculateCompatibility(person, friend)
            allOtherFriends.append((friend, compatibility))
    for friend in allFriends:
        if person.school == friend.school and person != friend:
            compatibility = calculateCompatibility(person, friend)
            allOtherFriends.append((friend, compatibility))

    # Reverse sorts by compatibility with person
    allOtherFriends.sort(key=lambda x: x[1], reverse=True)
    prefList[person] = allOtherFriends

    # Extracts Friends from tuple to replace prefList value
    for i in range(len(prefList[person])):
        prefList[person][i] = prefList[person][i][0]
    
# https://daffidwilde.github.io/matching/
# Use matching library to solve stable roommates problem
game = StableRoommates.create_from_dictionary(prefList)
result = game.solve()

# Writes matches to two CSV files--one for different-school matches, and one for same-school matches
header = ['Name', 'Email', 'Friend Name', 'Friend Email', 'Friend School', 'Compatibility Score']
diffSchoolRows = []
sameSchoolRows = []
for each in result:
    person = each.name
    friend = result[each].name
    compatibility = calculateCompatibility(person, friend)
    
    row = [person.name, person.email, friend.name, friend.email, friend.school, compatibilityToStr(compatibility)]
    diffSchoolRows.append(row) if person.school != friend.school else sameSchoolRows.append(row)

diffSchools_filename = "diff_school_matches.csv"
with open(diffSchools_filename, 'w', newline='') as output:
    writer = csv.writer(output)
    writer.writerow(header)
    writer.writerows(diffSchoolRows)

sameSchools_filename = "same_school_matches.csv"
with open(sameSchools_filename, 'w', newline='') as output:
    writer = csv.writer(output)
    writer.writerow(header)
    writer.writerows(sameSchoolRows)