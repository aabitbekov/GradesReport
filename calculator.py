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


import pandas as pd
def generateExcelAvgGrades(studList, year, op_list, filename, mode):
    fy = list((stud for stud in studList if stud.year == year))
    avg_df = []
    for opname in op_list:
        for_df = []
        op_students = list((stud for stud in fy if stud.op == opname))
        avg = getAvgGrades(op_students, opname)
        for_df.append(opname)
        for_df.append(avg)
        avg_df.append(for_df)
    avg_df = pd.DataFrame(avg_df,columns=["ОП", "Средняя оценка"])
    print(avg_df)
    with pd.ExcelWriter(filename, mode=mode) as writer:
        if year == 'M1' or year == 'M2':
            avg_df.to_excel(writer, f'{year}', index=False)
        else:
            avg_df.to_excel(writer, f'{year}-курс', index=False)
