from Tkinter import *
from time import sleep
import tkMessageBox
root = Tk()
root.title("Memory Card Game!")
app = Frame(root)
app.grid()
button_flag1 =  button_flag2 = button_flag3 = button_flag4 = button_flag5 = button_flag6 = button_flag7 = button_flag8 = True
button_flag9 = button_flag10 = button_flag11 = button_flag12 = button_flag13 = button_flag14 = True
button_flag15 =  button_flag16 = button_flag17 = button_flag18 = button_flag19 = button_flag20 = button_flag21 = button_flag22 = True
button_flag23 = button_flag24 = button_flag25 = button_flag26 = button_flag27 = button_flag28 = True
flag1 = flag2 = flag3 = flag4 = flag5 = flag6 = flag7 = flag8 = flag9 = flag10 = flag11 = flag12 = flag13 = flag14 = 0
flag15 = flag16 = flag17 = flag18 = flag19 = flag20 = flag21 = flag22 = flag23 = flag24 = flag25 = flag26 = flag27 = flag28 = 0
clicks = 0

def img1():
    global button_flag1,clicks,flag1
    print (button_flag1)
    button_flag1 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but1 = Button(app, text="1", image=but_image,command = click1)
    but1.grid(row=0, column=0, sticky=W)
    but1.image = but_image
    clicks = clicks - 1
    flag1 = 0
    #clicks = clicks + 1
    print "Closed click(s)",clicks
    return

def img2():
    global button_flag2,clicks,flag2
    print (button_flag2)
    button_flag2 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but2 = Button(app, text="2", image=but_image,command = click2)
    but2.grid(row=0, column=1, sticky=W)
    but2.image = but_image
    clicks = clicks - 1
    flag2 = 0
    print "Closed click(s)", clicks
    return

def img3():
    global button_flag3,clicks,flag3
    print (button_flag3)
    button_flag3 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but3 = Button(app, text="3", image=but_image,command = click3)
    but3.grid(row=0, column=2, sticky=W)
    but3.image = but_image
    clicks = clicks - 1
    flag3 = 0
    print "Closed click(s)", clicks
    return

def img4():
    global button_flag4,clicks,flag4
    print (button_flag4)
    button_flag4 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but4 = Button(app, text="4", image=but_image,command = click4)
    but4.grid(row=0, column=3, sticky=W)
    but4.image = but_image
    clicks = clicks - 1
    flag4 = 0
    print "Closed click(s)", clicks
    return

def img5():
    global button_flag5,flag5,clicks
    print (button_flag5)
    button_flag5 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but5 = Button(app, text="5", image=but_image,command = click5)
    but5.grid(row=0, column=4, sticky=W)
    but5.image = but_image
    flag5 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img6():
    global button_flag6,flag6,clicks
    print (button_flag6)
    button_flag6 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but6 = Button(app, text="6", image=but_image,command = click6)
    but6.grid(row=0, column=5, sticky=W)
    but6.image = but_image
    flag6 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img7():
    global button_flag7,flag7,clicks
    print (button_flag7)
    button_flag7 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but7 = Button(app, text="6", image=but_image,command = click7)
    but7.grid(row=0, column=6, sticky=W)
    but7.image = but_image
    flag7 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return
def img8():
    global button_flag8,flag8,clicks
    print (button_flag8)
    button_flag8 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but8 = Button(app, text="8", image=but_image,command = click8)
    but8.grid(row=1, column=0, sticky=W)
    but8.image = but_image
    flag8 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img9():
    global button_flag9,flag9,clicks
    print (button_flag9)
    button_flag9 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but9 = Button(app, text="9", image=but_image,command = click9)
    but9.grid(row=1, column=1, sticky=W)
    but9.image = but_image
    flag9 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img10():
    global button_flag10,flag10,clicks
    print (button_flag10)
    button_flag10 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but10 = Button(app, text="10", image=but_image,command = click10)
    but10.grid(row=1, column=2, sticky=W)
    but10.image = but_image
    flag10 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img11():
    global button_flag11,flag11,clicks
    print (button_flag11)
    button_flag11 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but11 = Button(app, text="11", image=but_image,command = click11)
    but11.grid(row=1, column=3, sticky=W)
    but11.image = but_image
    flag11 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img12():
    global button_flag12,flag12,clicks
    print (button_flag12)
    button_flag12 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but12 = Button(app, text="12", image=but_image,command = click12)
    but12.grid(row=1, column=4, sticky=W)
    but12.image = but_image
    falg12 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img13():
    global button_flag13,flag13,clicks
    print (button_flag13)
    button_flag13 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but13 = Button(app, text="13", image=but_image,command = click13)
    but13.grid(row=1, column=5, sticky=W)
    but13.image = but_image
    clicks = clicks - 1
    falg13 = 0
    print "Closed click(s)", clicks
    return

def img14():
    global button_flag14,flag14,clicks
    print (button_flag14)
    button_flag14 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but14 = Button(app, text="14", image=but_image,command = click14)
    but14.grid(row=1, column=6, sticky=W)
    but14.image = but_image
    clicks = clicks - 1
    flag14 = 0
    print "Closed click(s)", clicks
    return

def img15():
    global button_flag15,flag15,clicks
    print (button_flag15)
    button_flag15 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but15 = Button(app, text="15", image=but_image,command = click15)
    but15.grid(row=2, column=0, sticky=W)
    but15.image = but_image
    flag15 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img16():
    global button_flag16,flag16,clicks
    print (button_flag16)
    button_flag16 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but16 = Button(app, text="16", image=but_image,command = click16)
    but16.grid(row=2, column=1, sticky=W)
    but16.image = but_image
    flag16 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img17():
    global button_flag17,flag17,clicks
    print (button_flag17)
    button_flag17 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but17 = Button(app, text="17", image=but_image,command = click17)
    but17.grid(row=2, column=2, sticky=W)
    but17.image = but_image
    clicks = clicks - 1
    flag17 = 0
    print "Closed click(s)", clicks
    return

def img18():
    global button_flag18,flag18,clicks
    print (button_flag18)
    button_flag18 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but18 = Button(app, text="18", image=but_image,command = click18)
    but18.grid(row=2, column=3, sticky=W)
    but18.image = but_image
    flag18 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img19():
    global button_flag19,flag19,clicks
    print (button_flag19)
    button_flag19 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but19 = Button(app, text="19", image=but_image,command = click19)
    but19.grid(row=2, column=4, sticky=W)
    but19.image = but_image
    flag19 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img20():
    global button_flag20,flag20,clicks
    print (button_flag20)
    button_flag20 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but20 = Button(app, text="20", image=but_image,command = click20)
    but20.grid(row=2, column=5, sticky=W)
    but20.image = but_image
    flag20 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img21():
    global button_flag21,flag21,clicks
    print (button_flag21)
    button_flag21 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but21 = Button(app, text="21", image=but_image,command = click21)
    but21.grid(row=2, column=6, sticky=W)
    but21.image = but_image
    flag21 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return
