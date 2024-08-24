class Friend(object):
    """Encapsulates information about each survey response."""
    def __init__(self, name, school, email, socials, questions):
        self.name = name
        self.school = school
        self.email = email
        self.socials = socials
        # Array of ints--each int is the person's answer (1-7) for each question on the survey
        self.questions = questions 
        
    def __repr__(self):
        return f"{self.name}"    
    
    def __str__(self):
        return f"{self.name}"