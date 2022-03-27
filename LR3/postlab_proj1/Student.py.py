class Students(object):

    def __init__(self, name, number):
        self.name = name
        self.grade = []
        for count in range(number):
            self.grade.append(0)

    def getName(self):
        return self.name
    def setScore(self, i, score):
        self.grade[i - 1] = score
    def getScore(self, i):
        return self.grade[i - 1]
    def getAverage(self):
        return sum(self.grade) / len(self._grade)
    def getHighScore(self):
        return max(self.grade)
    def __eq__(self,student):
        return self.name==student.name
    def __lt__(self,student):
        return self.name<student.name
    def __ge__(self,student):
        return self.name>=student.name
    def __str__(self):
        return "Student Name: " + self.name  + "\nResult: " + \
               " ".join(map(str, self.grade))

def main():
    student = Students("Justine", 5)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)
    print('\nSecond Student: ')
    student2=Students('Justine',5)
    print(student2)
    print('\nIs Student 1 equal to Student 2')
    print(student == student2)
    print('\Is student 1 greater than Student 2')
    print(student>=student2)
    print('\Is Student 1 less than Student 2')
    print(student<student2)


if __name__ == "__main__":
    main()




