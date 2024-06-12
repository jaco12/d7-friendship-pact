class Friend( object ):
    #
    def __init__(self, name, email, school, questions) -> None:
        self.name = name
        self.email = email
        self.school = school
        # Array of ints--each int is the persons answer (1-7) for each question on the survey
        self.questions = questions 
        
    def __str__(self) -> str:
        return f"{self.name}"