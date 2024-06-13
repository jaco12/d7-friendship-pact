import Friend
from matching import Player
from matching.games import StableRoommates
from matching import SingleMatching

# CONSTANTS: Each corresponds to an index of the array outputted by line.strip().split(',')
CONST_NAME = 1
CONST_EMAIL = 2
CONST_SCHOOL = 3
CONST_Q1 = 4
CONST_Q2 = 5
CONST_Q3 = 6
CONST_Q4 = 7
CONST_Q5 = 8

# List of all responses, as Friend objects
allFriends = []
# Key: Friend
# Value: List of all other Friends, converted to Player instances
prefList = {}

def calculateCompatibility(friend1, friend2):
    total = len(friend1.questions) * 6
    score = 0
    
    # Calculate difference of answers between both people for each question
    for i in range(len(friend1.questions)):
        score += abs(friend1.questions[i] - friend2.questions[i])
        
    compatibility = round((1 - (score / total)) * 100, 4)
    
    # For debugging
    # print(friend1, end='')
    # print(" and ", end='')
    # print(friend2, end='')
    # print(": " + str((compatibility * 100)) + "%")
    
    return compatibility

# Reading from CSV file into list of Friend objects
with open("d7fp_test_responses.csv", 'r') as file:
    next(file)
    for line in file:
        response = line.strip().split(',')
        friend = Friend.Friend(response[CONST_NAME], 
                               response[CONST_EMAIL], 
                               response[CONST_SCHOOL], 
                               [int(response[CONST_Q1]), 
                                int(response[CONST_Q2]), 
                                int(response[CONST_Q3]), 
                                int(response[CONST_Q4]), 
                                int(response[CONST_Q5])])
        allFriends.append(friend)

# Convert allFriends list into a dict
for person in allFriends:
    allOtherFriends = []
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

    for i in range(len(prefList[person])):
        prefList[person][i] = prefList[person][i][0]
    

game = StableRoommates.create_from_dictionary(prefList)
result = game.solve()

for person in result:
    print(str(person.name) + " - " + str(result[person].name) + ": Compatibility: " + str(calculateCompatibility(person.name, result[person].name)) + "%")