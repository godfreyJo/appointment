from tkinter import *
import sqlite3
import tkinter.messagebox

#connect to the database
conn = sqlite3.connect('database.db')

c = conn.cursor()

#empty list to later append

ids = []

#tkinter window

class AppWindow:
    def __init__(self,master):
        self.master = master

        #creating the frames

        self.left = Frame(master, width=800, height= 720, bg='lightSteelBlue3')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='pale turquoise')
        self.right.pack(side=RIGHT)


        #labels for the window

        self.heading= Label(self.left, text="The github hospital Appointments", font=('arial 40 bold'), fg='ivory4', bg='lightSteelBlue3')
        self.heading.place(x=0, y=0)

        #patients name details
        self.name= Label(self.left, text="Pateint's Name", font=('arial 18 bold' ), fg='ivory4', bg='lightSteelBlue3')
        self.name.place(x=0, y=100)

        #age

        self.age = Label(self.left, text="Age", font=('arial 18 bold' ), fg='ivory4', bg='lightSteelBlue3')
        self.age.place(x=0, y=140)

        #gender
        self.gender = Label(self.left, text="Gender", font=('arial 18 bold' ), fg='ivory4', bg='lightSteelBlue3')
        self.gender.place(x=0, y=180)

        #location
        self.location = Label(self.left, text="Location", font=('arial 18 bold' ), fg='ivory4', bg='lightSteelBlue3')
        self.location.place(x=0, y=220)

        #appointment time
        self.time = Label(self.left, text="Appointment Time", font=('arial 18 bold' ), fg='ivory4', bg='lightSteelBlue3')
        self.time.place(x=0, y=260)

        #phone
        self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold' ), fg='ivory4', bg='lightSteelBlue3')
        self.phone.place(x=0, y=260)


        #Entries
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)
    
        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=300)

        #button 
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='lightSteelBlue3', command=self.add_appointment)
        self.submit.place(x=300, y=340)

        #getting number of appointments
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        #ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        #displaying the logs in our right frame
        self.logs = Label(self.right, text = "logs", font=('arial 28 bold'), fg='ivory4', bg='lightSteelBlue3')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Total Appointments till now.." + str(self.final_id))

        #function to call when the submit is clicked
    def add_appointment(self):
        #getting user input
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        #checkin if the user  input is not empty

        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            messagebox.showinfo("Warning", "Please fill in all boxes")
        else:
            #now we add to the db
            sql = "INSTERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES (?,?,?,?,?,?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            messagebox.showinfo("Success", "Appointment for " + str(self.val1) + "has been created")

            self.box.insert(END, 'Appoinments fixed for ' +str(self.val1) + 'at' + str(self.val5))

# creating the object
root = Tk()
b = AppWindow(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()