def img22():
    global button_flag22,flag22,clicks
    print (button_flag22)
    button_flag22 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but22 = Button(app, text="22", image=but_image,command = click22)
    but22.grid(row=3, column=0, sticky=W)
    but22.image = but_image
    flag22 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img23():
    global button_flag23,flag23,clicks
    print (button_flag23)
    button_flag23 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but23 = Button(app, text="23", image=but_image,command = click23)
    but23.grid(row=3, column=1, sticky=W)
    but23.image = but_image
    flag23 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img24():
    global button_flag24,flag24,clicks
    print (button_flag24)
    button_flag24 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but24 = Button(app, text="24", image=but_image,command = click24)
    but24.grid(row=3, column=2, sticky=W)
    but24.image = but_image
    flag24 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img25():
    global button_flag25,flag25,clicks
    print (button_flag25)
    button_flag25 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but25 = Button(app, text="25", image=but_image,command = click25)
    but25.grid(row=3, column=3, sticky=W)
    but25.image = but_image
    flag25 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img26():
    global button_flag26,flag26,clicks
    print (button_flag26)
    button_flag26 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but26 = Button(app, text="26", image=but_image,command = click26)
    but26.grid(row=3, column=4, sticky=W)
    but26.image = but_image
    flag26 = 0
    clicks = clicks - 1
    print "Closed click(s)",clicks
    return


def img27():
    global button_flag27,flag27,clicks
    print (button_flag27)
    button_flag27 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but27 = Button(app, text="27", image=but_image,command = click27)
    but27.grid(row=3, column=5, sticky=W)
    but27.image = but_image
    flag27 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return

def img28():
    global button_flag28,flag28,clicks
    print (button_flag28)
    button_flag28 = True
    but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
    but28 = Button(app, text="28", image=but_image,command = click28)
    but28.grid(row=3, column=6, sticky=W)
    but28.image = but_image
    flag28 = 0
    clicks = clicks - 1
    print "Closed click(s)", clicks
    return


def click1():
    global button_flag1,but1,flag1,clicks

    if button_flag1:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\2_clover.gif")
        but1 = Button(app ,text="1", image = my_image,command = img1)
        but1.grid(row=0, column=0, sticky=W)
        but1.image = my_image
        #button_flag1 = False
        flag1 = 1
        clicks = clicks + 1
        print (button_flag1,flag1)
        print "Open click(s)" , clicks
    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but1 = Button(app, text="1", image=but_image)
        but1.grid(row=0, column=0, sticky=W)
        but1.image = but_image
        button_flag1 = True
        print (button_flag1)
    return
def click2():
    global button_flag2,but2,flag2,clicks

    if button_flag2:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\3_dice.gif")
        but2 = Button(app ,text="2", image = my_image,command = img2)
        but2.grid(row=0, column=1, sticky=W)
        but2.image = my_image
        #button_flag2 = False
        flag2 = 1
        clicks = clicks + 1
        print "Open click(s)",clicks
        print (button_flag2, flag2)
    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but2 = Button(app, text="2", image=but_image)
        but2.grid(row=0, column=1, sticky=W)
        but2.image = but_image
        button_flag2 = True
        print (button_flag2)
    return

def click3():
    global button_flag3,but3,flag3,clicks

    if button_flag3:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\4_spade.gif")
        but3 = Button(app ,text="3", image = my_image,command = img3)
        but3.grid(row=0, column=2, sticky=W)
        but3.image = my_image
        #button_flag3 = False
        flag3 = 1
        clicks = clicks + 1
        print "Open click(s)", clicks
        print (button_flag3,flag3)
    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but3 = Button(app, text="3", image=but_image)
        but3.grid(row=0, column=2, sticky=W)
        but3.image = but_image
        button_flag3 = True
        print (button_flag3)
    return

def click4():
    global button_flag4,but4,flag4,clicks

    if button_flag4:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\5_hearts.gif")
        but4 = Button(app ,text="4", image = my_image,command = img4)
        but4.grid(row=0, column=3, sticky=W)
        but4.image = my_image
        #button_flag4 = False
        flag4 = 1
        print (button_flag4,flag4)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but4 = Button(app, text="4", image=but_image)
        but4.grid(row=0, column=3, sticky=W)
        but4.image = but_image
        button_flag4 = True
        print (button_flag4)
    return
def click5():
    global button_flag5,but5,flag5,clicks

    if button_flag5:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\6_hearts.gif")
        but5 = Button(app ,text="5", image = my_image,command = img5)
        but5.grid(row=0, column=4, sticky=W)
        but5.image = my_image
        #button_flag5 = False
        flag5 = 1
        print (button_flag5,flag5)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but5 = Button(app, text="5", image=but_image)
        but5.grid(row=0, column=4, sticky=W)
        but5.image = but_image
        button_flag5 = True
        print (button_flag5)
    return
def click6():
    global button_flag6,but6,flag6,clicks

    if button_flag6:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\7_clover.gif")
        but6 = Button(app ,text="6", image = my_image,command = img6)
        but6.grid(row=0, column=5, sticky=W)
        but6.image = my_image
        #button_flag6 = False
        flag6 = 1
        print (button_flag6,flag6)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but6 = Button(app, text="6", image=but_image)
        but6.grid(row=0, column=5, sticky=W)
        but6.image = but_image
        button_flag6 = True
        print (button_flag6)
    return
def click7():
    global button_flag7,but7,flag7,clicks

    if button_flag7:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\8_spade.gif")
        but7 = Button(app ,text="7", image = my_image,command = img7)
        but7.grid(row=0, column=6, sticky=W)
        but7.image = my_image
        #button_flag7 = False
        flag7 = 1
        print (button_flag7,flag7)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but7 = Button(app, text="7", image=but_image)
        but7.grid(row=0, column=6, sticky=W)
        but7.image = but_image
        button_flag7 = True
        print (button_flag7)
    return

def click8():
    global button_flag8,but8,flag8,clicks

    if button_flag8:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\10_dice.gif")
        but8 = Button(app ,text="8", image = my_image,command = img8)
        but8.grid(row=1, column=0, sticky=W)
        but8.image = my_image
        #button_flag8 = False
        flag8 = 1
        print (button_flag8,flag8)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but8 = Button(app, text="8", image=but_image)
        but8.grid(row=1, column=0, sticky=W)
        but8.image = but_image
        button_flag8 = True
        print (button_flag8)
    return
def click9():
    global button_flag9,but9,flag9,clicks

    if button_flag9:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\a_heart.gif")
        but9 = Button(app ,text="9", image = my_image,command = img9)
        but9.grid(row=1, column=1, sticky=W)
        but9.image = my_image
        #button_flag9 = False
        flag9 = 1
        print (button_flag9,flag9)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but9 = Button(app, text="9", image=but_image)
        but9.grid(row=1, column=1, sticky=W)
        but9.image = but_image
        button_flag9 = True
        print (button_flag9)
    return

def click10():
    global button_flag10,but10,flag10,clicks

    if button_flag10:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\j_clover.gif")
        but10 = Button(app ,text="10", image = my_image,command = img10)
        but10.grid(row=1, column=2, sticky=W)
        but10.image = my_image
        #button_flag10 = False
        flag10 = 1
        print (button_flag10,flag10)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but10 = Button(app, text="10", image=but_image)
        but10.grid(row=1, column=2, sticky=W)
        but10.image = but_image
        button_flag10 = True
        print (button_flag10)
    return

