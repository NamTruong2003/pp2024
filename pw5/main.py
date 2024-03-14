import input as ip
from output import *
from input import compress_files,decompress_files
import os
if os.path.exists('students.dat'):
    decompress_files()
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
        with open("students.txt","w") as f:
            for _ in range(ip.numberStudent):
                f.write(f"id: {ip.listStudent[_].id} name: {ip.listStudent[_].name} DoB: {ip.listStudent[_].DoB} GPA: {ip.listStudent[_].GPA}\n")


    if choice == 2:
        if ip.numberCourse != 0:
            print('Course list are already exist , please choose other choice!')
            continue
        ip.inputCourse()
        with open("courses.txt","w") as f:
            for _ in range(ip.numberCourse):
                f.write(f"id: {ip.listCourse[_].id} name: {ip.listCourse[_].name} credit: {ip.listCourse[_].credit}\n")
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
        with open("marks.txt","w") as f:
            for _ in range(ip.numberStudent*ip.numberCourse):
                f.write(f"course: {ip.listMark[_].course} id: {ip.listMark[_].id} name: {ip.listMark[_].name} mark: {ip.listMark[_].mark}\n")
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
compress_files() 
