import Friend

# CONSTANTS: each corresponds to an index of the array outputted by line.strip().split(',')
CONST_NAME = 1
CONST_EMAIL = 2
CONST_SCHOOL = 3
CONST_Q1 = 4
CONST_Q2 = 5
CONST_Q3 = 6
CONST_Q4 = 7
CONST_Q5 = 8

allFriends = []
friendMap = {}

with open("d7fp_test_responses.csv", 'r') as file:
    next(file)
    for line in file:
        response = line.strip().split(',')
        friend = Friend.Friend(response[CONST_NAME], response[CONST_EMAIL], response[CONST_SCHOOL], [response[CONST_Q1], response[CONST_Q2], response[CONST_Q3], response[CONST_Q4], response[CONST_Q5]])
        allFriends.append(friend)
        
for person in allFriends:
    print(person)
