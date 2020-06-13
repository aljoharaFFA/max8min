import array

name = input("Hello! whats your name?\n")

print("Hello " + name + " please enter the number of students"
" You would like to calculate their maximum and their minimum")

numOfStudents = int(input())

listOfNames = array.array('u', [])
for i in range(numOfStudents):

    nameOfStudents = input("Whats the name of the " + str(i) + " student\n")
    listOfNames.append(nameOfStudents)

print(','.join(listOfNames))
