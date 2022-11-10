import pandas as pd
from configs import GRADES_PATH, STUD_EMAILS_PATH, FIRST_YEAR_STUD_SHEET_NAME, THRIRD_YEAR_STUD_SHEET_NAME
from models import Subject, Student

grades_df = pd.read_excel(GRADES_PATH)
emails = pd.read_excel(STUD_EMAILS_PATH, sheet_name=FIRST_YEAR_STUD_SHEET_NAME)

def readStudListWithEmail(grades_df, emails):
    students_list, mails = [], []

    for index in range(len(grades_df)):
        mail = grades_df['email'][index]
        op, group = '', ''
        if mail not in mails:
            for emails_index in range(len(emails)):
                if emails['username'][emails_index] == grades_df['email'][index]:
                    op = emails['ОП'][emails_index]
                    group = emails['Группа'][emails_index]
                    break
            mails.append(mail)

            student = Student(fname=grades_df['firstname'][index],
                              lname=grades_df['lastname'][index],
                              email=grades_df['email'][index],
                              op=op,
                              group=group)

            student.gradeslist.append(Subject(grades_df['fullname'][index], grades_df['calcTotal'][index]))

            students_list.append(student)

        else:
            for stud in students_list:
                if stud.email == grades_df['email'][index]:
                    subject = Subject(grades_df['fullname'][index], grades_df['calcTotal'][index])
                    i = students_list.index(stud)
                    students_list[i].gradeslist.append(subject)
                    break
    mails = []
    return students_list


def getFirstYearStudents(students_list):
    students = []
    for student in students_list:
        if student.year == 1:
            students.append(student)
    return students

def getSecondYearStudents(students_list):
    students = []
    for student in students_list:
        if student.year == 2:
            students.append(student)
    return students

def getThirdYearStudents(students_list):
    students = []
    for student in students_list:
        if student.year == 3:
            students.append(student)
    return students

def getM1Students(students_list):
    students = []
    for student in students_list:
        if student.year == "M1":
            students.append(student)
    return students

def getM2Students(students_list):
    students = []
    for student in students_list:
        if student.year == "M1":
            students.append(student)
    return students



