mynumbers = int (input("input your grade :"))
grades =  []
gradestak =  []
lowergrade = 10000
higthgrade = 0
buck = 0
for mynumber in range (0,mynumbers,1):
    grade = int(input ("input your number grade  :"))
    grades.append(grade)

for let in range(0,mynumbers,1):
    if grades[let] < lowergrade:
        lowergrade = grades[let]
    if grades[let] >higthgrade:
        higthgrade = grades[let]
    buck = buck +grades[let]

average = buck/mynumbers

for look in range(0,mynumber,1):
    if grades[look] < grades[look+1]:
        buck = grade[look]
        gradestak.append(buck)

print (gradestak)
        


