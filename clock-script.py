#Work Done
#time_values = ["07:24:16","13:48:18","18:48:15","11:47:55","05:46:39","20:35:19","10:51:40","10:16:17","08:17:26","17:48:59","20:04:33","01:35:39","13:23:39","01:56:09","10:50:22","07:41:09","10:20:42","02:19:30","13:41:41","03:17:28"]

from datetime import datetime
#import pytz

def binary_clock(x):

    y = x.split(":")
    #print("Time : ",y)

    #Hours
    b1 = []
    hours = y[0]
    #hours = str(int(y[0])+5)
    #print("Hours : ",hours)
    a1 = [bin(int(i))[::-1][:-2] for i in hours]
    #print("a : ",a)
    k = 0
    while(k < 2):
        if(k == 0):
            if(len(a1[0]) == 2):
                b1.append(a1[0] + "0" * (2 - len(a1[0])) + " " * 2)
            elif(len(a1[0]) == 1):
                b1.append(a1[0] + "0" * (2 - len(a1[0])) + " " * 2)
            elif(len(a1[0]) == 0):
                b1.append(a1[0] + " " * 2)
        else:
            #print(a[1] + " " * (4-len(a[1])))
            b1.append(a1[1] + "0" * (4-len(a1[1])))
        k += 1
    #print("Hours :",b1)

    #Minutes
    b2 = []
    minutes = y[1]
    #minutes = str(int(y[1])+30)
    #print("Minutes :",minutes)
    a2 = [bin(int(i))[::-1][:-2] for i in minutes]
    #print("a2 :",a)
    k = 0
    while(k < 2):
        if(k == 0):
            if(len(a2[0]) == 3):
                b2.append(a2[0] + " ")
            elif(len(a2[0]) == 2):
                b2.append(a2[0] + "0" * (3 - len(a2[0])) + " ")
            elif(len(a2[0]) == 1):
                b2.append(a2[0] + "0" * (3 - len(a2[0])) + " ")
        else:
            b2.append(a2[1] + "0" * (4-len(a2[1])))
        k += 1
    #print("Minutes :",b2)

    #Seconds
    b3 = []
    seconds = y[-1]
    #print("Seconds :",seconds)
    a3 = [bin(int(i))[::-1][:-2] for i in seconds]
    #print(a)
    k = 0
    while(k < 2):
        if(k == 0):
            if(len(a3[0]) == 3):
                b3.append(a3[0] + " ")
            elif(len(a3[0]) == 2):
                b3.append(a3[0] + "0" * (3 - len(a3[0])) + " ")
            elif(len(a3[0]) == 1):
                b3.append(a3[0] + "0" * (3 - len(a3[0])) + " ")
        else:
            b3.append(a3[1] + "0" * (4-len(a3[1])))
        k += 1
    #print("Seconds :",b3)

    initial = []
    #print(b1)
    #print(b2)
    #print(b3)
    for i in b1:
        initial.extend(list(i))
    for i in b2:
        initial.extend(list(i))
    for i in b3:
        initial.extend(list(i))
    #print("Initial : ",initial)


    z = 0
    final = []
    while(z < len(initial)):
        final.append(initial[z:z+4])
        z += 4

    #print("Final :",final)


    M = [[m[i] for m in final] for i in range(4)][::-1]
    #Adding ':'s
    M[0].insert(2,':')
    M[0].insert(5,':')
    M[1].insert(2,':')
    M[1].insert(5,':')
    M[2].insert(2,':')
    M[2].insert(5,':')
    M[3].insert(2,':')
    M[3].insert(5,':')

    #Adding binaries
    M[0].insert(0,'8 ')
    M[1].insert(0,'4 ')
    M[2].insert(0,'2 ')
    M[3].insert(0,'1 ')
    #print("M : ",M)

    #print("M_final : ",M_final)
  
    N = ["".join(k) for k in M]
    N.insert(0,'  HH:MM:SS')
    #print("N : ",N)
    #print("N : ",N,sep="\n")
    return "\n".join(N)

#IST = pytz.timezone('Asia/Kolkota')

now = datetime.now()
#now = datetime.now(IST)

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print("-------------------------------")
print(binary_clock(current_time))
