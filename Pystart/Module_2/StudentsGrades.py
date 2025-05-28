grades = (5,4,2,6,2,4,6,3,5,5,4,1,2,5)

#print(f'Grades :{sorted(grades)}')

average = sum(grades)/float(len(grades))

if (average >= 4.75):
    print(f"Student will have awarded results. His average = {average:.2f}")
else :
    print(f'Student will not be awarded. His average = {average:02.2f}')