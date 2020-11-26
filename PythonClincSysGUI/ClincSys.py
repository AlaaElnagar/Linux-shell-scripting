
#from config import*
import tkinter
import sys
from tkinter import ttk
from PIL import Image, ImageTk


 
#******************************************************************************************************************************


#************************************			   ***************************************************************
#************************************ Sub functions      ***************************************************************
#************************************			   ***************************************************************


#******************************************************************************************************************************
#--------------common functions

# clear_text Responsible for clearing the words inside any entery
def clear_text(self):
        self.entry.delete(0, 'end')

def hide(self):
        """"""
        self.root.withdraw()

def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()

def show(self):
        """"""
        self.root.update()
        self.root.deiconify()

#******************************************************************************************************************************
#*****************************************  The following function concerned with Display patient*********************************
#********************************************************************************************************************************************
def clear ():
# 	1.0 TO Clr to start from first char in line 1    1.14  to start clear from this point to end   or to 1.20 for exa
	#PatientTxtSheet.delete('1.5', '1.7')
	PatientTxtSheet.delete('1.5', tkinter.END)

#This function responsible for calling the sheet of Patients
def GetTxt():
	global SheetTxt
	global scroll
	scroll=tkinter.Scrollbar(root)
	scroll.pack(side = tkinter.RIGHT)

	#TxtLabel.config (text = PatientTxtSheet.get ('1.0',tkinter.END))
	SheetTxt = open('file_handeling.txt').read()
	PatientTxtSheet.insert(tkinter.END,SheetTxt)




def ScrollBar(root):
	global main_frame
	global my_canvas
	global MY_SCROLLBAR
	global second_frame
	#This section concerned with scroll bar

	#creat a main frame to hold all contents
	main_frame = tkinter.Frame(root)
	main_frame.pack(fill=tkinter.BOTH,expand=1 )

	#creat canvas inside the main frame to hold in the scrllbar
	my_canvas = tkinter.Canvas(main_frame)
	my_canvas.pack(side = tkinter.LEFT ,fill= tkinter.BOTH, expand=1 )

	#add scrollbar to the canvas
	MY_SCROLLBAR = ttk.Scrollbar(main_frame,orient=tkinter.VERTICAL,command=my_canvas.yview)
	MY_SCROLLBAR.pack(side = tkinter.RIGHT ,fill= tkinter.Y )
	#configur canvas to scroll in y direction
	my_canvas.configure(yscrollcommand=MY_SCROLLBAR.set)

	#lambda llow the canvas to take respond from the mouse


	#my_canvas.bind('<configure>', lambda e: my_canvas.cofigure(scrollregion =my_canvas.bbox("all")))

	main_frame.bind(
	    "<Configure>",
	    lambda e: my_canvas.configure(
		scrollregion=my_canvas.bbox("all")
	    )
	)

	#creat another frame inside the canvas
	second_frame =tkinter.Frame(my_canvas)

	#add new frame to the window in the canvas
	my_canvas.create_window((0,0),window=second_frame,anchor="nw")





def CallTxt():
	global PatientTxtSheet

	PatientTxtSheet=tkinter.Text(second_frame,width=800,height=400,font=("Helvetica",12, "bold "))
	PatientTxtSheet.pack(side=tkinter.LEFT)
	GetTxt()


#******************************************************************************************************************************
#*****************************************  The following function concerned with Delete  patient*********************************
#********************************************************************************************************************************************

def DeleteFromFile():

	global ID_Label
	global ID_Message
	global PatientName
	ID_Message=tkinter.StringVar()

	EnteredID=AddPatientNameEnt4.get()

	ID_Label=tkinter.Label(top4,textvariable=ID_Message )
	ID_Label.place(x=110,y=50 )


			#searching for the ID
	#open file with read
	File = open ("file_handeling.txt",'r')
	#store all file in variable
	FileData=File.readlines()
	#search for the required id in the file  in this case searching by line
	for line in FileData:
	#search for the id in the line
		ID=line[line.find('$')+1:line.find('&')]
		PatientName=line[line.find('<')+1:line.find('>')]

		if ID==EnteredID:
			#get the name of the patient
			ID_Message.set(f"We wish u happy life mr/s {PatientName}")
			#open the file and delete all contents
			File = open ("file_handeling.txt",'w')
			#remove the patient
			FileData.remove(line)
			#write the file againline by line
			for line in FileData:
				File.write(line)
			#for security close the file
			File.close()
			break
		else:

			ID_Message.set("Sorry this patient dosen't exist         ")




	#if exist delete


	#else label sorry Invalid inpout




