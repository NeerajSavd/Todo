import task

class store:
    def __init__(self, path):
        self.path = path
        self.tasks = []
        self.archived = []
        file = open(path, 'r')
        self.nextId = int(file.readline().strip())
        for line in file:
            if line != '\n':
                line = line.strip('\n').split(', ')
                newTask = task.task(*line[1:])
                newTask.id = line[0]
                self.tasks.append(newTask)
        file.close()
        self.tasks.sort(key=lambda x: x.dueDateTime)
    
    def addTask(self, task):
        task.id = str(self.nextId)
        self.nextId += 1
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: x.dueDateTime)
    
    def removeTask(self, task):
        self.tasks.remove(task)
        self.archived.append(task)
    
    def changePriority(self, task, priority):
        task.priority = priority
    
    def save(self):
        file = open(self.path, 'w')
        file.write(str(self.nextId)+'\n')
        for task in self.tasks:
            file.write(repr(task)+'\n')
        file.close()