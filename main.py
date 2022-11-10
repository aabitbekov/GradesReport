import pandas as pd

from calculator import getAvgGrades, generateExcelAvgGrades
from configs import GRADES_PATH, STUD_EMAILS_PATH, FIRST_YEAR_STUD_SHEET_NAME, FIRST_YEAR_OP, SECOND_YEAR_OP, \
    THIRD_YEAR_OP, MFIRST_YEAR_OP, MSECOND_YEAR_OP
from read import readStudListWithEmail



if __name__ == '__main__':
    grades_df = pd.read_excel(GRADES_PATH)
    emails = pd.read_excel(STUD_EMAILS_PATH, sheet_name=FIRST_YEAR_STUD_SHEET_NAME)
    studList = readStudListWithEmail(grades_df, emails)


    # FIRST YEAR STUDENTS AVG
    generateExcelAvgGrades(studList=list((stud for stud in studList if stud.year == 1)),
                           year=1,
                           op_list=FIRST_YEAR_OP,
                           filename="res/avg.xlsx",
                           mode='w')

    generateExcelAvgGrades(studList=list((stud for stud in studList if stud.year == 2)),
                           year=2,
                           op_list=SECOND_YEAR_OP,
                           filename="res/avg.xlsx",
                           mode='a')

    generateExcelAvgGrades(studList=list((stud for stud in studList if stud.year == 3)),
                           year=3,
                           op_list=THIRD_YEAR_OP,
                           filename="res/avg.xlsx",
                           mode='a')

    generateExcelAvgGrades(studList=list((stud for stud in studList if stud.year == 'M1')),
                           year='M1',
                           op_list=MFIRST_YEAR_OP,
                           filename="res/avg.xlsx",
                           mode='a')

    generateExcelAvgGrades(studList=list((stud for stud in studList if stud.year == 'M2')),
                           year='M2',
                           op_list=MSECOND_YEAR_OP,
                           filename="res/avg.xlsx",
                           mode='a')

    #
    # # SECOND YEAR STUDENTS AVG
    # fy = list((stud for stud in studList if stud.year == 2))
    # avg_df = []
    # for opname in SECOND_YEAR_OP:
    #     for_df = []
    #     op_students = list((stud for stud in fy if stud.op == opname))
    #     avg = getAvgGrades(op_students, opname)
    #     for_df.append(opname)
    #     for_df.append(avg)
    #     avg_df.append(for_df)
    # avg_df = pd.DataFrame(avg_df,columns=["ОП", "Средняя оценка"])
    # print(avg_df)
    # with pd.ExcelWriter("res/avg.xlsx",mode='a') as writer:
    #     avg_df.to_excel(writer, '2-курс', index=False)
    #
    #
    # # THIRD YEAR STUDENTS AVG
    # fy = list((stud for stud in studList if stud.year == 3))
    # avg_df = []
    # for opname in THIRD_YEAR_OP:
    #     for_df = []
    #     op_students = list((stud for stud in fy if stud.op == opname))
    #     avg = getAvgGrades(op_students, opname)
    #     for_df.append(opname)
    #     for_df.append(avg)
    #     avg_df.append(for_df)
    # avg_df = pd.DataFrame(avg_df,columns=["ОП", "Средняя оценка"])
    # print(avg_df)
    # with pd.ExcelWriter("res/avg.xlsx", mode='a') as writer:
    #     avg_df.to_excel(writer, '3-курс', index=False)
    #
    #
    # # MASTERS FIRST YEAR STUDENTS AVG
    # fy = list((stud for stud in studList if stud.year == 'M1'))
    # avg_df = []
    # for opname in MFIRST_YEAR_OP:
    #     for_df = []
    #     op_students = list((stud for stud in fy if stud.op == opname))
    #     avg = getAvgGrades(op_students, opname)
    #     for_df.append(opname)
    #     for_df.append(avg)
    #     avg_df.append(for_df)
    # avg_df = pd.DataFrame(avg_df,columns=["ОП", "Средняя оценка"])
    # print(avg_df)
    # with pd.ExcelWriter("res/avg.xlsx", mode='a') as writer:
    #     avg_df.to_excel(writer, '1-курс Магистратура', index=False)
    #
    #
    # # MASTERS SECOND YEAR STUDENTS AVG
    # fy = list((stud for stud in studList if stud.year == 'M2'))
    # avg_df = []
    # for opname in MSECOND_YEAR_OP:
    #     for_df = []
    #     op_students = list((stud for stud in fy if stud.op == opname))
    #     avg = getAvgGrades(op_students, opname)
    #     for_df.append(opname)
    #     for_df.append(avg)
    #     avg_df.append(for_df)
    # avg_df = pd.DataFrame(avg_df,columns=["ОП", "Средняя оценка"])
    # print(avg_df)
    # with pd.ExcelWriter("res/avg.xlsx", mode='a') as writer:
    #     avg_df.to_excel(writer, '2-курс Магистратура', index=False)
    #