#******************************************************************************************************************************

#************************************			   ***************************************************************
#************************************ THE ADMIN WINDOW   ***************************************************************
#************************************			   ***************************************************************


#******************************************************************************************************************************

def AdminWindow1():

	global top1
	global canvas1
	global photo1
	global image
	global Entry1
	global Entry2
	global Label1
	global Label2
	global Button3
	global Button4
	top1=tkinter.Toplevel()
	top1.title("HOSPITAL ADMIN")
	top1.geometry("800x400+300+200")
	canvas1=tkinter.Canvas(top1,width=800,height=400)
	canvas1.pack()
	#photo1=tkinter.PhotoImage(file='h2.png')

	image = Image.open("PermanentStaff.jpg")
	photo1 = ImageTk.PhotoImage(image)

	canvas1.create_image(400,200,image=photo1,anchor=tkinter.CENTER)
	Entry1=tkinter.Entry(top1,width=20)
	Entry2=tkinter.Entry(top1,width=20,show="*")


	Label1=tkinter.Label(top1,text="USER")
	Label2=tkinter.Label(top1,text="PASS")
	Button3=tkinter.Button(top1,text='Sumbit',bg='SteelBlue2',command=Enter)
	Button3.place(x=40,y=55)


	Button4=tkinter.Button(top1,text='Back',bg='SteelBlue2',command=BackToStartWindow)
	Button4.place(x=740,y=365)

	Entry1.place(x=40,y=10)
	Entry2.place(x=40,y=35)
	Label1.place(x=0,y=10 )
	Label2.place(x=0,y=35)

	root.withdraw()


#A VARIABLEW THAT  I NEED TO DEFINE IT
counter=0

#******************************************************************************************************************************


#************************************			   ***************************************************************
#************************************ ENTER ADMIN MODE FUNC ************************************************************
#************************************			   ***************************************************************


#******************************************************************************************************************************

def Enter():
	global counter
	global ButtonAdminConent

	user=Entry1.get()
	password=Entry2.get()


	if password=="1234" and user=="ALAA":
		print("welcome")
		AdminContentWindow()


	else :
		counter+=1
		print ("wrong password")
	if counter==3:
		exit (0)


#******************************************************************************************************************************


#************************************			    ***************************************************************
#************************************ Back to main WINDOW ***************************************************************
#************************************			    ***************************************************************


#******************************************************************************************************************************

	         #BACK TO STAART
def BackToStartWindow0():


	top2.destroy()

	root.update()
	root.deiconify()


		#ADD PATIENT
def BackToStartWindow():

	top1.destroy()

	top2.update()
	top2.deiconify()


def BackToStartWindow1():
	top4.destroy()
	"""root.update()
	root.deiconify()"""
	top2.update()
	top2.deiconify()

def BackToStartWindow2():
	top5.destroy()
	"""root.update()
	root.deiconify()"""

	top2.update()
	top2.deiconify()

def BackToStartWindow3():
	top6.destroy()
	"""root.update()
	root.deiconify()"""

	top2.update()
	top2.deiconify()


def BackToStartWindow6():
	top7.update()
	top7.deiconify()

def BackToStartWindow8():
	top7.update()
	top7.deiconify()
	top6.destroy()

def BackToStartWindow7():
	top7.destroy()
	root.update()
	root.deiconify()





#******************************************************************************************************************************


#************************************			   ***************************************************************
#************************************ EXIT FUNCTION      ***************************************************************
#************************************			   ***************************************************************


#******************************************************************************************************************************
def Exit():
	exit (0)


#******************************************************************************************************************************


#************************************			     *************************************************************
#************************************ Admin Content window *************************************************************
#************************************			     *************************************************************


#******************************************************************************************************************************

