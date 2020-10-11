#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[16]:


from tkinter import *
import math

root= Tk()
root.title("Jupyter Calculator")
root.resizable(width=False, height=False)
root.geometry("510x675+500+40")                              #dimnesions of calculator ,size of output screen
mainFrame = Frame(root, bd=10, bg='gainsboro', relief=RIDGE)
mainFrame.grid()

innerFrame = Frame(root, bd=35, bg='medium slate blue', relief=RIDGE)
innerFrame.grid()

class Calc():
    def __init__(self):
        self.current = ''
        self.input_valur =True
        self.result=False
        self.forstnum = ''
        self.op=''
        self.total =0
        self.secondnum=''
        self.check_sum=False
        
    def clear_Entry():
        self.result = False
        self.current = '0'
        self.input_value=True
    
    def numberEntry(self,num):
        self.result =False
        firstnum =str(num)
        if self.input_value:
            self.current = secondnnum
            self.input_value =False
        else:
            if secondnum =='.':
                if second in firstnum:
                    return
            self.current = fristnum + secondnum
        self.display(self.current)
     
    def sum_of_total(self):
        self.result =True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())
            
    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)
    
   

added_value = Calc()


                        #this is screen, where output comes the top one
txtDisplay = Entry(innerFrame,font=('arial',18,'bold'),bd=10,width=28,justify=LEFT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,'0')



                        #this is for creating buttons for numbers 
numberpad ='789456123'
i=0
btn= []
for j in range(3,6):   #decides the loaction(row) for button.This includes space from top inlcuding screen,so we cant use (0,6) 
    for k in range(3): #decides column
        btn.append(Button(innerFrame,width=6,height=2,font=('arial', 18,'bold'), bd=7,text=numberpad[i])) #button styling
        btn[i].grid(row=j,column = k,pady=1)
        i +=1         #because of this all numbers comes or else only one will appear
        
        
        
 
                        #this is  for operators and other buttons,can do this method for numbers as well
    
Deletebtn = Button(innerFrame,text= '',width=6,height=2,font=('arial', 18,'bold'),bd=7,bg='red') #text came from MS word symbols, it is the erase button symbol
Deletebtn.grid(row=1,column=0,pady=1)     # loaction  

AllClearbtn = Button(innerFrame,text= 'C',width=6,height=2,font=('arial', 18,'bold'),bd=7,bg='red',
                     command= added_value.clear_Entry)
AllClearbtn.grid(row=1,column=1,pady=1)

Percentbtn = Button(innerFrame,text= '%',width=6,height=2,font=('arial', 18,'bold'),bd=7,bg='royal blue')
Percentbtn.grid(row=2,column=1,pady=1)

Divbtn = Button(innerFrame,text= '   /',width=6,height=2,font=('arial', 18,'bold'),bd=7,bg='light blue')
Divbtn.grid(row=1,column=3,pady=1)


Plusbtn = Button(innerFrame,text= '+',width=6,height=2,font=('arial', 18,'bold'),bd=7,bg='light blue')
Plusbtn.grid(row=2,column=2,pady=1)

Minusbtn = Button(innerFrame,text= '-',width=6,height=2,font=('arial', 18,'bold'),bd=7,bg='light blue')
Minusbtn.grid(row=2,column=3,pady=1)

Multibtn = Button(innerFrame,text= '*',width=6,height=2,font=('arial', 18,'bold'),bd=7,bg='light blue')
Multibtn.grid(row=1,column=2,pady=1)

Pibtn = Button(innerFrame,text= 'π',width=6,height=2,font=('arial', 18,'bold'),bd=7,bg='royal blue') # agin from Msword symbols
Pibtn.grid(row=2,column=0,pady=1)

Squbtn = Button(innerFrame,text= 'x^2',width=6,height=2,font=('arial', 18,'bold'),bd=7,bg='royal blue')
Squbtn.grid(row=3,column=3,pady=1)

Rootbtn = Button(innerFrame,text= '√',width=6,height=2,font=('arial', 18,'bold'),bd=7,bg='royal blue') # agin from Msword symbols
Rootbtn.grid(row=4,column=3,pady=1)

Equalsbtn = Button(innerFrame,text= '=',width=6,height=2,font=('arial', 18,'bold'),bd=7,bg='lime green')
Equalsbtn.grid(row=6,column=3,pady=1)

Zerobtn = Button(innerFrame,text= '0',width=6,height=2,font=('arial', 18,'bold'),bd=7,)
Zerobtn.grid(row=6,column=0,pady=1)

Dotbtn = Button(innerFrame,text= '.',width=6,height=2,font=('arial', 18,'bold'),bd=7,)
Dotbtn.grid(row=6,column=1,pady=1)

Bracketbtn = Button(innerFrame,text= '()',width=6,height=2,font=('arial', 18,'bold'),bd=7,)
Bracketbtn.grid(row=6,column=2,pady=1)

Factbtn = Button(innerFrame,text= 'n!',width=6,height=2,font=('arial', 18,'bold'),bd=7,bg='royal blue')
Factbtn.grid(row=5,column=3,pady=1)


root.mainloop()


# In[ ]:




