#count the number of students
numofStudents=int(input("Enter the number of students: "))

#data storage
studentsData=[]

for i in range(numofStudents):
    print(f"Enter details for student {i+1}:")
    studentName=input(f"Enter the name of student {i+1}: ")
    studentAge=int(input(f"Enter the age of student {i+1}: "))
    studentGrade=float(input(f"Enter the grade of student {i+1}: "  ))

    student={
        "name": studentName,
        "age": studentAge,
        "grade": studentGrade
    }
    studentsData.append(student)
    if studentGrade >= 90:
        #print(f"{studentName} has an A grade.")
        grade="A"
    elif studentGrade >= 80:
        print(f"{studentName} has a B grade.")
    elif studentGrade >= 70:
        print(f"{studentName} has a C grade.")
    else:
        print(f"{studentName} has a D grade.")
print("\nSummary of Students Data:")
for student in studentsData:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")


print("\nPASSING STUDENTS:")
for student in studentsData:
    if student['grade'] >= 70:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")