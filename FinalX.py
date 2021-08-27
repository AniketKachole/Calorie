from tkinter import *
from tkinter import *
from dictall import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk

root = Tk()
root.geometry('1536x864+0+0')
root.title("Calorie Manager")

files = open('cal.txt', 'r')
cal=(files.read())
calorie=(cal)


files = open('calb.txt','r')
calb=(files.read())
calorieB = float(calb)

files = open('calL.txt','r')
calL=(files.read())
calorieL = float(calL)

files = open('cald.txt','r')
cald=(files.read())
calorieD = float(cald)

files = open('calsn.txt','r')
calsn=(files.read())
caloriesn= float(calsn)

#files = open('reqcal.txt','r')
#calreq=(files.read())
#limits=(calreq)

files = open('calreqint.txt','r')
caloriereqstr=files.read()
caloriereq=int(caloriereqstr)

'''
files = open('calsport.txt', 'r')
calsport=(files.read())
caloriespo = int(calsport)
'''
files = open('foodeaten.txt','r')
foodt=(files.read())
'''
files = open('sportsplayed.txt','r')
sports=(files.read())
'''
files = open('reqcal.txt','r')
limitset=files.read()

acti={"Sedentary (little or no exercise)":1.2, 'Lightly active (exercise 1–3 days/week)':1.375, 'Moderately active (exercise 3–5 days/week)':1.55, 'Active (exercise 6–7 days/week)':1.725, 'Very active (hard exercise 6–7 days/week)':1.9}

finalbg = ImageTk.PhotoImage(file="1.jpg")
back=Label(root,image=finalbg)
back.place(x=0,y=0)



F1= Frame(root, relief=SUNKEN)
F1.place(x=33, y= 330, width= 1450, height= 500)

F2= Frame(root, relief=RAISED)
F2.place(x=33, y= 60, width= 1450, height= 270)

F1bg=Label(F1,image=finalbg)
F1bg.place(x=0,y=0)

F2bg=Label(F2,image=finalbg)
F2bg.place(x=0,y=0)


def dailycalorie():
    global caloriereq, limitset
    if weight.get() == "":
        messagebox.showerror('Error', 'Enter Weight')
    elif heighth.get() == "":
        messagebox.showerror("Error", "Enter Height")
    elif age.get() == "":
        messagebox.showerror('Error', 'Enter Age')
    elif genderentry.get() == "Select":
        messagebox.showerror('Error', "Enter Gender")
    elif activeentry.get() == "Select":
        messagebox.showerror("Error", "Select activity level")
    else:
        w = int(weight.get())
        h = int(heighth.get())
        a = int(age.get())
        g = str(genderentry.get())
        at = str(activeentry.get())
        if g == "Male":
            if at in acti:
                c=acti[at]
                caloriereq=int((10*w+6.25*h-5*a+5)*c)
                files = open('calreqint.txt','w')
                files.write(str(caloriereq))

                netreq=(f'Daily '+f'{caloriereq}' + f' cal required')
                calculation.config(text=netreq)
                limitset = (f'Limit ' + f'{caloriereq - 100}' + f' - ' + f'{caloriereq + 100}')
                calrequiredlbl.config(text=limitset)
                files = open('reqcal.txt', 'w')
                files.write(str(limitset))
        elif g == "Female":
            if at in acti:
                c=acti[at]
                caloriereq=int((10*w+6.25*h-5*a-161)*c)
                files = open('calreqint.txt','w')
                files.write(str(caloriereq))
                netreq=(f'Daily '+f'{caloriereq}' + f'cal required')
                calculation.config(text=netreq)
                limitset = (f'Limit ' + f'{caloriereq - 100}' + f' - ' + f'{caloriereq + 100}')
                calrequiredlbl.config(text=limitset)
                files = open('reqcal.txt', 'w')
                files.write((limitset))

    weight.set("")
    heighth.set("")
    age.set("")
    genderentry.set("Select")
    activeentry.set("Select")


