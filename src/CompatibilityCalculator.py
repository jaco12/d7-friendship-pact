import Friend

def calculateCompatibility(friend1: Friend, friend2: Friend):
    """Calculate difference of answers between both people for each question."""
    total = len(friend1.questions) * 6
    score = 0
        
    for i in range(len(friend1.questions)):
        score += abs(friend1.questions[i] - friend2.questions[i])

    compatibility = round((1 - (score / total)) * 100, 4)    
    return compatibility

def compatibilityToStr(compatibility):
    """Format compatibility as a percentage and returns string. If compatibility is a whole number, remove decimal point."""
    return (str(int(compatibility)) + '%') if (compatibility).is_integer() else (str(round(compatibility, 2)) + '%')