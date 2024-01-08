listStudent = []
listCourse = []
liskMark = []
numberStudent = 0
numberCourse = 0

def inputNumberStudent(n):
    global numberStudent 
    numberStudent = int(n)

def inputInformation():
    n = numberStudent
    for _ in range(n):
        id = input("please enter the id of student \n"+str(_+1)+":")
        name = input("please enter the name \n"+str(_+1)+":")
        DoB = input("please enter the DoB \n"+str(_+1)+":")
        student= {
                "id":id,
                "name":name,
                "DoB" :DoB 
        }
        listStudent.append(student)
    
def printStudent():
    for _ in range(numberStudent):
        print("id: "+listStudent[_]["id"]+" name: "+listStudent[_]["name"]+" DoB: "+listStudent[_]["DoB"]+"\n")
    
def inputNumberCourse(n):
    global numberCourse
    numberCourse = int(n)
def inputCourse():
    n = numberCourse
    for _ in range(n):
        id = input("please enter the id of course \n"+str(_+1)+":")
        name = input("please enter the name of course \n"+str(_+1)+":")
        course = {
                "id":id,
                "name":name
                }
        listCourse.append(course)
def printCourse():
    for _ in range(numberCourse):
        print("id: "+listCourse[_]["id"]+" name: "+listCourse[_]["name"]+"\n")
def mark(n):
    mark = {
        "mark":n
    }
    return mark
def markInput():
    for x in range(numberCourse):
        for y in range(numberStudent):
            print("Enter the mark of student:")
            print("id: "+listStudent[y]["id"]+" name: "+listStudent[y]["name"])
            print("Course:")
            print("id: "+listCourse[x]["id"]+" name: "+listCourse[x]["name"])
            n = input("Mark: ")
            marks = mark(n)
            mark_info = {
                "course": listCourse[x],
                "student": listStudent[y],
                "marks": marks
            }
            liskMark.append(mark_info)
def printMark():
    for _ in range(numberStudent*numberCourse):
        print("course:"+liskMark[_]["course"]["name"]+" student id: "+liskMark[_]["student"]["id"]+" name: "+liskMark[_]["student"]["name"]+" mark: "+liskMark[_]["marks"]["mark"]+"\n")


print("0. Exit\n1. input number of students\n2. input student information\n3. input number of course\n4. input course info\n5. input mark\n6. print student\n7. print course\n8. print mark")
while True :
    choice = int(input("please enter the choice: \n"))
    if choice == 0:
        break
    if choice == 1:
        n = input("enter the number of student: ")
        inputNumberStudent(n)
    if choice == 2:
        if numberStudent == 0:
            print("no student please enter number of students\n")
            continue
        inputInformation()
    if choice == 3:
        n = input("enter number of course: ")
        inputNumberCourse(n)
    if choice == 4:
        if numberCourse == 0:
            print("no course available please enter the number of course\n")
            continue    
        inputCourse()
    if choice == 5:
        if numberCourse == 0 or numberStudent == 0:
            print("no course or no student ")
            continue
        markInput()
    if choice == 6:
        if numberStudent == 0:
            print("no student")
            continue
        printStudent()
    if choice == 7:
        if numberCourse == 0:
            print("no course")
            continue
        printCourse()
    if choice == 8:
        if numberCourse == 0 or numberStudent == 0:
            print("no student or no course")
            continue
        printMark()