def totalcalorie():
    global caloriereq
    calorie = int(calorieB+calorieL+calorieD+caloriesn)
    tt.config(text=calorie)
    file = open('cal.txt','w')
    file.seek(0)
    file.write(str(calorie))

    if calorie < int(caloriereq-100):
        ttr.config(text=f'Short of '+f'{int(caloriereq-100-calorie)}'+f' calories')
        ttr.config(bg="yellow")
    elif calorie > int(caloriereq+100):
        ttr.config(text=f'Exceeded by'+f'{int(caloriereq+100-calorie)}'+f' calories')
        ttr.config(bg='red')
    else:
        ttr.config(text='Correct')
        ttr.config(bg='green2')

def addition():
    a = str(food.get())
    d = dine.get()
    global calorie, calorieB, calorieL, calorieD, caloriesn, caloriespo
    if d == 'ADD BreakFast':
        if a.lower() == "done":
            dine.set("ADD")
        else:
            if a in All:
                verifylbl.config(text="Food item add successful")
                c = All[a]
                calorieB = calorieB + int(c)
                b = str(totalfood.get())
                total = (f'{b}' + f'\n{a}' + f'({c})')

                totalfood.set(total)
                bt.config(text=calorieB)
                files = open('calb.txt','w')
                files.write(str(calorieB))
                with open('foodeaten.txt','w') as f:
                    f.write(total)


            else:
                verifylbl.config(text="Food Item Invalid")

            food.set("")

    elif d=='ADD Lunch':
        if a in All:
            verifylbl.config(text="Food item add successful")
            c = All[a]
            calorieL = calorieL + int(c)

            b = str(totalfood.get())
            total = (f'{b}' + f'\n{a}' + f'({c})')
            totalfood.set(total)

            lt.config(text=calorieL)
            files = open('calL.txt', 'w')
            files.write(str(calorieL))

            with open('foodeaten.txt', 'w') as f:
                f.write(total)

        else:
            verifylbl.config(text="Food Item Invalid")
        food.set("")

    elif d=="ADD Snack" :
        if a in All:
            verifylbl.config(text="Food item add successful")
            c=All[a]
            caloriesn = caloriesn + int(c)

            b = str(totalfood.get())
            total = (f'{b}' + f'\n{a}' + f'({c})')
            totalfood.set(total)

            sn.config(text=caloriesn)
            files = open('calsn.txt','w')
            files.write(str(caloriesn))

            with open('foodeaten.txt', 'w') as f:
                f.write(total)
        else:
            verifylbl.config(text="Food Item Invalid")
        food.set("")

    elif d == 'ADD Dinner':
        if a in All:
            verifylbl.config(text="Food item add successful")
            c = All[a]
            calorieD = calorieD + int(c)

            b = str(totalfood.get())
            total = (f'{b}' + f'\n{a}' + f'({c})')
            totalfood.set(total)

            dt.config(text=calorieD)
            files = open('cald.txt', 'w')
            files.write(str(calorieD))

            with open('foodeaten.txt', 'w') as f:
                f.write(total)

        else:
            verifylbl.config(text="Food Item Invalid")
        food.set("")
'''
    elif d=='ADD Sport':
        if a in Sportsall:
            verifylbl.config(text="Sports added successfully")
            c=Sportsall[a]
            caloriespo = caloriespo + c

            b= str(totalsport.get())
            total = (f'{b}' + f'\n{a}' + f'({c})')
            totalsport.set(total)
            tt.config(text=calorie)
            spt.config(text=caloriespo)
            files = open('calsport.txt', 'w')
            files.write(str(caloriespo))

            with open('sportsplayed.txt', 'w') as f:
                f.write(total)

    food.set("")
'''

def Breakfast():
    verifylbl.config(text="Dine type set to BreakFast")
    b = str(totalfood.get())
    l = (f'{b}' + f'\nBreakFast')
    totalfood.set(l)
    dine.set("ADD BreakFast")

