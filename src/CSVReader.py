import csv
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
        reader = csv.reader(file)
        
        # Skip header
        next(reader)
        for i, row in enumerate(reader, start=1):
            try:
            # response = line.strip().split(',')
            
            # # Create int array of person's answer (1-7) for each question on the survey
            # questionResponses = []
            # for i in range(6, len(response)):
            #     # answer = response[i].strip('\"')
            #     questionResponses.append(int(response[i]))
            
                questionResponses = [int(answer) for answer in row[6:-1]]
                
                # Create new Friend instance
                friend = Friend.Friend(row[CONST_NAME], 
                                row[CONST_SCHOOL], 
                                row[CONST_EMAIL], 
                                row[CONST_SOCIALS],
                                questionResponses)
                allFriends.append(friend)
            except Exception as e:
                print(f"Error processing row {i}: {row}")
                print(f"Exception: {e}")
                raise
    
    return allFriends