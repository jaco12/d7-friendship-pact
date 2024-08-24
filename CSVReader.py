import Friend

def csvToFriendList(filename: str):
    """Reads the responses CSV file and returns a list of all Friends"""
    # CONSTANTS: Each corresponds to an index of the array outputted by line.strip().split(',')
    CONST_NAME = 1
    CONST_SCHOOL = 2
    CONST_EMAIL = 3
    CONST_SOCIALS = 4
    
    allFriends = []
    # Reading from CSV file into list of Friend objects
    with open(filename, 'r') as file:
        # Skip header
        next(file)
        for line in file:
            response = line.strip().split(',')
            
            # Create int array of person's answer (1-7) for each question on the survey
            questionResponses = []
            for i in range(6, len(response)):
                # answer = response[i].strip('\"')
                questionResponses.append(int(response[i]))
            
            # Create new Friend instance
            friend = Friend.Friend(response[CONST_NAME], 
                            response[CONST_SCHOOL], 
                            response[CONST_EMAIL], 
                            response[CONST_SOCIALS],
                            questionResponses)
            allFriends.append(friend)
    
    return allFriends