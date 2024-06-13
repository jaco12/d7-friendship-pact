class Question(object):
    """Encapsulates question number and question weight."""
    def __init__(self, number, weight):
        self.number = number
        self.weight = weight
    
    def __repr__(self):
        return f"Question {self.number}: {self.weight}"
    
    def __str__(self):
        return f"Question {self.number}: {self.weight}"