def AdminContentWindow():
	global top2
	global canvas2
	global photo2
	global image2
	global ButtonAdminConentBack
	global ServiceChoosen
	global ButtonAdminConentSumbit

	top2=tkinter.Toplevel()
	top2.title("Admin options")
	top2.geometry("800x400+300+200")
	canvas2=tkinter.Canvas(top2,width=800,height=400)
	canvas2.pack()

	image2= Image.open("DC.jpg")
	photo2 = ImageTk.PhotoImage(image2)

	canvas2.create_image(400,200,image=photo2,anchor=tkinter.CENTER)
	top1.withdraw()
	ButtonAdminConentBack=tkinter.Button(top2,text='Back',bg='SteelBlue2',command=BackToStartWindow0)
	ButtonAdminConentBack.place(x=740,y=365)

	n = tkinter.StringVar()
	ServiceChoosen = ttk.Combobox(top2, width = 27, textvariable = n)

	# Adding combobox drop down list
	ServiceChoosen['values'] = (
                          'Add patient',
                          'Delete patient',
                          'Edit patient',
                          'Display patient',
        			   )

	ServiceChoosen.place(x=100, y = 50)
	ServiceChoosen.current()
	ButtonAdminConentSumbit=tkinter.Button(top2,text='Sumbit',bg='SteelBlue2',command=ServiceChoosenSumbt)
	ButtonAdminConentSumbit.place(x=100, y = 70)

def ServiceChoosenSumbt():
	global result

	result=ServiceChoosen.get()
	print (result)
	if result=="Add patient":
		AddPatient()
	elif result=="Delete patient":
		DeletePatient()
	elif result=="Edit patient":
		EditPatient()
	elif result=="Display patient":
		Displaypatient()



#******************************************************************************************************************************


#************************************			    ***************************************************************
#************************************ Add patient section ***************************************************************
#************************************			    ***************************************************************


#******************************************************************************************************************************
def WriteToFile():
	global File





	File =  open('file_handeling.txt','a+')


	File.write(f"\n		<{AddPatientNameEnt.get()}>")
	File.write(f"		~{AddPatientAgeEnt.get()}@")
	File.write(f"		({AddPatientNumbEnt.get()})")
	File.write(f"		${AddPatientIDEnt.get()}&")
	File.write(f"		[{AddPatientGendEnt.get()}]")



	AddPatientNameEnt.delete(0, 'end')
	AddPatientAgeEnt.delete(0, 'end')
	AddPatientNumbEnt.delete(0, 'end')
	AddPatientIDEnt.delete(0, 'end')
	AddPatientGendEnt.delete(0, 'end')

	File.close()



def AddPatient():
	global top3
	global canvas3
	global photo3
	global image3
	global ButtonAdminConentBack1
	global AdminSumbit2
	#PATIENT DATA
	global AddPatientNameEnt
	global AddPatientAgeEnt
	global AddPatientNumbEnt
	global AddPatientIDEnt
	global AddPatientGendEnt
	global ButtonAdminConentSumbit2


	global ButtonAdminConentSumbit2

	top3=tkinter.Toplevel()
	top3.title("Add patient")
	top3.geometry("800x400+300+200")
	canvas3=tkinter.Canvas(top3,width=800,height=400)
	canvas3.pack()

	image3= Image.open("DC.jpg")
	photo3 = ImageTk.PhotoImage(image3)

	canvas3.create_image(400,200,image=photo3,anchor=tkinter.CENTER)
	ButtonAdminConentBack1=tkinter.Button(top3,text='Back',bg='SteelBlue2',command=BackToStartWindow)
	ButtonAdminConentBack1.place(x=740,y=365)

	AddPatientNameEnt =tkinter.Entry(top3,width=20)
	AddPatientAgeEnt =tkinter.Entry(top3,width=20)
	AddPatientNumbEnt=tkinter.Entry(top3,width=20)
	AddPatientIDEnt  =tkinter.Entry(top3,width=20)
	AddPatientGendEnt=tkinter.Entry(top3,width=20)



	AddPatientNameEntLabel=tkinter.Label(top3,text="Name")
	AddPatientAgeEntLabel=tkinter.Label(top3,text="Age")
	AddPatientNumbEntLabel=tkinter.Label(top3,text="Phone")
	AddPatientIDEntLabel=tkinter.Label(top3,text="ID")
	AddPatientGendEntLabel=tkinter.Label(top3,text="gender")

	AddPatientNameEnt.place(x=110,y=30)
	AddPatientAgeEnt.place(x=110,y=60)
	AddPatientNumbEnt.place(x=110,y=90)
	AddPatientIDEnt.place(x=110,y=120)
	AddPatientGendEnt.place(x=110,y=150)

	AddPatientNameEntLabel.place(x=10,y=30)
	AddPatientAgeEntLabel.place(x=10,y=60)
	AddPatientNumbEntLabel.place(x=10,y=90)
	AddPatientIDEntLabel.place(x=10,y=120)
	AddPatientGendEntLabel.place(x=10,y=150)
	ButtonAdminConentSumbit2=tkinter.Button(top3,text='Sumbit',bg='SteelBlue2',command=WriteToFile)
	ButtonAdminConentSumbit2.place(x=130,y=180)


	top2.withdraw()





