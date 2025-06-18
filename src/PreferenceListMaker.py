from CompatibilityCalculator import calculateCompatibility

def createPreferenceList(friendList: list):
    """Creates preference list from list of Friend instances."""
    prefList = {}
    
    for person in friendList:
        allOtherFriends = []
        
        # Move same-school friends to the back of the list, in order to prefer diff-school matches
        for friend in friendList:
            if person.school != friend.school:
                compatibility = calculateCompatibility(person, friend)
                allOtherFriends.append((friend, compatibility))
        for friend in friendList:
            if person.school == friend.school and person != friend:
                compatibility = calculateCompatibility(person, friend)
                allOtherFriends.append((friend, compatibility))

        # Reverse sorts by compatibility with person
        allOtherFriends.sort(key=lambda x: x[1], reverse=True)
        prefList[person] = allOtherFriends

        # Extracts Friends from tuple to replace prefList value
        for i in range(len(prefList[person])):
            prefList[person][i] = prefList[person][i][0]
    
    return prefList