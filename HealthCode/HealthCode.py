import mysql.connector
import random
from tkinter import *
from PIL import ImageTk, Image

# tkinter initialization
root = Tk()
root.geometry("480x270")
root.title("HealthCode")
root['background'] = '#DDC3A5'
frame = Frame(root,bg = '#DDC3A5')
frame.place(relx=0.5, rely=0.5, anchor=CENTER)
# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

# Create a database called "Medicine"
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists Medicine")

# Connect to the "Medicine" database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="Medicine"
)

mycursor = mydb.cursor()
mycursor.execute("drop table if exists patients")
mycursor.execute("CREATE TABLE if not exists Patients (aadhar_number INT PRIMARY KEY, name VARCHAR(255), age INT, blood_type VARCHAR(255), emergency_contacts VARCHAR(255), past_medical_illness VARCHAR(255), allergies VARCHAR(255))")

blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
medical_illnesses = ['None', 'High blood pressure', 'Diabetes', 'Asthma', 'Heart disease', 'Migraine', 'Arthritis', 'Depression']
allergies = ['None', 'Pollen', 'Peanuts', 'Shellfish', 'Eggs', 'Dairy', 'Gluten', 'Soy', 'Fish']

for i in range(10):
    aadhar_number = random.randint(10000000, 99999999)
    name = f'Patient {i+1}'
    age = random.randint(18, 80)
    blood_type = random.choice(blood_types)
    emergency_contacts = f'{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}'
    past_medical_illness = random.choice(medical_illnesses)
    allergy = random.choice(allergies)

    sql = f"INSERT INTO Patients (aadhar_number, name, age, blood_type, emergency_contacts, past_medical_illness, allergies) VALUES ({aadhar_number}, '{name}', {age}, '{blood_type}', '{emergency_contacts}', '{past_medical_illness}', '{allergy}')"
    mycursor.execute(sql)

# Commit the changes to the database
mydb.commit()

# Database work completes here.

# Funtions to be called in tkinter
def send():
  global data
  num = inp.get()
  mycursor.execute("use medicine")
  mycursor.execute("select * from patients where aadhar_number =%s",(num,))
  data = mycursor.fetchall()
  inp.destroy()
  B.destroy()
  adh.destroy()
  log.destroy()
  empty.destroy()
  tit.destroy()
  details()

def details():
  # print(len(data))
  font_style = ('courier', 15, 'bold')
  if len(data)==0:
    pos1 = Label(frame,text = "No Data Found!", anchor = 'w',background='#DDC3A5',font = font_style)
    pos1.pack(side = TOP)
  else:  
    for i in data:
      aadhar_number, name, age, blood_type, emergency_contacts, past_medical_illness, allergies = i[0],i[1],i[2],i[3],i[4],i[5],i[6]
      label1 = 'Aadhar Number: '+str(aadhar_number)
      pos1 = Label(text = label1, anchor = 'w',background='#DDC3A5',font = font_style)
      pos1.grid(column='0',row='1',sticky = W)

      label2 = 'Name: '+str(name)
      pos2 = Label(text = label2, anchor = 'w',background='#DDC3A5',font = font_style)
      pos2.grid(column='0',row='2',sticky = W)

      label3 = 'Age: '+str(age)
      pos3 = Label(text = label3, anchor = 'w',background='#DDC3A5',font = font_style)
      pos3.grid(column='0',row='3',sticky = W)

      label4 = 'Blood Type: '+str(blood_type)
      pos4 = Label(text = label4, anchor = 'w',background='#DDC3A5',font = font_style)
      pos4.grid(column='0',row='4',sticky = W)

      label5 = 'Emergency Contacts: '+str(emergency_contacts)
      pos5 = Label(text = label5, anchor = 'w',background='#DDC3A5',font = font_style)
      pos5.grid(column='0',row='5',sticky = W)

      label6 = 'Past Medical Illness: '+str(past_medical_illness)
      pos6 = Label(text = label6, anchor = 'w',background='#DDC3A5',font = font_style)
      pos6.grid(column='0',row='6',sticky = W)

      label7 = 'Allergies: '+str(allergies)
      pos7 = Label(text = label7, anchor = 'w',background='#DDC3A5',font = font_style)
      pos7.grid(column='0',row='7',sticky = W)

global num
tit = Label(text = 'HealthCode',font = ('courier', 25,'underline'),background='#DDC3A5')
tit.pack(side = TOP)
empty = Label(frame,text = "",background='#DDC3A5',font = ('courier', 5,'underline'))
empty.pack(side = TOP)
my_log = ImageTk.PhotoImage(Image.open("Logo.png"))
log = Label(frame,image = my_log, highlightthickness=2,highlightcolor= "black",highlightbackground = "red")
log.pack(side = TOP)
empty = Label(frame,text = "",background='#DDC3A5')
empty.pack(side = TOP)
inp = Entry(frame,width=12,background='#E0A96D',foreground = '#201E20',font = ('courier', 15, 'bold'),highlightthickness=2)
inp.pack(side = TOP)
num = inp.get()
print(num)
adh = Label(frame,text = 'Aadhar Number',font = ('courier', 10),background='#DDC3A5')
adh.pack(side = TOP)
B = Button(frame, width = 6,text='Submit',command=send,foreground = '#201E20',background='#E0A96D',font = ('courier', 10, 'bold'))
B.pack(side = TOP)

root.mainloop()
