import math
import numpy
import curses
class students:
    def __init__(self,id,name,DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
        self.GPA = 0
    def __str__(self):
        return f"id: {self.id}\nname: {self.name}\nDoB: {self.DoB}\nGPA: {self.GPA}"
class courses:
    def __init__(self,id,name,credit):
        self.id = id
        self.name = name
        self.credit = credit
    def __str__(self):
        return f"id: {self.id}\nname: {self.name}\ncredit: {self.credit}"   
class marks:
    def __init__(self,mark):
        self.mark = mark
def round_down_mark(mark):
    rounded_score = math.floor(mark * 10) / 10
    return rounded_score

def inputInforStudent():
    global numberStudent
    global listStudent
    listStudent = numpy.array([]) 
    numberStudent = int(input("please enter number of student: "))
    for _ in range(numberStudent):
        id = input('enter id of student '+str(_+1)+':')
        name = input('enter name of student '+str(_+1)+':')
        DoB = input('enter the DoB of student '+str(_+1)+':')
        student = students(id,name,DoB)
        listStudent=numpy.append(listStudent,student)
def inputCourse():
    global numberCourse
    global listCourse
    listCourse = []
    numberCourse = int(input('enter number of course: '))
    for _ in range(numberCourse):
        id = input('enter id of course '+str(_+1)+':')
        name = input('enter name of course '+str(_+1)+':')
        credit = int(input('enter credit of course'+str(_+1)+':'))
        course = courses(id,name,credit)
        listCourse.append(course)
def inputMark():
    global listMark
    listMark =[]
    for x in range(numberCourse):
        print('Course: '+listCourse[x].name+'\n')
        for y in range(numberStudent):
            mark =  float(input('please enter mark of student: '+listStudent[y].name+' id: '+listStudent[y].id+'\n'))
            mark_score = marks(round_down_mark(mark))
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
def calculate_avarage_GPA():
    sum_credit = 0
    for _ in range(numberCourse):
        sum_credit = sum_credit + listCourse[_].credit
    for x in range(numberStudent):
        total_mark = 0
        for y in range(numberCourse*numberStudent):
            for z in range(numberCourse):
                if(listCourse[z].name==listMark[y].course):
                    credits = listCourse[z].credit
            if(listStudent[x].id==listMark[y].id):
                total_mark += listMark[y].mark * credits
        GPA = total_mark/sum_credit
        listStudent[x].GPA = GPA
    n = numberStudent 
    while(n != 1):
        for _ in range(n-1):
            if(listStudent[_].GPA<listStudent[_+1].GPA):
                listStudent[_],listStudent[_+1]=listStudent[_+1],listStudent[_]
        n -= 1


numberStudent = 0
numberCourse = 0
listMark = []
print("0. Exit\n1. input infor of students\n2. input infor of course\n3. print students list\n4. print courses list\n5. input mark\n6. print marks list\n7. Calculate GPA")
def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    stdscr.refresh()
    for _ in range(numberCourse*numberStudent):
        stdscr.addstr(_,0,f"course: {listMark[_].course} id: {listMark[_].id} name: {listMark[_].name} mark: {listMark[_].mark}")
    stdscr.refresh()
    stdscr.getch()
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
        if __name__ == '__main__':
            curses.wrapper(main)
    if choice == 7:
        if listMark == []:
            print('the list of mark does not exist!')
            continue
        if numberCourse == 0 :
            print('no course')
            continue
        if numberStudent == 0:
            print('no student')
            continue
        calculate_avarage_GPA()
 