def click11():
    global button_flag11,but11,flag11,clicks

    if button_flag11:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\joker.gif")
        but11 = Button(app ,text="11", image = my_image,command = img11)
        but11.grid(row=1, column=3, sticky=W)
        but11.image = my_image
        #button_flag11 = False
        flag11 = 1
        print (button_flag11,flag11)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but11 = Button(app, text="11", image=but_image)
        but11.grid(row=1, column=3, sticky=W)
        but11.image = but_image
        button_flag11 = True
        print (button_flag11)
    return
def click12():
    global button_flag12,but12,flag12,clicks

    if button_flag12:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\k_spade.gif")
        but12 = Button(app ,text="12", image = my_image,command = img12)
        but12.grid(row=1, column=4, sticky=W)
        but12.image = my_image
        #button_flag12 = False
        flag12 = 1
        print (button_flag12,flag12)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but12 = Button(app, text="12", image=but_image)
        but12.grid(row=1, column=4, sticky=W)
        but12.image = but_image
        button_flag12 = True
        print (button_flag12)
    return
def click13():
    global button_flag13,but13,flag13,clicks

    if button_flag13:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\q_spade.gif")
        but13 = Button(app ,text="13", image = my_image,command = img13)
        but13.grid(row=1, column=5, sticky=W)
        but13.image = my_image
        #button_flag13 = False
        flag13 = 1
        print (button_flag13,flag13)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but13 = Button(app, text="13", image=but_image)
        but13.grid(row=1, column=5, sticky=W)
        but13.image = but_image
        button_flag13 = True
        print (button_flag13)
    return
def click14():
    global button_flag14,but14,flag14,clicks

    if button_flag14:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\th.gif")
        but14 = Button(app ,text="14", image = my_image,command = img14)
        but14.grid(row=1, column=6, sticky=W)
        but14.image = my_image
        #button_flag14 = False
        flag14 = 1
        print (button_flag14,flag14)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but14 = Button(app, text="7", image=but_image)
        but14.grid(row=1, column=6, sticky=W)
        but14.image = but_image
        button_flag14 = True
        print (button_flag14)
    return

def click15():
    global button_flag15,but15,flag15,clicks

    if button_flag15:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\2_clover.gif")
        but15 = Button(app ,text="15", image = my_image,command = img15)
        but15.grid(row=2, column=0, sticky=W)
        but15.image = my_image
        #button_flag15 = False
        flag15 = 1
        print (button_flag15,flag15)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but15 = Button(app, text="15", image=but_image)
        but15.grid(row=2, column=0, sticky=W)
        but15.image = but_image
        button_flag15 = True
        print (button_flag15)
    return
def click16():
    global button_flag16,but16,flag16,clicks

    if button_flag16:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\3_dice.gif")
        but16 = Button(app ,text="16", image = my_image,command = img16)
        but16.grid(row=2, column=1, sticky=W)
        but16.image = my_image
        #button_flag16 = False
        flag16 = 1
        print (button_flag16,flag16)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but16 = Button(app, text="16", image=but_image)
        but16.grid(row=2, column=1, sticky=W)
        but16.image = but_image
        button_flag16 = True
        print (button_flag16)
    return

def click17():
    global button_flag17,but17,flag17,clicks

    if button_flag17:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\4_spade.gif")
        but17 = Button(app ,text="17", image = my_image,command = img17)
        but17.grid(row=2, column=2, sticky=W)
        but17.image = my_image
        #button_flag17 = False
        flag17 = 1
        print (button_flag17,flag17)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but17 = Button(app, text="17", image=but_image)
        but17.grid(row=2, column=2, sticky=W)
        but17.image = but_image
        button_flag17 = True
        print (button_flag17)
    return

def click18():
    global button_flag18,but18,flag18,clicks

    if button_flag18:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\5_hearts.gif")
        but18 = Button(app ,text="18", image = my_image,command = img18)
        but18.grid(row=2, column=3, sticky=W)
        but18.image = my_image
        #button_flag18 = False
        flag18 = 1
        print (button_flag18,flag18)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but18 = Button(app, text="18", image=but_image)
        but18.grid(row=2, column=3, sticky=W)
        but18.image = but_image
        button_flag18 = True
        print (button_flag18)
    return
def click19():
    global button_flag19,but19,flag19,clicks

    if button_flag19:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\6_hearts.gif")
        but19 = Button(app ,text="19", image = my_image,command = img19)
        but19.grid(row=2, column=4, sticky=W)
        but19.image = my_image
        #button_flag19 = False
        flag19 = 1
        print (button_flag19,flag19)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but19 = Button(app, text="19", image=but_image)
        but19.grid(row=2, column=4, sticky=W)
        but19.image = but_image
        button_flag19 = True
        print (button_flag19)
    return
def click20():
    global button_flag20,but20,flag20,clicks

    if button_flag20:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\7_clover.gif")
        but20 = Button(app ,text="20", image = my_image,command = img20)
        but20.grid(row=2, column=5, sticky=W)
        but20.image = my_image
        #button_flag20 = False
        flag20 = 1
        print (button_flag20,flag20)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but20 = Button(app, text="20", image=but_image)
        but20.grid(row=2, column=5, sticky=W)
        but20.image = but_image
        button_flag20 = True
        print (button_flag20)
    return
def click21():
    global button_flag21,but21,flag21,clicks

    if button_flag21:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\8_spade.gif")
        but21 = Button(app ,text="21", image = my_image,command = img21)
        but21.grid(row=2, column=6, sticky=W)
        but21.image = my_image
        #button_flag21 = False
        flag21 = 1
        print (button_flag21,flag21)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but21 = Button(app, text="21", image=but_image)
        but21.grid(row=2, column=6, sticky=W)
        but21.image = but_image
        button_flag21 = True
        print (button_flag21)
    return

def click22():
    global button_flag22,but22,flag22,clicks

    if button_flag22:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\10_dice.gif")
        but22 = Button(app ,text="22", image = my_image,command = img22)
        but22.grid(row=3, column=0, sticky=W)
        but22.image = my_image
        #button_flag22 = False
        flag22 = 1
        print (button_flag22,flag22)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but22 = Button(app, text="22", image=but_image)
        but22.grid(row=3, column=0, sticky=W)
        but22.image = but_image
        button_flag22 = True
        print (button_flag22)
    return
def click23():
    global button_flag23,but23,flag23,clicks

    if button_flag23:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\a_heart.gif")
        but23 = Button(app ,text="23", image = my_image,command = img23)
        but23.grid(row=3, column=1, sticky=W)
        but23.image = my_image
        #button_flag23 = False
        flag23 = 1
        print (button_flag23,flag23)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but23 = Button(app, text="23", image=but_image)
        but23.grid(row=3, column=1, sticky=W)
        but23.image = but_image
        button_flag23 = True
        print (button_flag23)
    return

def click24():
    global button_flag24,but24,flag24,clicks
    if button_flag24:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\j_clover.gif")
        but24 = Button(app ,text="24", image = my_image,command = img24)
        but24.grid(row=3, column=2, sticky=W)
        but24.image = my_image
        #button_flag24 = False
        flag24 = 1
        print (button_flag24,flag24)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but24 = Button(app, text="24", image=but_image)
        but24.grid(row=3, column=2, sticky=W)
        but24.image = but_image
        button_flag24 = True
        print (button_flag24)
    return

