import array

name = input("Hello! whats your name?\n")

print("Hello " + name + " please enter the number of students"
" You would like to calculate their maximum and their minimum")

numOfStudents = int(input())

listOfNames = list()
listOfGrades = list()

for i in range(numOfStudents):

    nameOfStudents = input("Whats the name of the " + str(i + 1) + " student\n")
    listOfNames.append(nameOfStudents)

for i in range(len(listOfNames)):
    gradesOfStudents = int(input("Whats " + listOfNames[i] + " grade? "))
    listOfGrades.append(gradesOfStudents)

for i in range(len(listOfNames)):
    print(listOfNames[i] + " grade is " + str(listOfGrades[i]))

def max():
    maxGrade = 0
    maxName = ""
    for i in range(len(listOfNames)):
        if listOfGrades[i] > maxGrade:
            maxGrade = listOfGrades[i]
            maxName = listOfNames[i]
    print(maxName + " has a grade of:")        
    print(maxGrade)

max()

def min():
    minGrade = listOfGrades[0]
    minName = ""
    for i in range(len(listOfNames)):
        if listOfGrades[i] < minGrade:
            minGrade = listOfGrades[i]
            minName = listOfNames[i]
    print(minGrade)
    print(minName)
min()