def Lunch():
    verifylbl.config(text="Dine type set to Lunch")
    b = str(totalfood.get())
    l = (f'{b}' + f'\nLunch')
    totalfood.set(l)
    dine.set("ADD Lunch")

def Dinner():
    verifylbl.config(text="Dine type set to Dinner")
    b = str(totalfood.get())
    l = (f'{b}' + f'\nDinner')
    totalfood.set(l)
    dine.set("ADD Dinner")

def Snack():
    verifylbl.config(text="Type set to Snacks")
    b= str(totalfood.get())
    l= (f'{b}' + f'\nSnack')
    totalfood.set(l)
    dine.set('ADD Snack')
'''
def Sport():
    verifylbl.config(text="Mode set to sport")
    b= str(totalsport.get())
    l=(f'{b}' + f'\nSport')
    totalsport.set(l)
    dine.set("ADD Sport")
'''

def reset():
    file = open("cal.txt", "r+")
    file.seek(0)
    file.truncate(0)
    file.write("0")

    file = open("calb.txt", "r+")
    file.seek(0)
    file.truncate(0)
    file.write("0")

    file = open("calL.txt", "r+")
    file.seek(0)
    file.truncate(0)
    file.write("0")

    file = open("cald.txt", "r+")
    file.seek(0)
    file.truncate(0)
    file.write("0")

    file = open("calsn.txt", "r+")
    file.seek(0)
    file.truncate(0)
    file.write("0")

    file = open("foodeaten.txt", "r+")
    file.seek(0)
    file.truncate(0)
    file.write("Food Eaten Today")

    file = open("reqcal.txt", "r+")
    file.seek(0)
    file.truncate(0)
    file.write("")

    file = open("calreqint.txt", "r+")
    file.seek(0)
    file.truncate(0)
    file.write("0")





    tt.config(text=0)
    bt.config(text=0)
    lt.config(text=0)
    dt.config(text=0)
    sn.config(text=0)

    ttr.config(text="")
    '''
    btr.config(text="")
    ltr.config(text="")
    dtr.config(text="")
    snr.config(text="")
    '''
    totalfood.set("Food Eaten Today")
    breaklbl.config(bg='white')
    lunchlbl.config(bg='white')
    dinnerlbl.config(bg='white')
    snacklbl.config(bg='white')

    calrequiredlbl.config(text="")



# sprt.config(text="")
# spt.config(text=0)


#totalsport.set("Sports Played")


#sportlbl.config(bg='white')

    '''
        file = open("calsport.txt", "r+")
        file.seek(0)
        file.truncate(0)
        file.write("0")



        file = open("sportsplayed.txt", "r+")
        file.seek(0)
        file.truncate(0)
        file.write("Sports Played Today")
    '''

def calreqreset():
    calculation.config(text="")



#.................labels of calorie required
calreqbg = Label(F2, relief=GROOVE, border=10)
calreqbg.place(x=0, y=0, width=1450, height=270)

enterweight=Label(F2,text="Enter Your Weight in Kg",font='Arial 15 bold',relief=SOLID,bd=2)
enterweight.place(x=10,y=10, width=300, height=40)

enterheight=Label(F2, text="Enter Your Height in cm", font='Arial 15 bold', relief=SOLID,bd=2)
enterheight.place(x=10,y=60, width=300, height=40)

enterage=Label(F2, text="Enter Your Age", font='Arial 15 bold', relief=SOLID,bd=2)
enterage.place(x=10,y=110, width=300,height=40)

entergender=Label(F2, text="Enter Your Gender", font='Arial 15 bold', relief=SOLID,bd=2)
entergender.place(x=10,y=160, width=300, height=40)

enterlevel=Label(F2, text="Enter Level of Activity", font='Arial 15 bold', relief=SOLID,bd=2)
enterlevel.place(x=10,y=210, width=300, height=40)
#.................variables
weight=StringVar()
weight.set("")
weightent= Entry(F2,textvar=weight,font="Arial 20",relief=SUNKEN,bd=2 )
weightent.place(x=410,y=10,width=300, height=40)