#******************************************************************************************************************************


#************************************			    ***************************************************************
#************************************   DeletePatient     ***************************************************************
#************************************			    ***************************************************************


#******************************************************************************************************************************
def DeletePatient() :

	global AddPatientNameEnt4
	global AddPatientNameEntLabel4


	global top4
	global canvas4
	global photo4
	global image4
	global ButtonAdminConentBack2
	global AdminSumbit3

	global ButtonAdminConentSumbit3

	top4=tkinter.Toplevel()
	top4.title("Delete patient")
	top4.geometry("800x400+300+200")
	canvas4=tkinter.Canvas(top4,width=1000,height=400)
	canvas4.pack()

	image4= Image.open("v.jpg")
	photo4 = ImageTk.PhotoImage(image4)

	canvas4.create_image(400,200,image=photo4,anchor=tkinter.CENTER)
	ButtonAdminConentBack2=tkinter.Button(top4,text='Back',bg='SteelBlue2',command=BackToStartWindow1)
	ButtonAdminConentBack2.place(x=740,y=365)

	ButtonAdminConentSumbit3=tkinter.Button(top4,text='Sumbit',bg='SteelBlue2',command=DeleteFromFile)
	ButtonAdminConentSumbit3.place(x=110,y=80)


	AddPatientNameEnt4 =tkinter.Entry(top4,width=20)
	AddPatientNameEntLabel4=tkinter.Label(top4,text="ID")
	AddPatientNameEnt4.place(x=110,y=30)
	AddPatientNameEntLabel4.place(x=10,y=30)

	top2.withdraw()

#******************************************************************************************************************************


#************************************			    ***************************************************************
#************************************  EditPatient        ***************************************************************
#************************************			    ***************************************************************


#******************************************************************************************************************************
def ModifyPatientData():

	nameRecive=NameModifyENtry.get()
	IDRecive=IDModifyENtry6.get()
	AgeRecive=AgeModifyENtry.get()
	PhoneRecive=PhoneModifyENtry.get()
	GenderRecive=GenderModifyENtry.get()


	File = open ("file_handeling.txt",'r')
	FileData=File.readlines()

	FileData[GetLinesIndexCountre]=(f"		<{nameRecive}>		~{IDRecive}@		${AgeRecive}&		({PhoneRecive})		[{GenderRecive}]")

	#open the file and delete all contents
	File = open ("file_handeling.txt",'w')
	#write the file againline by line
	for line in FileData:
		File.write(line)
			#for security close the file
	File.close()

	NameModifyENtry .delete(0, 'end')
	IDModifyENtry6 .delete(0, 'end')
	AgeModifyENtry .delete(0, 'end')
	PhoneModifyENtry.delete(0, 'end')
	GenderModifyENtry.delete(0, 'end')





def EditPatientData7():
	global ID_Label
	global PatientNameLabel
	global PatienAgeLabel
	global PatientPhoneLabel
	global PatientGenderLabel
	global PatientIDLabel
	global ID_Message
	global PatientName
	global PatienAge
	global PatientPhone
	global PatientGender
	global PatientID
	global EnteredID
	global NameModifyENtry
	global IDModifyENtry6
	global AgeModifyENtry
	global PhoneModifyENtry
	global GenderModifyENtry
	global GetLinesIndexCountre
	GetLinesIndexCountre=0

	ID_Message=tkinter.StringVar()
	PatientName=tkinter.StringVar()
	PatientAge=tkinter.StringVar()
	PatientPhone=tkinter.StringVar()
	PatientGender=tkinter.StringVar()
	PatientID=tkinter.StringVar()

	PatientNameLabel=tkinter.Label(top6,textvariable=PatientName )
	PatienAgeLabel=tkinter.Label(top6,textvariable=PatientAge )
	PatientPhoneLabel=tkinter.Label(top6,textvariable=PatientPhone )
	PatientGenderLabel=tkinter.Label(top6,textvariable=PatientGender)
	PatientIDLabel=tkinter.Label(top6,textvariable=PatientID )

	#get the id from the entery
	EnteredID=AddPatientNameEnt6.get()
	ID_Label=tkinter.Label(top6,textvariable=ID_Message )
	ID_Label.place(x=110,y=105 )
