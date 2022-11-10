import pandas as pd

from calculator import getAvgGrades
from configs import GRADES_PATH, STUD_EMAILS_PATH, FIRST_YEAR_STUD_SHEET_NAME, FIRST_YEAR_OP, SECOND_YEAR_OP, \
    THIRD_YEAR_OP
from excelWriter import write_to_excel
from read import readStudListWithEmail



if __name__ == '__main__':
    grades_df = pd.read_excel(GRADES_PATH)
    emails = pd.read_excel(STUD_EMAILS_PATH, sheet_name=FIRST_YEAR_STUD_SHEET_NAME)
    studList = readStudListWithEmail(grades_df, emails)


    # FIRST YEAR STUDENTS AVG
    fy = list((stud for stud in studList if stud.year == 1))
    avg_df = []
    for opname in FIRST_YEAR_OP:
        for_df = []
        op_students = list((stud for stud in fy if stud.op == opname))
        avg = getAvgGrades(op_students, opname)
        for_df.append(opname)
        for_df.append(avg)
        avg_df.append(for_df)
    avg_df = pd.DataFrame(avg_df,columns=["ОП", "Средняя оценка"])
    print(avg_df)
    avg_df.to_excel('res/avg.xlsx', '1-курс', index=False)


    # SECOND YEAR STUDENTS AVG
    fy = list((stud for stud in studList if stud.year == 2))
    avg_df = []
    for opname in SECOND_YEAR_OP:
        for_df = []
        op_students = list((stud for stud in fy if stud.op == opname))
        avg = getAvgGrades(op_students, opname)
        for_df.append(opname)
        for_df.append(avg)
        avg_df.append(for_df)
    avg_df = pd.DataFrame(avg_df,columns=["ОП", "Средняя оценка"])
    print(avg_df)
    write_to_excel(filename='res/avg.xlsx',df=avg_df, sheetname='2-курс')
    # avg_df.to_excel('res/avg.xlsx', '2-курс', index=False)


    # THIRD YEAR STUDENTS AVG
    fy = list((stud for stud in studList if stud.year == 3))
    avg_df = []
    for opname in THIRD_YEAR_OP:
        for_df = []
        op_students = list((stud for stud in fy if stud.op == opname))
        avg = getAvgGrades(op_students, opname)
        for_df.append(opname)
        for_df.append(avg)
        avg_df.append(for_df)
    avg_df = pd.DataFrame(avg_df,columns=["ОП", "Средняя оценка"])
    print(avg_df)
    # avg_df.to_excel('res/avg.xlsx', '3-курс', index=False)
    # write_to_excel(filename='res/avg.xlsx',df=avg_df, sheetname='3-курс')