def click25():
    global button_flag25,but25,flag25,clicks

    if button_flag25:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\joker.gif")
        but25 = Button(app ,text="25", image = my_image,command = img25)
        but25.grid(row=3, column=3, sticky=W)
        but25.image = my_image
        #button_flag25 = False
        flag25 = 1
        print (button_flag25,flag25)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but25 = Button(app, text="25", image=but_image)
        but25.grid(row=3, column=3, sticky=W)
        but25.image = but_image
        button_flag25 = True
        print (button_flag25)
    return
def click26():
    global button_flag26,but26,flag26,clicks

    if button_flag26:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\k_spade.gif")
        but26 = Button(app ,text="26", image = my_image,command = img26)
        but26.grid(row=3, column=4, sticky=W)
        but26.image = my_image
        #button_flag26 = False
        flag26 = 1
        print (button_flag26,flag26)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but26 = Button(app, text="26", image=but_image)
        but26.grid(row=3, column=4, sticky=W)
        but26.image = but_image
        button_flag26 = True
        print (button_flag26)
    return
def click27():
    global button_flag27,but27,flag27,clicks

    if button_flag27:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\q_spade.gif")
        but27 = Button(app ,text="27", image = my_image,command = img27)
        but27.grid(row=3, column=5, sticky=W)
        but27.image = my_image
        #button_flag27 = False
        flag27 = 1
        print (button_flag27,flag27)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but27 = Button(app, text="27", image=but_image)
        but27.grid(row=3, column=5, sticky=W)
        but27.image = but_image
        button_flag27 = True
        print (button_flag27)
    return
def click28():
    global button_flag28,but28,flag28,clicks

    if button_flag28:
        my_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\th.gif")
        but28 = Button(app ,text="28", image = my_image,command = img28)
        but28.grid(row=3, column=6, sticky=W)
        but28.image = my_image
        #button_flag28 = False
        flag28 = 1
        print (button_flag28,flag28)
        clicks = clicks + 1
        print "Open click(s)", clicks

    else:
        but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
        but28 = Button(app, text="28", image=but_image)
        but28.grid(row=3, column=6, sticky=W)
        but28.image = but_image
        button_flag28 = True
        print (button_flag28)
    return