#the labels


			#searching for the ID
	#open file with read
	File = open ("file_handeling.txt",'r')
	#store all file in variable
	FileData=File.readlines()
	#search for the required id in the file  in this case searching by line
	for line in FileData:

		#To set element of lables
		PatientID.set(f"{line[line.find('$')+1:line.find('&')]}")
		PatientName.set(f"{line[line.find('<')+1:line.find('>')]}")
		PatientAge.set(f"{line[line.find('~')+1:line.find('@')]}")
		PatientPhone.set(f"{line[line.find('(')+1:line.find(')')]}")
		PatientGender.set(f"{line[line.find('[')+1:line.find(']')]}")
		#To get elements inside the file

		ID=line[line.find('$')+1:line.find('&')]
		Name   =	line[line.find('<')+1:line.find('>')]
		Age    =	line[line.find('~')+1:line.find('@')]
		Phone  =	line[line.find('(')+1:line.find(')')]
		Gender =	line[line.find('[')+1:line.find(']')]

		if ID==EnteredID:


			ID_Message.set(f"Welcome  mr/s {Name}  info.        ")

			break
		else:
			ID_Message.set("Sorry Patient dosen't exist          ")
			PatientID.set    ("0           	 ")
			PatientName.set  ("0          ")
			PatientAge.set   ("0                    ")
			PatientPhone.set ("0             ")
			PatientGender.set("0                     ")
	File.close()

	PatientNameLabel.place(x=10,y=200 )
	PatienAgeLabel.place(x=210,y=200)
	PatientPhoneLabel.place(x=310,y=200 )
	PatientGenderLabel.place(x=450,y=200)
	PatientIDLabel.place(x=540,y=200)






def EditPatientData():

	global ID_Label
	global PatientNameLabel
	global PatienAgeLabel
	global PatientPhoneLabel
	global PatientGenderLabel
	global PatientIDLabel
	global ID_Message
	global PatientName
	global PatienAge
	global PatientPhone
	global PatientGender
	global PatientID
	global EnteredID
	global NameModifyENtry
	global IDModifyENtry6
	global AgeModifyENtry
	global PhoneModifyENtry
	global GenderModifyENtry
	global GetLinesIndexCountre
	GetLinesIndexCountre=0

	ID_Message=tkinter.StringVar()
	PatientName=tkinter.StringVar()
	PatientAge=tkinter.StringVar()
	PatientPhone=tkinter.StringVar()
	PatientGender=tkinter.StringVar()
	PatientID=tkinter.StringVar()

	PatientNameLabel=tkinter.Label(top6,textvariable=PatientName )
	PatienAgeLabel=tkinter.Label(top6,textvariable=PatientAge )
	PatientPhoneLabel=tkinter.Label(top6,textvariable=PatientPhone )
	PatientGenderLabel=tkinter.Label(top6,textvariable=PatientGender)
	PatientIDLabel=tkinter.Label(top6,textvariable=PatientID )

	NameModifyENtry =tkinter.Entry(top6,width=20)
	IDModifyENtry6 =tkinter.Entry(top6,width=10)
	AgeModifyENtry =tkinter.Entry(top6,width=15)
	PhoneModifyENtry =tkinter.Entry(top6,width=10)
	GenderModifyENtry =tkinter.Entry(top6,width=10)
	#get the id from the entery
	EnteredID=AddPatientNameEnt6.get()
	ID_Label=tkinter.Label(top6,textvariable=ID_Message )
	ID_Label.place(x=110,y=105 )
