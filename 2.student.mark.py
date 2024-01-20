class students:
    def __init__(self,id,name,DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
    def __str__(self):
        return f"id: {self.id}\nname: {self.name}\nDoB: {self.DoB}"
class courses:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __str__(self):
        return f"id: {self.id}\nname: {self.name}"   
class marks:
    def __init__(self,mark):
        self.mark = mark
def inputInforStudent():
    global numberStudent
    global listStudent
    listStudent = [] 
    numberStudent = int(input("please enter number of student: "))
    for _ in range(numberStudent):
        id = input('enter id of student '+str(_+1)+':')
        name = input('enter name of student '+str(_+1)+':')
        DoB = input('enter the DoB of student '+str(_+1)+':')
        student = students(id,name,DoB)
        listStudent.append(student)
def inputCourse():
    global numberCourse
    global listCourse
    listCourse = []
    numberCourse = int(input('enter number of course: '))
    for _ in range(numberCourse):
        id = input('enter id of course '+str(_+1)+':')
        name = input('enter name of course '+str(_+1)+':')
        course = courses(id,name)
        listCourse.append(course)
def inputMark():
    global listMark
    listMark =[]
    for x in range(numberCourse):
        print('Course: '+listCourse[x].name+'\n')
        for y in range(numberStudent):
            mark = int(input('please enter mark of student: '+listStudent[y].name+' id: '+listStudent[y].id+'\n'))
            mark_score = marks(mark)
            class mark_infos:
                def __init__(self,course,id,name,mark):
                    self.course = course
                    self.id = id
                    self.name = name
                    self.mark = mark
                def __str__(self):
                    return f"course: {self.course}\nid: {self.id}\nname: {self.name}\nmark: {self.mark}\n"
            mark_info = mark_infos(listCourse[x].name,listStudent[y].id,listStudent[y].name,mark_score.mark)
            listMark.append(mark_info)
    
def printStudent():
    for _ in range(numberStudent):
        print('Student: '+str(_+1))
        print(listStudent[_])
        print('\n')
def printCourse():
    for _ in range(numberCourse):
        print('Course: '+str(_+1))
        print(listCourse[_])
        print('\n')
def printMark():
    for _ in range(numberCourse*numberStudent):
        print(listMark[_])
numberStudent = 0
numberCourse = 0
listMark = []
print("0. Exit\n1. input infor of students\n2. input infor of course\n3. print students list\n4. print courses list\n5. input mark\n6. print marks list")

while True:
    choice = int(input("please enter the choice: \n"))
    if choice == 0:
        break
    if choice == 1:
        if numberStudent != 0:
            print('student list are already exist , please choose other choice!')
            continue
        inputInforStudent()
    if choice == 2:
        if numberCourse != 0:
            print('Course list are already exist , please choose other choice!')
            continue
        inputCourse()
    if choice == 3:
        if numberStudent == 0:
            print('no student in list of student!')
            continue
        printStudent()
    if choice == 4:
        if numberCourse == 0:
            print('no course in list of course!')
            continue
        printCourse()
    if choice == 5:
        if listMark != []:
            print('the list of mark already exist!')
            continue
        if numberCourse == 0 :
            print('no course')
            continue
        if numberStudent == 0:
            print('no student')
            continue
        inputMark()
    if choice == 6:
        if listMark == []:
            print("mark list doesn't exist ")
            continue

        if numberCourse == 0 :
            print('no course')
            continue
        if numberStudent == 0:
            print('no student')
            continue
        printMark()
    