heighth=StringVar()
heighth.set("")
heightent= Entry(F2,textvar=heighth, font='Arial 20',relief=SUNKEN,bd=2)
heightent.place(x=410, y=60, width=300, height=40)

age=StringVar()
age.set("")
ageent= Entry(F2,textvar=age, font='Arial 20',relief=SUNKEN,bd=2)
ageent.place(x=410, y=110, width=300, height=40)

gender=['Select','Male','Female','Other']
genderentry= ttk.Combobox(F2, value=gender, font=('times new roman', 15,'bold') )
genderentry.place(x=410, y=160, width=300, height=40)
genderentry.current(0)

activity=['Select','Sedentary (little or no exercise)','Lightly active (exercise 1–3 days/week)','Moderately active (exercise 3–5 days/week)', 'Active (exercise 6–7 days/week)','Very active (hard exercise 6–7 days/week)']
activeentry= ttk.Combobox(F2, value=activity, font=('times new roman', 15,'bold') )
activeentry.place(x=410, y=210, width=300, height=40)
activeentry.current(0)

calculatebtn= Button(F2,text="Calculate",font=('Arial 20 bold'),relief=GROOVE,bd=2,command=dailycalorie)
calculatebtn.place(x=820, y= 50, width=300, height=40)

calculation=Label(F2, text="",font="Arial 15 bold", relief=SUNKEN,bd=2)
calculation.place(x=820, y=100, width=300, height=40)

resetbtn = Button(F2,text="Reset",font="Arial 15 bold",relief=RIDGE,bd=4,bg='red3',command=calreqreset)
resetbtn.place(x=1200, y=210,width=200,height=40)





#.............calorie calculator
calBgLbl = Label(F1, relief=GROOVE, border=10)
calBgLbl.place(x=0, y=0, width=1450, height=500)
calorieManageHeader = Label(root,text="Calorie Counter", font=("Garamond", 25), relief=RIDGE, border=5,bg='brown1')
calorieManageHeader.place(x=592, y=5, width=400, height=45)

food = StringVar()
food.set("")
enter = Entry(F1,textvar=food,font="Arial 20 bold", relief=RIDGE, border=5)
enter.place(x=20, y=80, width=300, height=40)

dine = StringVar()
dine.set("ADD")
addBtn= Button(F1, text="ADD",font="Arial 15 bold", relief=RIDGE, border=5, command=addition)
addBtn.place(x=340, y=80, width=100, height=40)

verifylbl = Label(F1, text="",font="Arial 15 bold", relief=SUNKEN)
verifylbl.place(x=20, y=130, width=300, height=40)



totalfood=StringVar()
totalfood.set(foodt)
totalfoodlbl = Label(F1, textvar=totalfood, font="Arial 15 bold", relief=RIDGE, border=5)
totalfoodlbl.place(x=820, y=20)

'''
totalsport=StringVar()
totalsport.set(sports)
totalsportlbl= Label(F1, textvar=totalsport, font="Arial 13 bold", relief=RIDGE, border=5)
totalsportlbl.place(x=1200, y=20)
'''
calrequiredlbl=Label(F1, font="Arial 17 bold", relief=SUNKEN)
calrequiredlbl.place(x=20,y=20, width=300, height=40)


totalcallbl=Button(F1, text="Click here for Total calories",font="Arial 16 bold", relief=RIDGE, border=5,command=totalcalorie)
totalcallbl.place(x=20, y=180, height=40, width=300)