def match():
    global clicks
    global flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8,flag9,flag10,flag11,flag12,flag13,flag14,flag15,flag16,flag17,flag18,flag19,flag20,flag21,flag22,flag23,flag24,flag25,flag26,flag27,flag28
    global but1 , but2,but3,but4,but5,but6,but7,but8,but9,but10,but11,but12,but13,but14,but15,but16,but17,but18,but19,but20,but21,but22,but23,but24,but25,but26,but27,but28
    my_image1_15 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\2_clover.gif")
    my_image2_16 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\3_dice.gif")
    my_image_3_17 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\4_spade.gif")
    my_image_4_18 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\5_hearts.gif")
    my_image_5_19 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\6_hearts.gif")
    my_image_6_20 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\7_clover.gif")
    my_image7_21 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\8_spade.gif")
    my_image8_22 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\10_dice.gif")
    my_image_9_23 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\a_heart.gif")
    my_image_10_24 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\j_clover.gif")
    my_image_11_25 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\joker.gif")
    my_image_12_26 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\k_spade.gif")
    my_image_13_27 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\q_spade.gif")
    my_image_14_28 = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\Cards\\th.gif")
    if int(clicks) == 2:
        if flag1 == 1 and flag15 == 1:
            but1 = Button(app, text="1", image=my_image1_15)
            but1.grid(row=0, column=0, sticky=W)
            but1.image = my_image1_15
            but15 = Button(app, text="15", image=my_image1_15)
            but15.grid(row=2, column=0, sticky=W)
            but15.image = my_image1_15
            tkMessageBox.showinfo("Memory Game!!","Cards Match")
            sleep(1)
            but1 = Button(app, text="1", image=my_image1_15, state=DISABLED)
            but1.grid(row=0, column=0, sticky=W)
            but1.image = my_image1_15
            but15 = Button(app, text="15", image=my_image1_15, state=DISABLED)
            but15.grid(row=2, column=0, sticky=W)
            but15.image = my_image1_15
            print "Yes"
            flag1 = 0
            flag15 = 0

        elif flag2 == 1 and flag16 == 1:
            but2 = Button(app, text="2", image=my_image2_16)
            but2.grid(row=0, column=1, sticky=W)
            but2.image = my_image2_16
            but16 = Button(app, text="16", image=my_image2_16)
            but16.grid(row=2, column=1, sticky=W)
            but16.image = my_image2_16
            tkMessageBox.showinfo("Memory Game!!", "Cards Match")
            sleep(1)
            but2 = Button(app, text="2", image=my_image2_16, state=DISABLED)
            but2.grid(row=0, column=1, sticky=W)
            but2.image = my_image2_16
            but16 = Button(app, text="16", image=my_image2_16, state=DISABLED)
            but16.grid(row=2, column=1, sticky=W)
            but16.image = my_image2_16
            print "Yes"
            flag2 = flag16 = 0
        elif flag3 == 1 and flag17 == 1:
            but3 = Button(app, text="3", image=my_image_3_17)
            but3.grid(row=0, column=2, sticky=W)
            but3.image = my_image_3_17
            but17 = Button(app, text="17", image=my_image_3_17)
            but17.grid(row=2, column=2, sticky=W)
            but17.image = my_image_3_17
            tkMessageBox.showinfo("Memory Game!!", "Cards Match")
            sleep(1)
            but3 = Button(app, text="3", image=my_image_3_17, state=DISABLED)
            but3.grid(row=0, column=2, sticky=W)
            but3.image = my_image_3_17
            but17 = Button(app, text="17", image=my_image_3_17, state=DISABLED)
            but17.grid(row=2, column=2, sticky=W)
            but17.image = my_image_3_17
            print "Yes"
            flag3 = flag17 = 0

        elif flag4 == 1 and flag18 == 1:
            but4 = Button(app, text="4", image=my_image_4_18)
            but4.grid(row=0, column=3, sticky=W)
            but4.image = my_image_4_18
            but18 = Button(app, text="18", image=my_image_4_18)
            but18.grid(row=2, column=3, sticky=W)
            but18.image = my_image_4_18
            tkMessageBox.showinfo("Memory Game!!", "Cards Match")
            sleep(1)
            but4 = Button(app, text="4", image=my_image_4_18, state=DISABLED)
            but4.grid(row=0, column=3, sticky=W)
            but4.image = my_image_4_18
            but18 = Button(app, text="18", image=my_image_4_18, state=DISABLED)
            but18.grid(row=2, column=3, sticky=W)
            but18.image = my_image_4_18
            print "Yes"
            flag4 = flag18 = 0
        elif flag5 == 1 and flag19 == 1:
            but5 = Button(app, text="5", image=my_image_5_19)
            but5.grid(row=0, column=4, sticky=W)
            but5.image = my_image_5_19
            but19 = Button(app, text="19", image = my_image_5_19)
            but19.grid(row=2, column=4, sticky=W)
            but19.image = my_image_5_19
            tkMessageBox.showinfo("Memory Game!!", "Cards Match")
            sleep(1)
            but5 = Button(app, text="5", image=my_image_5_19, state=DISABLED)
            but5.grid(row=0, column=4, sticky=W)
            but5.image = my_image_5_19
            but19 = Button(app, text="19", image=my_image_5_19, state=DISABLED)
            but19.grid(row=2, column=4, sticky=W)
            but19.image = my_image_5_19
            print "Yes"
            flag5 = flag19 = 0
        elif flag6 == 1 and flag20 == 1:
            but6 = Button(app, text="6", image=my_image_6_20)
            but6.grid(row=0, column=5, sticky=W)
            but6.image = my_image_6_20
            but20 = Button(app, text="20", image=my_image_6_20)
            but20.grid(row=2, column=5, sticky=W)
            but20.image = my_image_6_20
            tkMessageBox.showinfo("Memory Game!!", "Cards Match")
            sleep(1)
            print "Yes"
            but6 = Button(app, text="6", image=my_image_6_20, state=DISABLED)
            but6.grid(row=0, column=5, sticky=W)
            but6.image = my_image_6_20
            but20 = Button(app, text="20", image=my_image_6_20, state=DISABLED)
            but20.grid(row=2, column=5, sticky=W)
            but20.image = my_image_6_20
            flag6 = flag20 = 0
        elif flag7 == 1 and flag21 == 1:
            but7 = Button(app, text="7", image=my_image7_21)
            but7.grid(row=0, column=6, sticky=W)
            but7.image = my_image7_21
            but21 = Button(app, text="21", image=my_image7_21)
            but21.grid(row=2, column=6, sticky=W)
            but21.image = my_image7_21
            tkMessageBox.showinfo("Memory Game!!", "Cards Match")
            sleep(1)
            but7 = Button(app, text="7", image=my_image7_21, state=DISABLED)
            but7.grid(row=0, column=6, sticky=W)
            but7.image = my_image7_21
            but21 = Button(app, text="21", image=my_image7_21, state=DISABLED)
            but21.grid(row=2, column=6, sticky=W)
            but21.image = my_image7_21
            print "Yes"
            flag7 = flag21 = 0
        elif flag8 == 1 and flag22 == 1:
            but8 = Button(app, text="8", image=my_image8_22)
            but8.grid(row=1, column=0, sticky=W)
            but8.image = my_image8_22
            but22 = Button(app, text="22", image=my_image8_22)
            but22.grid(row=3, column=0, sticky=W)
            but22.image = my_image8_22
            tkMessageBox.showinfo("Memory Game!!", "Cards Match")
            sleep(1)
            but8 = Button(app, text="8", image=my_image8_22, state=DISABLED)
            but8.grid(row=1, column=0, sticky=W)
            but8.image = my_image8_22
            but22 = Button(app, text="22", image=my_image8_22, state=DISABLED)
            but22.grid(row=3, column=0, sticky=W)
            but22.image = my_image8_22
            print "Yes"
            flag8 = flag22 = 0
        elif flag9 == 1 and flag23 == 1:
            but9 = Button(app, text="9", image=my_image_9_23)
            but9.grid(row=1, column=1, sticky=W)
            but9.image = my_image_9_23
            but23 = Button(app, text="23", image=my_image_9_23)
            but23.grid(row=3, column=1, sticky=W)
            but23.image = my_image_9_23
            tkMessageBox.showinfo("Memory Game!!", "Cards Match")
            sleep(1)
            but9 = Button(app, text="9", image=my_image_9_23, state=DISABLED)
            but9.grid(row=1, column=1, sticky=W)
            but9.image = my_image_9_23
            but23 = Button(app, text="23", image=my_image_9_23, state=DISABLED)
            but23.grid(row=3, column=1, sticky=W)
            but23.image = my_image_9_23
            print "Yes"
            flag9 = flag23 = 0
        elif flag10 == 1 and flag24 == 1:
            but10 = Button(app, text="10", image=my_image_10_24)
            but10.grid(row=1, column=2, sticky=W)
            but10.image = my_image_10_24
            but24 = Button(app, text="24", image=my_image_10_24)
            but24.grid(row=3, column=2, sticky=W)
            but24.image = my_image_10_24
            tkMessageBox.showinfo("Memory Game!!", "Cards Match")
            sleep(1)
            but10 = Button(app, text="10", image=my_image_10_24, state=DISABLED)
            but10.grid(row=1, column=2, sticky=W)
            but10.image = my_image_10_24
            but24 = Button(app, text="24", image=my_image_10_24, state=DISABLED)
            but24.grid(row=3, column=2, sticky=W)
            but24.image = my_image_10_24
            print "Yes"
            flag10 = flag24 = 0
        elif flag11 == 1 and flag25 == 1:
            but11 = Button(app, text="11", image=my_image_11_25)
            but11.grid(row=1, column=3, sticky=W)
            but11.image = my_image_11_25
            but25 = Button(app, text="25", image=my_image_11_25)
            but25.grid(row=3, column=3, sticky=W)
            but25.image = my_image_11_25
            tkMessageBox.showinfo("Memory Game!!", "Cards Match")
            sleep(1)
            but11 = Button(app, text="11", image=my_image_11_25, state=DISABLED)
            but11.grid(row=1, column=3, sticky=W)
            but11.image = my_image_11_25
            but25 = Button(app, text="25", image=my_image_11_25, state=DISABLED)
            but25.grid(row=3, column=3, sticky=W)
            but25.image = my_image_11_25
            print "Yes"
            flag11 = flag25 = 0
        elif flag12 == 1 and flag26 == 1:
            but12 = Button(app, text="12", image=my_image_12_26)
            but12.grid(row=1, column=4, sticky=W)
            but12.image = my_image_12_26
            but26 = Button(app, text="26", image=my_image_12_26)
            but26.grid(row=3, column=4, sticky=W)
            but26.image = my_image_12_26
            tkMessageBox.showinfo("Memory Game!!", "Cards Match")
            sleep(1)
            but12 = Button(app, text="12", image=my_image_12_26, state=DISABLED)
            but12.grid(row=1, column=4, sticky=W)
            but12.image = my_image_12_26
            but26 = Button(app, text="26", image=my_image_12_26, state=DISABLED)
            but26.grid(row=3, column=4, sticky=W)
            but26.image = my_image_12_26
            print "Yes"
            flag12 = flag26 = 0
        elif flag13 == 1 and flag27 == 1:
            but13 = Button(app, text="13", image=my_image_13_27)
            but13.grid(row=1, column=5, sticky=W)
            but13.image = my_image_13_27
            but27 = Button(app, text="27", image=my_image_13_27)
            but27.grid(row=3, column=5, sticky=W)
            but27.image = my_image_13_27
            tkMessageBox.showinfo("Memory Game!!", "Cards Match")
            sleep(1)
            but13 = Button(app, text="13", image=my_image_13_27, state=DISABLED)
            but13.grid(row=1, column=5, sticky=W)
            but13.image = my_image_13_27
            but27 = Button(app, text="27", image=my_image_13_27, state=DISABLED)
            but27.grid(row=3, column=5, sticky=W)
            but27.image = my_image_13_27
            print "Yes"
            flag13 = flag27 = 0
        elif flag14 == 1 and flag28 == 1:
            but14 = Button(app, text="14", image=my_image_14_28)
            but14.grid(row=1, column=6, sticky=W)
            but14.image = my_image_14_28
            but28 = Button(app, text="28", image=my_image_14_28)
            but28.grid(row=3, column=6, sticky=W)
            but28.image = my_image_14_28
            tkMessageBox.showinfo("Memory Game!!", "Cards Match")
            sleep(1)
            but14 = Button(app, text="14", image=my_image_14_28, state=DISABLED)
            but14.grid(row=1, column=6, sticky=W)
            but14.image = my_image_14_28
            but28 = Button(app, text="28", image=my_image_14_28, state=DISABLED)
            but28.grid(row=3, column=6, sticky=W)
            but28.image = my_image_14_28
            print "Yes"
            flag14 = flag28 = 0
        elif flag1 == 1:
            sleep(1)
            button_flag1 = True
            but1 = Button(app, text="1", image=but_image, command=click1)
            but1.grid(row=0, column=0, sticky=W)
            but1.image = but_image
            if  flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image = but_image , command = click2)
                but2.grid(row = 0, column = 1, sticky = W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image = but_image , command = click3)
                but3.grid(row = 0, column = 2, sticky = W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image = but_image , command = click4)
                but4.grid(row = 0, column = 3, sticky = W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image = but_image , command = click5)
                but5.grid(row = 0, column = 4, sticky = W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image = but_image , command = click6)
                but6.grid(row = 0, column = 5, sticky = W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image = but_image , command = click7)
                but7.grid(row = 0, column = 6, sticky = W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image = but_image , command = click8)
                but8.grid(row = 1, column = 0, sticky = W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image = but_image , command = click9)
                but9.grid(row = 1, column = 1, sticky = W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image = but_image , command = click10)
                but10.grid(row = 1, column = 2, sticky = W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image = but_image , command = click11)
                but11.grid(row = 1, column = 3, sticky = W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image = but_image , command = click12)
                but12.grid(row = 1, column = 4, sticky = W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image = but_image , command = click13)
                but13.grid(row = 1, column = 5, sticky = W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image = but_image , command = click14)
                but14.grid(row = 1, column = 6, sticky = W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image = but_image , command = click16)
                but16.grid(row = 2, column = 1, sticky = W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image = but_image , command = click17)
                but17.grid(row = 2, column = 2, sticky = W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image = but_image , command = click18)
                but18.grid(row = 2, column = 3, sticky = W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image = but_image , command = click19)
                but19.grid(row = 2, column = 4, sticky = W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image = but_image , command = click20)
                but20.grid(row = 2, column = 5, sticky = W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image = but_image , command = click21)
                but21.grid(row = 2, column = 6, sticky = W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image = but_image , command = click22)
                but22.grid(row = 3, column = 0, sticky = W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image = but_image , command = click23)
                but23.grid(row = 3, column = 1, sticky = W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image = but_image , command = click24)
                but24.grid(row = 3, column = 2, sticky = W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image = but_image , command = click25)
                but25.grid(row = 3, column = 3, sticky = W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image = but_image , command = click26)
                but26.grid(row = 3, column = 4, sticky = W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image = but_image , command = click27)
                but27.grid(row = 3, column = 5, sticky = W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                sleep(1)
                but28 = Button(app, text="28", image = but_image , command = click28)
                but28.grid(row = 3, column = 6, sticky = W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag1 = 0
        elif flag2 == 1:
            sleep(1)
            button_flag2 = True
            but2 = Button(app, text="2", image=but_image, command=click2)
            but2.grid(row=0, column=1, sticky=W)
            but2.image = but_image

            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag2 = 0
        elif flag3 == 1:
            sleep(1)
            button_flag3 = True
            but3 = Button(app, text="3", image=but_image, command=click3)
            but3.grid(row=0, column=2, sticky=W)
            but3.image = but_image
            if flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=1, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_fvlag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag3 = 0
        elif flag4 == 1:
            sleep(1)
            button_flag4 = True
            but4 = Button(app, text="4", image=but_image, command=click4)
            but4.grid(row=0, column=3, sticky=W)
            but4.image = but_image
            if flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=1, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag4 = 0
        elif flag5 == 1:
            sleep(1)
            button_flag5 = True
            but5 = Button(app, text="5", image=but_image, command=click5)
            but5.grid(row=0, column=4, sticky=W)
            but5.image = but_image
            if flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=1, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag5 = 0
        elif flag6 == 1:
            sleep(1)
            button_flag6 = True
            but6 = Button(app, text="6", image=but_image, command=click6)
            but6.grid(row=0, column=5, sticky=W)
            but6.image = but_image
            if flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=1, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag6 = 0
        elif flag7 == 1:
            sleep(1)
            button_flag7 = True
            but7 = Button(app, text="7", image=but_image, command=click7)
            but7.grid(row=0, column=6, sticky=W)
            but7.image = but_image
            if flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=1, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag7 = 0

        elif flag8 == 1:
            sleep(1)
            button_flag8 = True
            but8 = Button(app, text="2", image=but_image, command=click8)
            but8.grid(row=1, column=0, sticky=W)
            but8.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag8 = 0
        elif flag9 == 1:
            sleep(1)
            button_flag9 = True
            but9 = Button(app, text="9", image=but_image, command=click9)
            but9.grid(row=1, column=1, sticky=W)
            but9.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag9 = 0
        elif flag10 == 1:
            sleep(1)
            button_flag10 = True
            but10 = Button(app, text="10", image=but_image, command=click10)
            but10.grid(row=1, column=2, sticky=W)
            but10.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag10 = 0

        elif flag11 == 1:
            sleep(1)
            button_flag11 = True
            but11 = Button(app, text="10", image=but_image, command=click11)
            but11.grid(row=1, column=3, sticky=W)
            but11.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag11 = 0
        elif flag12 == 1:
            sleep(1)
            button_flag12 = True
            but12 = Button(app, text="12", image=but_image, command=click12)
            but12.grid(row=1, column=4, sticky=W)
            but12.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag12 = 0
        elif flag13 == 1:
            sleep(1)
            button_flag13 = True
            but13 = Button(app, text="13", image=but_image, command=click13)
            but13.grid(row=1, column=5, sticky=W)
            but13.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag13 = 0
        elif flag14 == 1:
            sleep(1)
            button_flag14 = True
            but14 = Button(app, text="14", image=but_image, command=click14)
            but14.grid(row=1, column=6, sticky=W)
            but14.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            flag14 = 0
        elif flag15 == 1:
            sleep(1)
            button_flag15 = True
            but15 = Button(app, text="15", image=but_image, command=click15)
            but15.grid(row=2, column=0, sticky=W)
            but15.image = but_image
            if flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag15 = 0

        elif flag16 == 1:
            sleep(1)
            button_flag16 = True
            but16 = Button(app, text="16", image=but_image, command=click16)
            but16.grid(row=2, column=1, sticky=W)
            but16.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag16 = 0

        elif flag17 == 1:
            sleep(1)
            button_flag17 = True
            but17 = Button(app, text="17", image=but_image, command=click17)
            but17.grid(row=2, column=2, sticky=W)
            but17.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag17 = 0
        elif flag18 == 1:
            sleep(1)
            button_flag18 = True
            but18 = Button(app, text="18", image=but_image, command=click18)
            but18.grid(row=2, column=3, sticky=W)
            but18.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag18 = 0
        elif flag19 == 1:
            sleep(1)
            button_flag19 = True
            but19 = Button(app, text="19", image=but_image, command=click19)
            but19.grid(row=2, column=4, sticky=W)
            but19.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag19 = 0
        elif flag20 == 1:
            sleep(1)
            button_flag20 = True
            but20 = Button(app, text="20", image=but_image, command=click20)
            but20.grid(row=2, column=5, sticky=W)
            but20.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag20 = 0
        elif flag21 == 1:
            sleep(1)
            button_flag21 = True
            but21 = Button(app, text="21", image=but_image, command=click21)
            but21.grid(row=2, column=6, sticky=W)
            but21.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag21 = 0
        elif flag22 == 1:
            sleep(1)
            button_flag22 = True
            but22 = Button(app, text="22", image=but_image, command=click22)
            but22.grid(row=3, column=0, sticky=W)
            but22.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag22 = 0
        elif flag23 == 1:
            sleep(1)
            button_flag23 = True
            but23 = Button(app, text="23", image=but_image, command=click23)
            but23.grid(row=3, column=1, sticky=W)
            but23.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag23 = 0
        elif flag24 == 1:
            sleep(1)
            button_flag24 = True
            but24 = Button(app, text="24", image=but_image, command=click24)
            but24.grid(row=3, column=2, sticky=W)
            but24.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag24 = 0
        elif flag25 == 1:
            sleep(1)
            button_flag25 = True
            but25 = Button(app, text="25", image=but_image, command=click25)
            but25.grid(row=3, column=3, sticky=W)
            but25.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag25 = 0
        elif flag26 == 1:
            sleep(1)
            button_flag26 = True
            but26 = Button(app, text="26", image=but_image, command=click26)
            but26.grid(row=3, column=4, sticky=W)
            but26.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag26 = 0
        elif flag27 == 1:
            sleep(1)
            button_flag27 = True
            but27 = Button(app, text="27", image=but_image, command=click27)
            but27.grid(row=3, column=5, sticky=W)
            but27.image = but_image
            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0
            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
            elif flag14 == 1:
                sleep(1)
                but14 = Button(app, text="14", image=but_image, command=click14)
                but14.grid(row=1, column=6, sticky=W)
                but14.image = but_image
                button_flag14 = True
                flag14 = 0
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
            elif flag28 == 1:
                sleep(1)
                but28 = Button(app, text="28", image=but_image, command=click28)
                but28.grid(row=3, column=6, sticky=W)
                but28.image = but_image
                button_flag28 = True
                flag28 = 0
            flag27 = 0
        elif flag28 == 1:
            sleep(1)
            button_flag28 = True
            but28 = Button(app, text="28", image=but_image, command=click28)
            but28.grid(row=3, column=6, sticky=W)
            but28.image = but_image

            if flag1 == 1:
                sleep(1)
                but1 = Button(app, text="1", image=but_image, command=click1)
                but1.grid(row=0, column=0, sticky=W)
                but1.image = but_image
                button_flag1 = True
                flag1 = 0

            elif flag2 == 1:
                sleep(1)
                but2 = Button(app, text="2", image=but_image, command=click2)
                but2.grid(row=0, column=2, sticky=W)
                but2.image = but_image
                button_flag2 = True
                flag2 = 0
                sleep(1)
            elif flag3 == 1:
                sleep(1)
                but3 = Button(app, text="3", image=but_image, command=click3)
                but3.grid(row=0, column=2, sticky=W)
                but3.image = but_image
                button_flag3 = True
                flag3 = 0
                sleep(1)
            elif flag4 == 1:
                sleep(1)
                but4 = Button(app, text="4", image=but_image, command=click4)
                but4.grid(row=0, column=3, sticky=W)
                but4.image = but_image
                button_flag4 = True
                flag4 = 0
                sleep(1)
            elif flag5 == 1:
                sleep(1)
                but5 = Button(app, text="5", image=but_image, command=click5)
                but5.grid(row=0, column=4, sticky=W)
                but5.image = but_image
                button_flag5 = True
                flag5 = 0
                sleep(1)
            elif flag6 == 1:
                sleep(1)
                but6 = Button(app, text="6", image=but_image, command=click6)
                but6.grid(row=0, column=5, sticky=W)
                but6.image = but_image
                button_flag6 = True
                flag6 = 0
                sleep(1)
            elif flag7 == 1:
                sleep(1)
                but7 = Button(app, text="7", image=but_image, command=click7)
                but7.grid(row=0, column=6, sticky=W)
                but7.image = but_image
                button_flag7 = True
                flag7 = 0
                sleep(1)
            elif flag8 == 1:
                sleep(1)
                but8 = Button(app, text="8", image=but_image, command=click8)
                but8.grid(row=1, column=0, sticky=W)
                but8.image = but_image
                button_flag8 = True
                flag8 = 0
                sleep(1)
            elif flag9 == 1:
                sleep(1)
                but9 = Button(app, text="9", image=but_image, command=click9)
                but9.grid(row=1, column=1, sticky=W)
                but9.image = but_image
                button_flag9 = True
                flag9 = 0
                sleep(1)
            elif flag10 == 1:
                sleep(1)
                but10 = Button(app, text="10", image=but_image, command=click10)
                but10.grid(row=1, column=2, sticky=W)
                but10.image = but_image
                button_flag10 = True
                flag10 = 0
                sleep(1)
            elif flag11 == 1:
                sleep(1)
                but11 = Button(app, text="11", image=but_image, command=click11)
                but11.grid(row=1, column=3, sticky=W)
                but11.image = but_image
                button_flag11 = True
                flag11 = 0
                sleep(1)
            elif flag12 == 1:
                sleep(1)
                but12 = Button(app, text="12", image=but_image, command=click12)
                but12.grid(row=1, column=4, sticky=W)
                but12.image = but_image
                button_flag12 = True
                flag12 = 0
                sleep(1)
            elif flag13 == 1:
                sleep(1)
                but13 = Button(app, text="13", image=but_image, command=click13)
                but13.grid(row=1, column=5, sticky=W)
                but13.image = but_image
                button_flag13 = True
                flag13 = 0
                sleep(1)
            elif flag15 == 1:
                sleep(1)
                but15 = Button(app, text="15", image=but_image, command=click15)
                but15.grid(row=2, column=0, sticky=W)
                but15.image = but_image
                button_flag15 = True
                flag15 = 0
                sleep(1)
            elif flag16 == 1:
                sleep(1)
                but16 = Button(app, text="16", image=but_image, command=click16)
                but16.grid(row=2, column=1, sticky=W)
                but16.image = but_image
                button_flag16 = True
                flag16 = 0
                sleep(1)
            elif flag17 == 1:
                sleep(1)
                but17 = Button(app, text="17", image=but_image, command=click17)
                but17.grid(row=2, column=2, sticky=W)
                but17.image = but_image
                button_flag17 = True
                flag17 = 0
                sleep(1)
            elif flag18 == 1:
                sleep(1)
                but18 = Button(app, text="18", image=but_image, command=click18)
                but18.grid(row=2, column=3, sticky=W)
                but18.image = but_image
                button_flag18 = True
                flag18 = 0
                sleep(1)
            elif flag19 == 1:
                sleep(1)
                but19 = Button(app, text="19", image=but_image, command=click19)
                but19.grid(row=2, column=4, sticky=W)
                but19.image = but_image
                button_flag19 = True
                flag19 = 0
                sleep(1)
            elif flag20 == 1:
                sleep(1)
                but20 = Button(app, text="20", image=but_image, command=click20)
                but20.grid(row=2, column=5, sticky=W)
                but20.image = but_image
                button_flag20 = True
                flag20 = 0
                sleep(1)
            elif flag21 == 1:
                sleep(1)
                but21 = Button(app, text="21", image=but_image, command=click21)
                but21.grid(row=2, column=6, sticky=W)
                but21.image = but_image
                button_flag21 = True
                flag21 = 0
                sleep(1)
            elif flag22 == 1:
                sleep(1)
                but22 = Button(app, text="22", image=but_image, command=click22)
                but22.grid(row=3, column=0, sticky=W)
                but22.image = but_image
                button_flag22 = True
                flag22 = 0
                sleep(1)
            elif flag23 == 1:
                sleep(1)
                but23 = Button(app, text="23", image=but_image, command=click23)
                but23.grid(row=3, column=1, sticky=W)
                but23.image = but_image
                button_flag23 = True
                flag23 = 0
                sleep(1)
            elif flag24 == 1:
                sleep(1)
                but24 = Button(app, text="24", image=but_image, command=click24)
                but24.grid(row=3, column=2, sticky=W)
                but24.image = but_image
                button_flag24 = True
                flag24 = 0
                sleep(1)
            elif flag25 == 1:
                sleep(1)
                but25 = Button(app, text="25", image=but_image, command=click25)
                but25.grid(row=3, column=3, sticky=W)
                but25.image = but_image
                button_flag25 = True
                flag25 = 0
                sleep(1)
            elif flag26 == 1:
                sleep(1)
                but26 = Button(app, text="26", image=but_image, command=click26)
                but26.grid(row=3, column=4, sticky=W)
                but26.image = but_image
                button_flag26 = True
                flag26 = 0
                sleep(1)
            elif flag27 == 1:
                sleep(1)
                but27 = Button(app, text="27", image=but_image, command=click27)
                but27.grid(row=3, column=5, sticky=W)
                but27.image = but_image
                button_flag27 = True
                flag27 = 0
                sleep(1)
            flag28 = 0
    else:
        tkMessageBox.showinfo("Memory Game!!" , "Invalid selection!!. Please select only two cards at a time and submit!!")
        root.quit()
    clicks = 0
    return

but_image = PhotoImage(file="C:\\Users\\munarayanan\\Desktop\\Learn_python\\_card_front.gif")
but1 = Button(app, text="1", image=but_image, command=click1)
but1.grid(row=0, column=0, sticky=W)
but1.image = but_image
but2 = Button(app, text="2", image=but_image, command=click2)
but2.grid(row=0, column=1, sticky=W)
but2.image = but_image
but3 = Button(app, text="3", image=but_image, command=click3)
but3.grid(row=0, column=2, sticky=W)
but3.image = but_image
but4 = Button(app, text="4", image=but_image, command=click4)
but4.grid(row=0, column=3, sticky=W)
but4.image = but_image
but5 = Button(app, text="5", image=but_image, command=click5)
but5.grid(row=0, column=4, sticky=W)
but5.image = but_image
but6 = Button(app, text="6", image=but_image, command=click6)
but6.grid(row=0, column=5, sticky=W)
but6.image = but_image
but7 = Button(app, text="7", image=but_image, command=click7)
but7.grid(row=0, column=6, sticky=W)
but7.image = but_image
but8 = Button(app, text="8", image=but_image, command=click8)
but8.grid(row=1, column=0, sticky=W)
but8.image = but_image
but9 = Button(app, text="9", image=but_image, command=click9)
but9.grid(row=1, column=1, sticky=W)
but9.image = but_image
but10 = Button(app, text="10", image=but_image, command=click10)
but10.grid(row=1, column=2, sticky=W)
but10.image = but_image
but11= Button(app, text="11", image=but_image, command=click11)
but11.grid(row=1, column=3, sticky=W)
but11.image = but_image
but12 = Button(app, text="12", image=but_image, command=click12)
but12.grid(row=1, column=4, sticky=W)
but12.image = but_image
but13 = Button(app, text="13", image=but_image, command=click13)
but13.grid(row=1, column=5, sticky=W)
but13.image = but_image
but14 = Button(app, text="14", image=but_image, command=click14)
but14.grid(row=1, column=6, sticky=W)
but14.image = but_image
but15 = Button(app, text="15", image=but_image, command=click15)
but15.grid(row=2, column=0, sticky=W)
but15.image = but_image
but16 = Button(app, text="16", image=but_image, command=click16)
but16.grid(row=2, column=1, sticky=W)
but16.image = but_image
but17 = Button(app, text="17", image=but_image, command=click17)
but17.grid(row=2, column=2, sticky=W)
but17.image = but_image
but18 = Button(app, text="18", image=but_image, command=click18)
but18.grid(row=2, column=3, sticky=W)
but18.image = but_image
but19 = Button(app, text="19", image=but_image, command=click19)
but19.grid(row=2, column=4, sticky=W)
but19.image = but_image
but20 = Button(app, text="20", image=but_image, command=click20)
but20.grid(row=2, column=5, sticky=W)
but20.image = but_image
but21 = Button(app, text="21", image=but_image, command=click21)
but21.grid(row=2, column=6, sticky=W)
but21.image = but_image
but22 = Button(app, text="22", image=but_image, command=click22)
but22.grid(row=3, column=0, sticky=W)
but22.image = but_image
but23 = Button(app, text="23", image=but_image, command=click23)
but23.grid(row=3, column=1, sticky=W)
but23.image = but_image
but24 = Button(app, text="24", image=but_image, command=click24)
but24.grid(row=3, column=2, sticky=W)
but24.image = but_image
but25= Button(app, text="25", image=but_image, command=click25)
but25.grid(row=3, column=3, sticky=W)
but25.image = but_image
but26 = Button(app, text="26", image=but_image, command=click26)
but26.grid(row=3, column=4, sticky=W)
but26.image = but_image
but27 = Button(app, text="27", image=but_image, command=click27)
but27.grid(row=3, column=5, sticky=W)
but27.image = but_image
but28 = Button(app, text="28", image=but_image, command=click28)
but28.grid(row=3, column=6, sticky=W)
but28.image = but_image
match_button = Button(app , text = "Submit" , command = match)
match_button.grid(row = 4 , column = 0 , sticky = W)
# create a frame and pack it
root.mainloop()