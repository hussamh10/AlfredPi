import pickle
from datetime import datetime
from time import time

class course():
    def __init__(self, name):
        self.assignments = []
        self.quizzes = []
        self.name = name

    def setSchedule(self, first_epoch, second_epoch):
        i = 0
        WEEK = 604800
        times_temp = []
        self.times = []

        while(i < 30):
            times_temp.append(first_epoch + i*WEEK)
            times_temp.append(second_epoch + i*WEEK)
            i += 1
        
        for c in times_temp:
            if c  > time():
                self.times.append(c)

    def addMakeup(self, epoch):
        self.times.append(epoch)
        self.times.sort()

    def getClass(self):
        return self.times[0]

    def removeClass(self):
        self.times = self.times[1:]

    def removeAssignment(self, index):
        self.assignments.pop(index)

    def removeQuiz(self, index):
        self.quizzes.pop(index)

    def addAssignment (self, description, epoch):
        self.assignments.append({'description': description, 'deadline': epoch})

    def addQuiz (self, description, epoch):
        self.quizzes.append({'description': description, 'deadline': epoch})

    def getAssignments(self):
        assignments = ''
        for assignment in self.assignments:
            assignments = assignments + '\n' + (assignment['description']) + ' ' + '[ ' + str(datetime.fromtimestamp(assignment['deadline'])) + ' ]'
        return assignments

    def getQuizzes(self):
        quizzes = ''
        for quiz in self.quizzes:
            quizzes = quizzes + '\n' + (quiz['description']) + ' ' + '[ ' + str(datetime.fromtimestamp(quiz['deadline'])) + ' ]'
        return quizzes
