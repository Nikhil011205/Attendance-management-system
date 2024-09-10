import admin 
import take_attendance
print('WELCOME TO THE ATTENDACE MANAGEMENT SYSTEM')
pw = '12345'
teach = input('are you an admin or a teacher (a/t) : ').lower()
if teach == 'a' : 
    password = input('Enter password : ')
    if pw == password : 
        print('HELLO ADMIN')
        print('1. add a student')
        print('2. get attendance percentage of a student')
        print('3. remove a student')
        op = int(input('Enter a operation : '))
        if op==1 : 
            name = input("Enter the new student's name : ")
            roll = input('Enter his/her roll number : ')
            admin.add_stud(name,roll)
            print('JOB DONE!')
        elif op==2 :
            roll = input('Enter his/her roll number : ')
            print(admin.get_perc_attendance(roll))
        elif op==3 : 
            roll = input('Enter his/her roll number : ')
            admin.remove_stud(roll)
            print('JOB DONE!')
        else : 
            print('no such operation exists')
        print('THANKS FOR USING THIS PROGRAM')
    else : 
        print('wrong password')
if teach == 't' : 
    print('1. take attendance')
    print('2. view attendance list')
    print('3. view students list')
    print('4. get percentage attendance')
    op2 = input('Enter operation you would like to perform : ')
    if op2 == '1' : 
        take_attendance.take_att()
    elif op2 == '2' : 
        mon = input("Which month's attendance (mm format) : ")
        try : 
            F_H = open('attendance_'+mon+'.txt','r')
            print(F_H.read())
        except : 
            print("that month's attendance does not exist")
    elif op == '3' : 
        f = open('stud_list','r')
        print(f.read())
    elif op == '4' : 
        roll = input('Enter his/her roll number : ')
        print(admin.get_perc_attendance(roll))
    else :
        print('operation does not exist')
    print('THANKS FOR USING THIS PROGRAM')
