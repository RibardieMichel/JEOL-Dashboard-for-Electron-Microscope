# -*- coding: utf-8 -*-

#Created on Thu Dec  3 11:57:27 2020

#@author: SAV-MR

import tkinter 
from tkinter import *
from tkinter import WORD
import datetime
from PyJEM import TEM3
BB=TEM3.Def3()
stage=TEM3.Stage3()
HT=TEM3.HT3()
eos=TEM3.EOS3()
feg=TEM3.FEG3()
gun=TEM3.GUN3()
lens=TEM3.Lens3()
root = Tk("Main")
# GEOMETRY= WIDTH+HEIGHT+POSX+POSY
#root.geometry("365x330+600+300")
root.geometry("+1100+100")

canv = tkinter.Canvas( bg="black", height=0, width=400)
canv.pack()


lab3 = Label(root) # time
lab3.pack()

lab = Label(root)
lab.pack()
lab.configure(background='black', foreground='white')

lab1 = Label(root) # ht et mag
lab1.pack()

lab16 = Label(root) # ht et mag
lab16.pack()

lab9 = Label(root) # probe mode, spot et alpha
lab9.pack()


#radioems=Radiobutton(root)
#radioems=Radiobutton(value=0)
#radioems.pack()
#side="bottom"
lab12 = Label(root) # emission
lab12.pack()

lab17=Label(root) #Defocus
lab17.pack()

lab5 = Label(root) #ligne
lab5.pack()
lab15 = Label(root) #STAGE
lab15.pack()

lab6=Label(root) #X ET Y
lab6.pack()
lab7=Label(root) #Z
lab7.pack()
lab8=Label(root) #TX ET TY
lab8.pack()



pos=stage.GetPos()
X=pos[0]
X=round(X/1000,2)
Y=pos[1]
Y=round(Y/1000,2)
Z=pos[2]
Z=round(Z/1000,2)
TX=pos[3]
TX=round(TX,2)
TY=pos[4]
TY=round(TY,2)


def SetTiltX(TX):
    TX=0
    stage.SetTiltXAngle(TX)
    

w1 = Scale(root, from_=-10, to=10,
           length=300,
           tickinterval=1,
           label='TX',
           resolution=2,
           orient=HORIZONTAL,
           command=SetTiltX(TX))
w1.set(TX)
w1.configure(background='black', foreground='green')
#w1.pack()


lab4=Label(root) #ligne
lab4.pack()

lab14 = Label(root) #clA1 LABEL
lab14.pack()

lab13 = Label(root) #clA1 VALUES
lab13.pack()

lab23 = Label(root) #clA2 LABEL
lab23.pack()

lab22 = Label(root) #clA2 VALUES
lab22.pack()

lab11 = Label(root) #clstig LABEL
lab11.pack()

lab2 = Label(root) # clstig Values
lab2.pack()

def stagen():
    x=0
    y=0
    tx=0
    ty=0
    Z=0
    stage.SetX(x)
    stage.SetY(y)
    stage.SetTiltXAngle(tx)
    stage.SetTiltXAngle(ty)
    stage.SetZ(Z)
    
b1 = Button(text = "Neutral TX", command = stagen)
b1.configure(background='black', foreground='lightgreen')
#b1.place(x = 100,y = 400)
#b1.pack()
#Radiobutton1=Radiobutton(root)
#Radiobutton1.pack()

lab10=Label(root) #READY V1
lab10.pack(side="bottom")