#the labels


			#searching for the ID
	#open file with read
	File = open ("file_handeling.txt",'r')
	#store all file in variable
	FileData=File.readlines()
	#search for the required id in the file  in this case searching by line
	for line in FileData:

		#To set element of lables
		PatientID.set(f"{line[line.find('$')+1:line.find('&')]}")
		PatientName.set(f"{line[line.find('<')+1:line.find('>')]}")
		PatientAge.set(f"{line[line.find('~')+1:line.find('@')]}")
		PatientPhone.set(f"{line[line.find('(')+1:line.find(')')]}")
		PatientGender.set(f"{line[line.find('[')+1:line.find(']')]}")
		#To get elements inside the file

		ID=line[line.find('$')+1:line.find('&')]
		Name   =	line[line.find('<')+1:line.find('>')]
		Age    =	line[line.find('~')+1:line.find('@')]
		Phone  =	line[line.find('(')+1:line.find(')')]
		Gender =	line[line.find('[')+1:line.find(']')]

		if ID==EnteredID:
			#get the index of the line to modify it
			GetLinesIndexCountre= FileData.index(line)

			ID_Message.set(f"You can edit  mr {Name}  info.        ")

			break
		else:
			ID_Message.set("Sorry Patient dosen't exist          ")
			PatientID.set    ("0           	 ")
			PatientName.set  ("0          ")
			PatientAge.set   ("0                    ")
			PatientPhone.set ("0             ")
			PatientGender.set("0                     ")
	File.close()

	PatientNameLabel.place(x=10,y=200 )
	PatienAgeLabel.place(x=210,y=200)
	PatientPhoneLabel.place(x=310,y=200 )
	PatientGenderLabel.place(x=450,y=200)
	PatientIDLabel.place(x=540,y=200)


	NameModifyENtry.place(x=10,y=220 )
	IDModifyENtry6.place(x=210,y=220)
	AgeModifyENtry.place(x=310,y=220 )
	PhoneModifyENtry.place(x=450,y=220)
	GenderModifyENtry.place(x=540,y=220)

	LoadButtom=tkinter.Button(top6,text='Load',bg='goldenrod3',command=ModifyPatientData)
	LoadButtom.place(x=650,y=220)



def EditPatient():

	global AddPatientNameEnt6
	global AddPatientNameEntLabel6


	global top6
	global canvas6
	global photo6
	global image6
	global ButtonAdminConentBack6
	global AdminSumbit6
	global AddPatientNameEnt6
	global ButtonAdminConentSumbit6
	global FlagEntry
	FlagEntry=0

	top6=tkinter.Toplevel()
	top6.title("Edit patient")
	top6.geometry("800x400+300+200")
	canvas6=tkinter.Canvas(top6,width=1000,height=400)
	canvas6.pack()

	image6= Image.open("v.jpg")
	photo6 = ImageTk.PhotoImage(image6)

	canvas6.create_image(400,200,image=photo6,anchor=tkinter.CENTER)
	ButtonAdminConentBack6=tkinter.Button(top6,text='Back',bg='SteelBlue2',command=BackToStartWindow3)
	ButtonAdminConentBack6.place(x=740,y=365)

	ButtonAdminConentSumbit6=tkinter.Button(top6,text='Sumbit',bg='SteelBlue2',command=EditPatientData)
	ButtonAdminConentSumbit6.place(x=110,y=80)


	AddPatientNameEnt6 =tkinter.Entry(top6,width=20)
	AddPatientNameEntLabel6=tkinter.Label(top6,text="ID")
	AddPatientNameEnt6.place(x=110,y=30)
	AddPatientNameEntLabel6.place(x=10,y=30)

	top2.withdraw()



#************************************			    ***************************************************************
#************************************ Displaypatient      ***************************************************************
#************************************			    ***************************************************************


#******************************************************************************************************************************

def Displaypatient():

	global top5
	global canvas5
	global photo5
	global image4
	global ButtonAdminConentBack3
	global AdminSumbit4

	global ButtonAdminConentSumbit4

	top5=tkinter.Toplevel()
	top5.title("Display patient")
	top5.geometry("800x400+300+200")

	ScrollBar(top5)

	CallTxt()


	ButtonAdminConentBack3=tkinter.Button(top5,text='Back',bg='SteelBlue2',command=BackToStartWindow2)
	ButtonAdminConentBack3.place(x=740,y=365)


	top2.withdraw()

#******************************************************************************************************************************


#************************************			   ***************************************************************
#************************************ THE OPENING WINDOW ***************************************************************
#************************************			   ***************************************************************


#******************************************************************************************************************************
root=tkinter.Tk()

root.title("HOSPITAL")
root.geometry("800x400+300+200")
#CONCERNED WITH INSERTING PIC
canvas=tkinter.Canvas(root,width=800,height=400)

canvas.pack()
photo=tkinter.PhotoImage(file='h2.png')


canvas.create_image(400,200,image=photo,anchor=tkinter.CENTER)

#to make startup  icon

if ( sys.platform.startswith('win')):


    gui.iconbitmap('h2.jpg')
