import input as ip
from output import *
print("0. Exit\n1. input infor of students\n2. input infor of course\n3. print students list\n4. print courses list\n5. input mark\n6. print marks list\n7. Calculate GPA")
while True:
    choice = int(input("please enter the choice: \n"))
    if choice == 0:
        break
    if choice == 1:
        if ip.numberStudent != 0:
            print('student list are already exist , please choose other choice!')
            continue
        ip.inputInforStudent()
    if choice == 2:
        if ip.numberCourse != 0:
            print('Course list are already exist , please choose other choice!')
            continue
        ip.inputCourse()
    if choice == 3:
        if ip.numberStudent == 0:
            print('no student in list of student!')
            continue
        ip.printStudent()
    if choice == 4:
        if ip.numberCourse == 0:
            print('no course in list of course!')
            continue
        ip.printCourse()
    if choice == 5:
        if ip.listMark != []:
            print('the list of mark already exist!')
            continue
        if ip.numberCourse == 0 :
            print('no course')
            continue
        if ip.numberStudent == 0:
            print('no student')
            continue
        ip.inputMark()
    if choice == 6:
        if ip.listMark == []:
            print("mark list doesn't exist ")
            continue
        if ip.numberCourse == 0 :
            print('no course')
            continue
        if ip.numberStudent == 0:
            print('no student')
            continue
        if __name__ == '__main__':
            curses.wrapper(main)
    if choice == 7:
        if ip.listMark == []:
            print('the list of mark does not exist!')
            continue
        if ip.numberCourse == 0 :
            print('no course')
            continue
        if ip.numberStudent == 0:
            print('no student')
            continue
        ip.calculate_avarage_GPA()
 
