import Friend

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
# Value: List of all other Friends
friendMap = {}

def calculateCompatibility(friend1, friend2):
    total = len(friend1.questions) * 6
    score = 0
    
    # Calculate difference of answers between both people for each question
    for i in range(len(friend1.questions)):
        score += abs(friend1.questions[i] - friend2.questions[i])
        
    compatibility = round(1 - (score / total), 4)
    
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
        if person != friend:
            compatibility = calculateCompatibility(person, friend)
            allOtherFriends.append((friend, compatibility))
    # Reverse sorts by compatibility with person
    friendMap[person] = sorted(allOtherFriends, reverse=True, key=lambda x: x[1])    

# Printing KV pairs in friendMap
for person in friendMap:
    print(person, end='')
    print(": [", end='')
    for friend in friendMap[person]:
        print("(", end='')
        print(friend[0], end='')
        print(", ", end='')
        print(friend[1], end='')
        print("), ", end='')
    print("]")


