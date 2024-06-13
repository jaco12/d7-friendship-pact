import Friend
from matching import Player
from matching.games import StableRoommates
from matching import SingleMatching

# CONSTANTS: Each corresponds to an index of the array outputted by line 33
CONST_NAME = 1
CONST_EMAIL = 2
CONST_SCHOOL = 3

# List of all responses, as Friend objects
allFriends = []
# Key: Friend
# Value: List of all other Friends
prefList = {}

def calculateCompatibility(friend1, friend2):
    total = len(friend1.questions) * 6
    score = 0
    
    # Calculate difference of answers between both people for each question
    for i in range(len(friend1.questions)):
        score += abs(friend1.questions[i] - friend2.questions[i])
        
    compatibility = round((1 - (score / total)) * 100, 4)    
    return compatibility

# Reading from CSV file into list of Friend objects
with open("d7fp_test_responses.csv", 'r') as file:
    # Skip header
    next(file)
    for line in file:
        response = line.strip().split(',')
        
        # Create int array of person's answer (1-7) for each question on the survey
        questionResponses = []
        for i in range(4, len(response)):
            questionResponses.append(int(response[i]))
        
        # Create new Friend instance
        friend = Friend.Friend(response[CONST_NAME], 
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

# Print matches with compatibility score
for person in result:
    print(str(person.name) + " - " + str(result[person].name) + ": Compatibility: " + str(calculateCompatibility(person.name, result[person].name)) + "%")