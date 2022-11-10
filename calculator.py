def getAvgGrades(students_list, op):
    totalSum = 0
    studentCount = 0
    for student in students_list:
        print(student.fname, student.lname, end=" ")
        count = 0
        studentSum = 0
        for grade in student.gradeslist:
            count += 1
            studentSum += grade.totalgrade
        print(f"Avg: {studentSum / count }")
        totalSum += studentSum / count
        studentCount += 1
    if studentCount == 0:
        return 0
    else:
        print(f"Avg of  {op}: {totalSum / studentCount}")
        return (totalSum / studentCount)