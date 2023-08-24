# id, subject, name, dueDate, dueTime, priority, status, notes
import datetime

class task:
    def __init__(self, subject, name, dueDate, dueTime, priority, status, notes):
        self.id = 0
        self.subject = subject
        self.name = name
        self.dueDate = dueDate
        # self.dueMonth = int(dueDate.split('-')[0])
        # self.dueDay = int(dueDate.split('-')[1])
        self.dueTime = dueTime
        self.dueDateTime = datetime.datetime.strptime(dueDate + " " + dueTime, "%m-%d %H:%M%p")
        self.priority = priority
        self.status = status
        self.notes = notes
    
    def __str__(self):
        return self.subject + " - " + self.name + "\n" + self.dueDate + " " + self.dueTime
    
    def __repr__(self):
        return self.id + ", " + self.subject + ", " + self.name + ", " + self.dueDate + ", " + self.dueTime + ", " + self.priority + ", " + self.status + ", " + self.notes
    
    def display(self):
        return self.subject + " - " + self.name + "\n" + self.dueDate + " " + self.dueTime + "\n Priority: " + self.priority + " - Current Status: " + self.status + "\n" + self.notes