breaklbl=Label(F1, text="Breakfast calorie (20-30)",font="Arial 16 bold", relief=SUNKEN)
breaklbl.place(x=20, y=230, height=40, width=300)
lunchlbl=Label(F1, text="Lunch calorie (50-60)",font="Arial 16 bold", relief=SUNKEN)
lunchlbl.place(x=20, y=280, height=40, width=300)
dinnerlbl=Label(F1, text="Dinner calorie (50-60)",font="Arial 16 bold", relief=SUNKEN)
dinnerlbl.place(x=20, y=330, height=40, width=300)
snacklbl= Label(F1, text="Snack calorie (20-30)", font="Arial 16 bold", relief=SUNKEN)
snacklbl.place(x=20, y=380, width=300, height=40)
#sportlbl= Label(F1, text="Sport calorie", font="Arial 16 bold", relief=RIDGE, border=5)
#sportlbl.place(x=20, y=430, width=300, height=40)


tt = Label(F1, text="",font="Arial 20 bold", relief=SUNKEN)
tt.place(x=340, y=180, height=40, width=100)
bt = Label(F1, text="000",font="Arial 20 bold", relief=SUNKEN)
bt.place(x=340, y=230, height=40, width=100)
lt = Label(F1, text="000",font="Arial 20 bold", relief=SUNKEN)
lt.place(x=340, y=280, height=40, width=100)
dt = Label(F1, text="000",font="Arial 20 bold", relief=SUNKEN)
dt.place(x=340, y=330, height=40, width=100)
sn = Label(F1, text="000", font="Arial 20 bold", relief=SUNKEN)
sn.place(x=340, y=380, height=40, width=100)
#spt=Label(F1, text="000", font="Arial 20 bold", relief=RIDGE, border=5)
#spt.place(x=340, y=430, height=40, width=100)

ttr = Label(F1, text="",font="Arial 15 bold", relief=SUNKEN)
ttr.place(x=460, y=180, height=40, width=300)
'''
btr = Label(F1, text="",font="Arial 15 bold", relief=SUNKEN)
btr.place(x=460, y=230, height=40, width=300)
ltr = Label(F1, text="",font="Arial 15 bold", relief=SUNKEN)
ltr.place(x=460, y=280, height=40, width=300)
dtr = Label(F1, text="",font="Arial 15 bold", relief=SUNKEN)
dtr.place(x=460, y=330, height=40, width=300)
snr = Label(F1, text="", font="Arial 15 bold",relief=SUNKEN)
snr.place(x=460, y=380, height=40, width=300)
#sprt= Label(F1, text="", font="Arial 15 bold", relief=RIDGE, border=5)
#sprt.place(x=460, y=430, width=300, height=40)
'''


breakbtn = Button(F1, text="Breakfast",font="Arial 14 bold", relief=RIDGE, border=5, command=Breakfast)
breakbtn.place(x=450,y=80, width=100, height=40)
lunchbtn = Button(F1, text="Lunch",font="Arial 15 bold", relief=RIDGE, border=5, command=Lunch)
lunchbtn.place(x=560,y=80, width=100, height=40)
dinnerbtn = Button(F1, text="Dinner",font="Arial 15 bold", relief=RIDGE, border=5, command=Dinner)
dinnerbtn.place(x=670,y=80, width=100, height=40)
snackbtn= Button(F1, text="Snacks", font="Arial 15 bold", relief=RIDGE, border=5, command=Snack)
snackbtn.place(x=450, y=130, width= 100, height= 40)
#sportbtn= Button(F1, text="Sport", font="Arial 15 bold", relief=RIDGE, border=5, command=Sport)
#sportbtn.place(x=560, y=130, width=100, height=40)
resetbtn=Button(F1, text="Reset",font="Arial 15 bold",relief=RIDGE, border=5,bg='red3',command=reset)
resetbtn.place(x=1200,y=430, width=200, height=40)


bt.config(text=calorieB)
lt.config(text=calorieL)
dt.config(text=calorieD)
sn.config(text=caloriesn)
calrequiredlbl.config(text=limitset)
#spt.config(text=caloriespo)





if calorie==0:
    totalcallbl.config(bg="white")
if calorieB==0:
    breaklbl.config(bg="white")
if calorieL==0:
    lunchlbl.config(bg="white")
if calorieD==0:
    dinnerlbl.config(bg="white")







root.mainloop()