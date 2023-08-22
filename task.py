# id, subject, name, dueDate, dueTime, priority, status, notes

class task:
    def __init__(self, subject, name, dueDate, dueTime, priority, status, notes):
        self.id = 0
        self.subject = subject
        self.name = name
        self.dueDate = dueDate
        self.dueTime = dueTime
        self.priority = priority
        self.status = status
        self.notes = notes
    
    def __str__(self):
        return self.subject + " - " + self.name + "\n" + self.dueDate + " " + self.dueTime
    
    def __repr__(self):
        return self.id + ", " + self.subject + ", " + self.name + ", " + self.dueDate + ", " + self.dueTime + ", " + self.priority + ", " + self.status + ", " + self.notes