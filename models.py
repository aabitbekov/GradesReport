class Subject:
    def __init__(self, name, totalgrade):
        self.name = name
        self.totalgrade = totalgrade

    def __str__(self):
        return f"{self.name} - {self.totalgrade}"



def getStudYear(group):
    import re
    if group:
        a = int(re.search(r'\d+', group).group())
    else:
        a = 0
    if group.endswith("M"):
        if a >= 2200:
            return ("M1")
        elif a >= 2100:
            return ("M2")
    else:
        if a >= 2200:
            return 1
        elif a >= 2100:
            return 2
        elif a >= 2000:
            return 3





class Student:

    def __init__(self, fname,lname, email, op, group):
        self.gradeslist = []
        self.fname = fname
        self.lname = lname
        self.email = email
        self.op = op
        self.group = group
        self.year = getStudYear(group)

    def __str__(self) -> str:
        return f"{self.email} - {self.fname} {self.lname} , {self.group}, {self.year}, {self.op}"






