#!/usr/bin/env python
# coding: utf-8

# In[20]:


from tkinter import *
from tkinter import ttk


root=Tk()
root.geometry('800x500')
root1=Tk()
root1.geometry('800x500')
def entry():
    x=text1.get()
    x=int(x)
    
    
label=Label(text="population size",fg='black',font=('Arial',14))
label.grid(row=1,column=0,padx=(100,0),pady=(100,20))
label1=Label(text="rate of retain in range (0,100)",fg='black',font=('Arial',14))
label1.grid(row=2,column=0,padx=(100,0),pady=(20,20))
label2=Label(text="rate of random select in range (0,100)",fg='black',font=('Arial',14))
label2.grid(row=3,column=0,padx=(100,0),pady=(20,20))
label3=Label(text="mutation rate in range(0,1)",fg='black',font=('Arial',14))
label3.grid(row=4,column=0,padx=(100,0),pady=(20,20))
label4=Label(text="rate of random select in range (0,100)",fg='black',font=('Arial',14))
label4.grid(row=5,column=0,padx=(100,0),pady=(20,20))
text1=Entry(width='70')
text1.grid(row=1,column=1,padx=(100,0),pady=(100,20))
text2=Entry(width='70')
text2.grid(row=2,column=1,padx=(100,0),pady=(20,20))
text3=Entry(width='70')
text3.grid(row=3,column=1,padx=(100,0),pady=(20,20))
text4=Entry(width='70')
text4.grid(row=4,column=1,padx=(100,0),pady=(20,20))
text5=Entry(width='70')
text5.grid(row=5,column=1,padx=(100,0),pady=(20,20))
bu1=ttk.Button(root,text="start",command=entry)
bu1.grid(row=7,column=1,padx=(100,0),pady=(20,20))

root.mainloop()


# In[ ]:





# In[ ]:




