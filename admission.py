import tkinter as tk
from tkinter import ttk
import os
from csv import DictWriter
ad = tk.Tk()
ad.title("ADMISSION PORTAL")
class admission:
    l=['NIT Trichy','NIT Karnataka','NIT Rourkela','NIT Warangal','NIT Calicut','NIT Nagpur','NIT Jaipur','NIT Kurushetra','NIT Silchar','NIT Durgapur','NIT Allahabad','NIT Jaladhar','NIT Surat']
    def __init__(self, master):
        self.l1=ttk.Label(master, text="Student Admission Portal")
        self.l1.grid(row=0,column=0)

        self.name_label=ttk.Label(master,text="Name ")
        self.name_label.grid(row=1,column=0,sticky=tk.W)

        self.age_label=ttk.Label(master,text="Age ")
        self.age_label.grid(row=2,column=0,sticky=tk.W)

        self.email_label=ttk.Label(master,text="Email ")
        self.email_label.grid(row=3,column=0,sticky=tk.W)

        self.gender_label=ttk.Label(master,text="Gender ")
        self.gender_label.grid(row=4,column=0,sticky=tk.W)

        self.l2=ttk.Label(master, text="Enter State/Central board percentage in the following subjects : ")
        self.l2.grid(row=5,column=0,sticky=tk.W)

        self.ph_label=ttk.Label(master,text="Physics ")
        self.ph_label.grid(row=6,column=0)

        self.che_label=ttk.Label(master,text="Chemistry")
        self.che_label.grid(row=7,column=0)

        self.math_label=ttk.Label(master,text="Maths")
        self.math_label.grid(row=8,column=0)

        self.jee_label=ttk.Label(master,text="Enter your jee mains rank ")
        self.jee_label.grid(row=9,column=0,sticky=tk.W)

        self.l3=ttk.Label(master, text="Eneter your choice of colleges : ")
        self.l3.grid(row=10,column=0,sticky=tk.W)

        self.p1_label=ttk.Label(master,text="Priority-1 ")
        self.p1_label.grid(row=11,column=0)

        self.p2_label=ttk.Label(master,text="Priority-2 ")
        self.p2_label.grid(row=12,column=0)

        self.p3_label=ttk.Label(master,text="Priority-3 ")
        self.p3_label.grid(row=13,column=0)

        self.name_var=tk.StringVar()
        self.name_entrybox=ttk.Entry(master,width=22,textvariable=self.name_var)
        self.name_entrybox.grid(row=1,column=1)
        self.name_entrybox.focus()

        self.age_var=tk.StringVar()
        self.age_entrybox=ttk.Entry(master,width=22,textvariable=self.age_var)
        self.age_entrybox.grid(row=2,column=1)
        
        self.email_var=tk.StringVar()
        self.email_entrybox=ttk.Entry(master,width=22,textvariable=self.email_var)
        self.email_entrybox.grid(row=3,column=1)

        self.gender_var=tk.StringVar()
        self.gender_rb1=ttk.Radiobutton(master,text='Male',value='Male',variable=self.gender_var)
        self.gender_rb1.grid(row=4,column=1)

        self.gender_rb2=ttk.Radiobutton(master,text='Female',value='Female',variable=self.gender_var)
        self.gender_rb2.grid(row=4,column=2)
        
        self.gender_rb3=ttk.Radiobutton(master,text='Other',value='Other',variable=self.gender_var)
        self.gender_rb3.grid(row=4,column=3)
        
        self.ph_var=tk.StringVar()
        self.ph_entrybox=ttk.Entry(master,width=10,textvariable=self.ph_var)
        self.ph_entrybox.grid(row=6,column=1)

        self.che_var=tk.StringVar()
        self.che_entrybox=ttk.Entry(master,width=10,textvariable=self.che_var)
        self.che_entrybox.grid(row=7,column=1)

        self.math_var=tk.StringVar()
        self.math_entrybox=ttk.Entry(master,width=10,textvariable=self.math_var)
        self.math_entrybox.grid(row=8,column=1)

        self.jee_var=tk.StringVar()
        self.jee_entrybox=ttk.Entry(master,width=10,textvariable=self.jee_var)
        self.jee_entrybox.grid(row=9,column=1)

        self.p1_var=tk.StringVar()
        self.p1_cb=ttk.Combobox(master,width=20,textvariable=self.p1_var,state='readonly')
        self.p1_cb['values']=tuple(admission.l)
        self.p1_cb.grid(row=11,column=1)

        self.p2_var=tk.StringVar()
        self.p2_cb=ttk.Combobox(master,width=20,textvariable=self.p2_var,state='readonly')
        self.p2_cb['values']=tuple(admission.l)
        self.p2_cb.grid(row=12,column=1)

        self.p3_var=tk.StringVar()
        self.p3_cb=ttk.Combobox(master,width=20,textvariable=self.p3_var,state='readonly')
        self.p3_cb['values']=tuple(admission.l)
        self.p3_cb.grid(row=13,column=1)

        def submit():
            n=self.name_var.get()
            a=self.age_var.get()
            e=self.email_var.get()
            g=self.gender_var.get()
            p=self.ph_var.get()
            c=self.che_var.get()
            m=self.math_var.get()
            j=self.jee_var.get()
            p1=self.p1_var.get()
            p2=self.p2_var.get()
            p3=self.p3_var.get()
            with open('admission.csv','a',newline='') as f:
                dict_writer=DictWriter(f, fieldnames=['Name','Age','Email','Gender','Physics(%)','Chemistry(%)','Maths(%)','JEE-Mains-Rank','Priority-1','Priority-2','Priority-3'])
                if os.stat('admission.csv').st_size==0:
                    dict_writer.writeheader()
                dict_writer.writerow({
                    'Name':n,
                    'Age':a,
                    'Email':e,
                    'Gender':g,
                    'Physics(%)':p,
                    'Chemistry(%)':c,
                    'Maths(%)':m,
                    'JEE-Mains-Rank':j,
                    'Priority-1':p1,
                    'Priority-2':p2,
                    'Priority-3':p3
                })

        self.submit_button=ttk.Button(master,text='Submit',command=submit)
        self.submit_button.grid(row=14,column=0)

a = admission(ad)
ad.mainloop()