def clock():

    OLf=lens.GetOLf()
    OLc=lens.GetOLc()
    OL0c=47446
    OL0f=32784
    f=(OLf-OL0f)*1.4
    # pas du coarse =32*pas du fine
    c=(OLc-OL0c)*44.8
    
    Defocus="Defocus: "+str(f+c)
    #print(Defocus)
    foc=round((f+c),2)
    lab17.config(text=("Defocus:",(foc),"nm"))
    lab17.configure(background='black', foreground='lightyellow')
    
    
    ems=gun.GetEmissionCurrentValue()
    #ems=13.4456
    ems=str(ems)
    ems=ems[0:5]
    ems=float(ems)
    ems1=int(ems)
    #ems1=10
    onoff= tkinter.BooleanVar()
    if(ems>=3):
        emission="ON"
        onoff.set(True)
        #print("emission=",onoff)
        #radioems.configure(text="Emission", variable = onoff,value=True)
        #,value=True
    elif(ems<=1): 
        emission="OFF"
        onoff.set(False)
        #print("emission=",onoff)
        #radioems.configure(text="Emission", variable = onoff,value=False)
        #,value=False
    BV=feg.GetBeamValve()
    if(BV==0): valve="Closed"
    if(BV==1): valve="Opened"
    ready=feg.GetV1Ready()
    #print(ready)
    if (ready==0): V1="Not Ready"
    if (ready==1): V1="Ready"
    
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    
    ht1=int(HT.GetHtValue())/1000
    ht=str(ht1),"kv"
    
    mag=eos.GetMagValue()
    mag=mag[2]
    
    func=eos.GetFunctionMode()[1]
    
    
    
    TemStem=eos.GetTemStemMode()
    if(TemStem==0):TS="TEM"
    if(TemStem==1): TS="STEM"
    
    #lab.config(text=time)
    
    pos=stage.GetPos()
    X=pos[0]
    X=round(X/1000,2)
    Y=pos[1]
    Y=round(Y/1000,2)
    Z=pos[2]
    Z=round(Z/1000,2)
    TX=pos[3]
    TX=round(TX,2)
    TY=pos[4]
    TY=round(TY,2)
    
    cls=BB.GetCLs()
    CLSAX=cls[0]
    CLSAY=cls[1]
    CLSAX=hex(CLSAX)
    CLSAY=hex(CLSAY)
    CLSAX=str(CLSAX.upper()[2:])
    CLSAY=str(CLSAY.upper()[2:])
    
    CLA1=BB.GetCLA1()
    CLA1X=CLA1[0]
    CLA1Y=CLA1[1]
    CLA1X=hex(CLA1X)
    CLA1Y=hex(CLA1Y)
    CLA1X=str(CLA1X.upper()[2:])
    CLA1Y=str(CLA1Y.upper()[2:])
        
    
    CLA2=BB.GetCLA2()
    CLA2X=CLA2[0]
    CLA2Y=CLA2[1]
    CLA2X=hex(CLA2X)
    CLA2Y=hex(CLA2Y)
    CLA2X=str(CLA2X.upper()[2:])
    CLA2Y=str(CLA2Y.upper()[2:])
    
    if(TS=="STEM"):
        cam=eos.GetStemCamValue()
        cam0=int(cam[0]/10)
        cam0=str(cam0)
                
    elif(TS=="TEM"): 
        cam0="..."
        
    #print(cam0,"cm")
    
    htst=gun.GetHtStts()
    if(htst==0): HTis="off"
    if(htst==1): HTis="on"
    if(htst==2): HTis="increasing"
    
    info=(str(ht1),"kv",'***',func,str(mag),TS)
    lab1.config(text=(info), font=('Verdana', 11, 'bold'))
    lab1.configure(background='black', foreground='lightblue')    
    
    lab16.config(text=('CameraLength:',cam0,"cm"),font=('Verdana', 9))
    lab16.configure(background='black', foreground='lightgreen')
    
    SP=eos.GetSpotSize()+1
    SP=str(SP)
    ALPHA=eos.GetAlpha()+1
    PROBE=eos.GetProbeMode()[1]
    lab9.config(text=(PROBE,"---Spot:",SP,"---Alpha",ALPHA), font=('Verdana', 11))
    lab9.configure(background='black', foreground='lightgreen')
    
    cam=TEM3.Camera3()
    a=cam.GetCurrentDensity()
    
    a=cam.GetCurrentDensity()
    ET=cam.GetExpTime()
    #print(ET)
    
    lab12.config(text=("Emission:",ems,"µA", "CurDens:",a,"pA/cm²"), font=('Verdana', 8, 'bold'))
    lab12.configure(background='black', foreground='lightblue')
    
    
    lab4.config(text=("--------------------------------------------------------"))
    lab4.configure(background='black', foreground='white')
    
    lab15.config(text=("-->STAGE<--"), font=('Verdana', 9, ' bold'))
    lab15.configure(background='black', foreground='orange')
    
    lab6.config(text=("X:",X,"Y:",Y), font=('Verdana', 9, 'bold'))
    lab6.configure(background='black', foreground='lightblue')
    
    lab7.config(text=("Z:",Z), font=('Verdana', 9, 'bold'))
    lab7.configure(background='black', foreground='lightblue')
    
    lab8.config(text=("TX:",TX,"TY:",TY), font=('Verdana', 9, 'bold'))
    lab8.configure(background='black', foreground='lightblue')
    
    
    lab5.config(text=("--------------------------------------------------------"))
    lab5.configure(background='black', foreground='white')
    
    
    lab14.config(text="BShift:", font=('Verdana', 9, 'italic'))
    lab14.configure(background='black', foreground='lightyellow')
    
    lab13.config(text=("X:",CLA1X,"___","Y:",CLA1Y ), font=('Verdana', 9, 'bold'))
    lab13.configure(background='black', foreground='yellow')
    
    lab11.config(text="CLStig:", font=('Verdana', 9, 'italic'))
    lab11.configure(background='black', foreground='lightyellow')
    
    lab2.config(text=("X:",CLSAX,"___","Y:",CLSAY ), font=('Verdana', 9, 'bold'))
    lab2.configure(background='black', foreground='yellow')
    
    lab23.config(text="BTilt:", font=('Verdana', 9, 'italic'))
    lab23.configure(background='black', foreground='lightyellow')
    
    lab22.config(text=("X:",CLA2X,"___","Y:",CLA2Y ), font=('Verdana', 9, 'bold'))
    lab22.configure(background='black', foreground='yellow')
    
    
   
    
    
    ready= tkinter.BooleanVar()
    
    #ready=False
    #Radiobutton1 = tkinter.Radiobutton(root,text = "HT Ready",variable = V1,value=V1 ,fg="black",bg="white",selectcolor="black")
    #Radiobutton1.configure(background='black', foreground='white')
    
    
    security=("V1:{}".format(V1),"---HTmode:{}-".format(HTis,end="\n"),"BeamValve:{}".format(valve),"---Emission:{}".format(emission))
    lab10.config(text=(security),font=('Helvetica',8,'bold'))
    #V1="Ready" #Valve V1 for test
    #BV=1 # Beam valve for test
    #HTis="on" #HT Status for test
    lab10.configure(background='orange', foreground='black')
    
    if(V1=="Ready" and BV==1 and HTis=="on"):
        lab10.configure(background='green', foreground='black')
    #if(V1=="Not Ready" or BV=0 ):
    #lab10.configure(background='red', foreground='black')
    
    
    #lab3['text'] = time 
    lab3.config(text=(time),font=('Verdana', 7, 'bold'))
    lab3.configure(background='black', foreground='gold')
    
    root.after(100, clock) # run itself again after 600 ms
    
    root.title("F200 Infos")
    root.configure(background='black')
    

# run first time
clock()

root.mainloop()