from datetime import datetime
month = datetime.now().strftime('%d-%m')
def take_att() : 
    hol = input('is today a holiday ? (y/n) : ')
    F_H = open(f'attendance_{month[3:5]}.txt','a')
    if hol == 'n' : 
        F_H2 = open('stud_list.txt','r')
        studs = F_H2.readlines()
        tod_att = []
        for i in studs : 
            att = input(i[:-6]+" : ")
            tod_att.append(att)
        if month[0:2] == '01' :
            F_H.write("        ")
            for i in studs : 
                F_H.write(i[:-1]+"    ")
            F_H.write('\n')
        F_H.write(month[:2])
        a = 6
        for i in range(len(tod_att)) :
            F_H.write(" "*(a)+tod_att[i])
            a = len(studs[i][:-1])+3
        F_H.write('\n')
        F_H.close()
    else : 
        F_H.write(month[0:2] + 'HOLIDAY')