else:

   logo=tkinter.PhotoImage(file='h2.png')

   root.call('wm', 'iconphoto', root._w,logo)





#************************************			   ***************************************************************
#************************************ THE USER WINDOW ******************************************************************
#************************************			   ***************************************************************


#******************************************************************************************************************************

def UserWindow():
	global top7
	global canvas7
	global photo7
	global image7
	global ButtonAdminConentBack7
	global ServiceChoosen7
	global ButtonAdminConentSumbit7

	top7=tkinter.Toplevel()
	top7.title("User options")
	top7.geometry("800x400+300+200")
	canvas7=tkinter.Canvas(top7,width=800,height=400)
	canvas7.pack()

	image7= Image.open("DC.jpg")
	photo7 = ImageTk.PhotoImage(image7)

	canvas7.create_image(400,200,image=photo7,anchor=tkinter.CENTER)

	ButtonAdminConentBack7=tkinter.Button(top7,text='Back',bg='SteelBlue2',command=BackToStartWindow7)
	ButtonAdminConentBack7.place(x=740,y=365)

	n7= tkinter.StringVar()
	ServiceChoosen7= ttk.Combobox(top7, width = 27, textvariable = n7)

	# Adding combobox drop down list
	ServiceChoosen7['values'] = (
                          'View hospital departments',
                          'View all doctors details',
                          'View patient details',

        			   )

	ServiceChoosen7.place(x=100, y = 50)
	ServiceChoosen7.current()
	ButtonAdminConentSumbit7=tkinter.Button(top7,text='Sumbit',bg='SteelBlue2',command=ServiceChoosenSumbt7)
	ButtonAdminConentSumbit7.place(x=100, y = 70)
	root.withdraw()
def ServiceChoosenSumbt7():
	global result7
	top7.withdraw()

	result7=ServiceChoosen7.get()
	print (result7)
	if result7=="View hospital departments":
		View_hospitalDep()
	elif result7=="View all doctors details'":
		ViewDoctorsDetails()
	elif result7=="View patient details":
		ViewPatientDetails()



def View_hospitalDep():
	pass
def ViewDoctorsDetails():
	pass
def ViewPatientDetails():
	global AddPatientNameEnt6
	global AddPatientNameEntLabel6
	global top6
	global canvas6
	global photo6
	global image6
	global ButtonAdminConentBack6
	global AdminSumbit6
	global AddPatientNameEnt6
	global ButtonAdminConentSumbit6
	global FlagEntry
	FlagEntry=0

	top6=tkinter.Toplevel()
	top6.title("Show patient")
	top6.geometry("800x400+300+200")
	canvas6=tkinter.Canvas(top6,width=1000,height=400)
	canvas6.pack()

	image6= Image.open("v.jpg")
	photo6 = ImageTk.PhotoImage(image6)

	canvas6.create_image(400,200,image=photo6,anchor=tkinter.CENTER)
	ButtonAdminConentBack6=tkinter.Button(top6,text='Back',bg='SteelBlue2',command=BackToStartWindow8)
	ButtonAdminConentBack6.place(x=740,y=365)

	ButtonAdminConentSumbit6=tkinter.Button(top6,text='Sumbit',bg='SteelBlue2',command=EditPatientData7)
	ButtonAdminConentSumbit6.place(x=110,y=80)


	AddPatientNameEnt6 =tkinter.Entry(top6,width=20)
	AddPatientNameEntLabel6=tkinter.Label(top6,text="ID")
	AddPatientNameEnt6.place(x=110,y=30)
	AddPatientNameEntLabel6.place(x=10,y=30)







#******************************************************************************************************************************


#----------------------------------------------------------------


#******************************************************************************************************************************


#************************************			   ***************************************************************
#************************************ THE MAIN BUTTONS   ***************************************************************
#************************************			   ***************************************************************


#******************************************************************************************************************************


#to add buttons to WINDOW1

Button1=tkinter.Button(root,height=5,text=' USER ',bg='SteelBlue2',command=UserWindow)
Button1.place(x=447,y=140)

Button1=tkinter.Button(root,height=5,text='ADMIN',bg='SteelBlue2',command=AdminWindow1)
Button1.place(x=280,y=140)

Button5=tkinter.Button(root,text='Back',bg='SteelBlue2',command=Exit)
Button5.place(x=740,y=365)

#**************************




root.mainloop()
