from datetime import datetime

Date = datetime.now().strftime('%d-%m')

def add_stud(name,roll_no) : 
    F_H = open('stud_list.txt','a+')
    F_H.write(name+" ("+roll_no+")"+"\n")
    F_H.close()
    F_H2 = open('attendance_'+Date[3:]+'.txt','r')
    bus = F_H2.readlines()
    bus[0] = bus[0][:-1] #the minus 1 to remove the new line func
    bus[0] += name+" ("+roll_no+")    \n"
    F_H2 = open('attendance_'+Date[3:]+'.txt','w')
    F_H2.writelines(bus)
def lines() : 
    global line
    F_H = open('attendance_'+Date[3:]+'.txt','r')
    line = len(F_H.readlines())-1
    return line
def get_perc_attendance(roll) : 
    lines()
    F_H = open('attendance_'+Date[3:]+'.txt','r')
    F_H.readline()
    F_H2 = open('stud_list.txt','r')
    stud = F_H2.readlines()
    studs = []
    for i in stud : 
        studs.append(i[:-6]+" : ")
    att = []
    for i in range(line) : 
        curr_att = []
        l = F_H.readline()
        for j in l : 
            if j == "P" or j == "A" : 
                curr_att.append(j)
        att.append(curr_att)
    count = 0
    for i in att : 
        try : 
            if i[int(roll)-1] == "P" : 
                count+=1
        except :
            pass
    stud_name = studs[int(roll)-1][:-4]
    perc = (count/len(att))*100
    return stud_name+"'s attendance pecentage : "+str(perc)+"%"

def remove_stud(roll) : 
    F_H = open('stud_list.txt','r')
    L = F_H.readlines()
    for i in L :
        if roll in i : 
            L.remove(i)
            break
    F_H2 = open('stud_list.txt','w')
    F_H2.writelines(L)
    F_H3 = open('attendance_'+Date[3:]+'.txt','r')
    bus = F_H3.readlines()
    att = []
    for j in bus[1:] : 
        try : 
            List = j.split()[:-1] # the minus 1 is to remove the new line func
            att.extend(List.pop(int(roll)))
        except : 
            att.extend(j.split())
    F_H4 = open('attendance_'+Date[3:]+'.txt','w')
    F_H4.write("        ")
    for i in L : 
        F_H4.write(i[:-1]+"    ")
    F_H4.write('\n')
    F_H4.write(Date[:2])
    a = 6
    x = 0
    for j in range(len(bus)-1) : 
        for i in range(len(L)) :
            F_H4.write(" "*(a)+att[1:][x])
            a = len(L[i][:-1])+3
        F_H4.write('\n')
    F_H.close()
    F_H2.close()
    F_H3.close()
    F_H4.close()