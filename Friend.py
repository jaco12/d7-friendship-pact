class Friend( object ):
    #
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
    