import store
import task
import datetime

def main():
    task1 = task.task("Math", "HW", "2018-10-10", "12:00", "High", "0", "Do it")
    task2 = task.task("English", "Essay", "2018-10-10", "12:00", "High", "0", "Do it")
    data = store.store("data.txt")
    data.addTask(task1)
    data.addTask(task2)
    data.save()

if __name__ == "__main__":
    main()