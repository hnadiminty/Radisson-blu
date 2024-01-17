#import modules
import mysql.connector
from tkinter import messagebox
from tkinter import *
import os
 
# Designing window for registration
def view():
    pass
def bookings():
    pass
# Designing Main(first) window
def main_menu():
    global main_menu
    main_menu = Tk()
    main_menu.geometry("600x500")
    main_menu.title("Radisson Blu")
    Label(text=" * * * W E L C O M E * * * ", bg="cyan", width="300", height="2", font=("Bell MT", 18)).pack()
    Label(text="").pack()
    canvas = Canvas(main_menu, width = 250, height = 200)      
    canvas.pack()      
    img = PhotoImage(file="logo.png")      
    canvas.create_image(20,20, anchor=NW, image=img)      
    Label(text="").pack()
    Button(text="CUSTOMER", height="2", width="30", bg="deepskyblue4",command = customer).pack()
    Label(text="").pack()
    Button(text="EMPLOYEE", height="2", width="30",  bg="cyan",command=staff_login).pack()
    Label(text="").pack()
    Button(text="EXIT", height="2", width="30",  bg="cyan",command=ex6).pack()
    main_menu.mainloop()
def ex6():
    main_menu.destroy()
#customer    
def customer():
    
    global customer_screen
    customer_screen = Toplevel(main_menu)
    #main_screen = Tk()
    customer_screen.geometry("600x500")
    customer_screen.title("C U S T O M E R")
    Label(customer_screen,text="").pack()
    canvas = Canvas(customer_screen, width = 250, height = 200)      
    canvas.pack()      
    img = PhotoImage(file="customer.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
    Label(customer_screen,text="Great offers & packages when you book direct.", bg="cyan", width="300", height="2", font=("Calibri", 13)).pack()
    Label(customer_screen,text="").pack()
    Button(customer_screen,text="Login", height="2", width="30",  bg="cyan",command = login).pack()
    Label(customer_screen,text="").pack()
    Button(customer_screen,text="Register", height="2", width="30",  bg="cyan",command=register).pack()
    Label(customer_screen,text="").pack()
    Button(customer_screen,text="Exit", height="2", width="30",  bg="cyan",command=ex7).pack()
    customer_screen.mainloop()
def ex7():
    customer_screen.destroy()
    
 
#staff login
def staff_login():
    global staff_login_screen
    global susername_verify
    global spassword_verify
    susername_verify = StringVar()
    spassword_verify = StringVar()
 
    global susername_login_entry
    global spassword_login_entry
 
    staff_login_screen = Toplevel(main_menu)
    staff_login_screen.geometry("600x400")
    staff_login_screen.title("Employee Login")
    Label(staff_login_screen, text="Please enter details below to login",bg="cyan").pack()
    #img1 = PhotoImage(file="book.png")  
    Label(staff_login_screen, text="").pack()
    #canvas1 = Canvas(staff_login_screen, width = 250, height = 200)      
    #canvas1.pack()      
    #img1 = PhotoImage(file="book.png")      
    #canvas1.create_image(20,20, anchor=NW, image=img1)
    Label(staff_login_screen, text="Username * ").pack()
    susername_login_entry = Entry(staff_login_screen, textvariable=susername_verify)
    susername_login_entry.pack()
    Label(staff_login_screen, text="").pack()
    Label(staff_login_screen, text="Password * ").pack()
    spassword_login_entry = Entry(staff_login_screen, textvariable=spassword_verify, show= '*')
    spassword_login_entry.pack()
    Label(staff_login_screen, text="").pack()
    Button(staff_login_screen, text="Login", width=10, height=1, bg="cyan",command = slogin_verify).pack()
    Label(staff_login_screen, text="").pack()
    Button(staff_login_screen,text="Cancel", width=10, height=1, bg="cyan", command=ex5).pack()
def ex5():
    staff_login_screen.destroy()
def staff():
    global staff_screen
    #staff_screen = Tk()
    staff_screen = Toplevel(main_menu)
    staff_screen.geometry("600x600")
    staff_screen.title("E M P L O Y E E")

    Label(staff_screen,text="LOGIN SUCCESSFUL").pack()
    canvas = Canvas(staff_screen, width = 250, height = 200)      
    canvas.pack()      
    img = PhotoImage(file="staff.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
   
    Label(staff_screen,text="Great offers & packages when you book direct.", bg="cyan", width="300", height="2", font=("Calibri", 13)).pack()
    Label(staff_screen,text="").pack()
    Button(staff_screen,text="View Customer", height="2", width="30", command=viewc).pack()
    Label(staff_screen,text="").pack()
    Button(staff_screen,text="View Bookings", height="2", width="30", command=viewb).pack()
    Label(staff_screen,text="").pack()
    Button(staff_screen,text="Cancel Bookings", height="2", width="30", command=cancel_booking).pack()
    Label(staff_screen,text="").pack()
    #Button(staff_screen,text="Booking", height="2", width="30", command=Booking1).pack()
    #Label(staff_screen,text="").pack()
    Button(staff_screen,text="Exit", height="2", width="30", command=ex3).pack()
    staff_screen.mainloop()
def ex3():
    staff_screen.destroy()
def Booking1():
    pass

def register():
    global register_screen
    register_screen = Toplevel(customer_screen)
    register_screen.geometry("600x500")
    register_screen.title("R E G I S T E R")
   
    Label(register_screen,text="").pack()
   
    global username
    global password
    global mobile
    global name
    global email
    global address
    global username_entry
    global password_entry
    global name_entry
    global mobile_entry
    global address_entry
    global email_entry
    username = StringVar()
    password = StringVar()
    mobile = StringVar()
    name = StringVar()
    address = StringVar()
    email = StringVar()
    
    
    Label(register_screen, text="Please enter details below", bg="cyan").pack()
    Label(register_screen, text="").pack()
    name_lable = Label(register_screen, text="Name * ")
    name_lable.pack()
    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    mobile_lable = Label(register_screen, text="Mobile * ")
    mobile_lable.pack()
    mobile_entry = Entry(register_screen, textvariable=mobile)
    mobile_entry.pack()
    email_lable = Label(register_screen, text="Email * ")
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()
    address_lable = Label(register_screen, text="Address * ")
    address_lable.pack()
    address_entry = Entry(register_screen, textvariable=address)
    address_entry.pack()
  
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="cyan", command = register_user).pack()
 
    Label(register_screen, text="").pack()
    Button(register_screen, text="Cancel", width=10, height=1, bg="cyan", command = Ex8).pack()
def Ex8():
    register_screen.destroy()
# Designing window for login 
 
def login():
    
    global login_screen
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
    login_screen = Toplevel(customer_screen)

    login_screen.title("Customer Login")
    login_screen.geometry("300x350")
    Label(login_screen, text="Please enter details below to login",bg="cyan").pack()
    Label(login_screen, text="").pack()
    
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, bg="cyan",command = login_verify).pack()
    Label(login_screen, text="").pack()
    Button(login_screen,text="Cancel", width=10, height=1, bg="cyan", command=ex4).pack()
def ex4():
    login_screen.destroy()
# Implementing event on register button
 
def register_user():
    try:
        username_info = username.get()
        password_info = password.get()
        mobile_info = mobile.get()
        name_info = name.get()
        address_info = address.get()
        email_info = email.get()
    
        
        if username_info=="" :
            Label(register_screen, text="User Name cannot be empty", fg="red", font=("calibri", 11)).pack()
            #messagebox.showinfo("Registration ", "User Name cannot be empty")
        elif password_info=="" :
            Label(register_screen, text="Password Name cannot be empty", fg="red", font=("calibri", 11)).pack()
        elif mobile_info=="" :
            Label(register_screen, text="Mobile Name cannot be empty", fg="red", font=("calibri", 11)).pack()
        elif name_info=="" :
            Label(register_screen, text="Name Name cannot be empty", fg="red", font=("calibri", 11)).pack()
        elif address_info=="" :
            Label(register_screen, text="Address Name cannot be empty", fg="red", font=("calibri", 11)).pack()
        elif email_info=="" :
            Label(register_screen, text="Email Name cannot be empty", fg="red", font=("calibri", 11)).pack()
        else:
            mycursor = mydb.cursor()
            sql = "INSERT INTO customers (name, username,password,mobile,email,address) VALUES (%s, %s,%s,%s,%s,%s)"
            val = (name_info,username_info,password_info,mobile_info,email_info,address_info)
            r=mycursor.execute(sql, val)

            mydb.commit()
       
 
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            mobile_entry.delete(0, END)
            name_entry.delete(0, END)
            address_entry.delete(0, END)
            email_entry.delete(0, END)
            #//print(r)
            Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
            Label(register_screen, text="").pack()
            Button(register_screen, text="Login", width=10, height=1, bg="cyan",command = login).pack()
 
    except ConnectionError:
        Label(register_screen, text="Failed to insert record", fg="green", font=("calibri", 11)).pack()
       # print("Failed to insert record into Laptop table {}".format(error))
# Implementing event on login button 
def slogin_verify():
    username1 = susername_verify.get()
    password1 = spassword_verify.get()
    if username1=="" :
        Label(login_screen, text="UserName cannot be empty", fg="red", font=("calibri", 11)).pack()
        #messagebox.showinfo("LOGIN ", "UserName cannot be empty")
    elif password1=="" :
        Label(login_screen, text="Password cannot be empty", fg="red", font=("calibri", 11)).pack()
    else:
        susername_login_entry.delete(0, END)
        spassword_login_entry.delete(0, END)
        mycursor = mydb.cursor()
        sql = "select * from employee where username='"+username1+"' and password='"+password1+"'"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        count = mycursor.rowcount
        #for x in myresult:
        if count>0:
            staff()
        else:
            spassword_not_recognised()
 
    #else:
     #   user_not_found()
def login_verify():
    global u
    global p
    username1 = username_verify.get()
    password1 = password_verify.get()
    if username1=="" :
        Label(login_screen, text="UserName cannot be empty", fg="red", font=("calibri", 11)).pack()
        #messagebox.showinfo("LOGIN ", "UserName cannot be empty")
    elif password1=="" :
        Label(login_screen, text="Password cannot be empty", fg="red", font=("calibri", 11)).pack()
    else:
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
        mycursor = mydb.cursor()
        sql = "select * from customers where username='"+username1+"' and password='"+password1+"'"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        count = mycursor.rowcount
        #for x in myresult:
        if count>0:
            u=username1
            p=password1
            Customer_Menu()
        else:
            password_not_recognised()
 
    #else:
     #   user_not_found()
 
# Designing popup for login success

    
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("250x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="Booking", command=Booking).pack()
    
 
# Designing popup for login invalid password
def spassword_not_recognised():
    global spassword_not_recog_screen
    spassword_not_recog_screen = Toplevel(staff_login_screen)
    spassword_not_recog_screen.title("LOGIN FAILED")
    spassword_not_recog_screen.geometry("250x100")
    Label(spassword_not_recog_screen, text="Invalid Password ").pack()
    Button(spassword_not_recog_screen, text="OK", command=sdelete_password_not_recognised).pack()
  
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("LOGIN FAILED")
    password_not_recog_screen.geometry("250x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found

 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("250x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
def viewc():
    global view_customer
    view_customer = Toplevel(staff_screen)
    view_customer.title("View All Customers")
    view_customer.geometry("450x450")
    mycursor = mydb.cursor()
    sql = "select * from Customers"
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    count = mycursor.rowcount
    
    Lb1 = Listbox(view_customer,bg="cyan", width="450", height="10")
    Lb1.pack()
    #Lb1.insert(END,mycursor.fetchall())# "ID =>Name       =>Mobile       =>Email       =>Address")
    i=1
    if count>0:
        for x in myresult:
           #st=str(x[0])+" => "+str(x[1])+" => "+ str(x[4])+" => "+str(x[5])+" => "+str(x[6])
           Lb1.insert(i,x)
           i=i+1
    else:
        print('Customer not found')
    
    
    Button(view_customer, text="Exit", command=ex2).pack()          
def ex2():
    view_customer.destroy()
def viewb():
    global view_booking
    view_booking = Toplevel(staff_screen)
    view_booking.title("View All Bookings")
    view_booking.geometry("450x450")
    mycursor = mydb.cursor()
    sql = "select * from Booking"
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    count = mycursor.rowcount
    
    Lb1 = Listbox(view_booking,bg="cyan", width="450", height="10")
    #Lb1.insert(1, "ID =>  Date                  => Room_ID=>Room_Type=>Food_Id=>Food_Type=>Room Charges=>Food_Charges=>Grand_Total=>UserName")
    i=1
    if count>0:
        for x in myresult:
           #st=str(x[0])+" => "+str(x[1])+" => "+ str(x[2])+" => "+str(x[3])+" => "+str(x[4])+" => "+str(x[5])+" => "+str(x[6])+" => "+str(x[7])+" => "+str(x[8])+" => "+str(x[9])
           Lb1.insert(i,x)
           i=i+1
    else:
        print('Booking not found')
    Lb1.pack()
    Button(view_booking, text="Exit", command=ex1).pack()          
def ex1():
    view_booking.destroy()
# Deleting popups
def delete_staff_login_success():
    staff_login_success_screen.destroy()
def book_room():
    try:
        room_type=""
        rch=0
        food_id=0
        
        fch=0;
        gt=0
        room=""+tkvar.get() #roomno=tkvar.get()
        food=""+tkvar1.get()
        ds=days.get()
        if room=="" :
            Label(customer_booking_screen, text="Select a room no", fg="red", font=("calibri", 11)).pack()
            #messagebox.showinfo("Registration ", "User Name cannot be empty")
        elif food=="" :
            Label(customer_booking_screen, text="Selec food item", fg="red", font=("calibri", 11)).pack()
        
        else:
            print(room)
            print(food)
            print(days)
            mycursor = mydb.cursor()
            sql = "select * from Room where room_no="+room
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            count = mycursor.rowcount
            if count>0:
                for x in myresult:
                    room_type=x[1]
                    rch=x[2]
                    
            else:
                print('not found')
            mycursor = mydb.cursor()
            sql = "select * from Food where Food_Type='"+food+"'"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            count = mycursor.rowcount
            if count>0:
                for x in myresult:
                    food_id=x[0]
                    fch=x[2]
                    
            else:
                print('not found')

            
            mycursor = mydb.cursor()
            amt=rch*ds
            gt=fch+amt
            sql = "INSERT INTO booking(Room_No, Room_Type, Food_ID, Food_Type, Room_Charges,days,amount, Food_Charges, Grand_Total, UserName) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (room,room_type,food_id,food,rch,ds,amt,fch,gt,u)
            r=mycursor.execute(sql, val)

            mydb.commit()
            days_entry.delete(0, END)
          
            Label(customer_booking_screen, text="Booking Done Successfully", fg="red", font=("calibri", 11)).pack()
            Label(customer_booking_screen, text="").pack()
            #Button(customer_booking_screen, text="Exit", width=10, height=1, bg="cyan",command = ex).pack()

    except ConnectionError:
        Label(customer_booking_screen, text="Failed to insert record", fg="green", font=("calibri", 11)).pack()
def ex():
    main_menu.destroy();
    
    #customer_booking_screen.destroy()
def cancel_booking():
    global customer_Cancel_booking_screen
    global popupMenu
    global tkvar2
   
    customer_Cancel_booking_screen = Toplevel(staff_screen)
    customer_Cancel_booking_screen.geometry("600x500")
    customer_Cancel_booking_screen.title("CANCEL BOOKING")
    Label(customer_Cancel_booking_screen,text=" * * * BOOKING MENU * * * ", bg="cyan", width="300", height="2", font=("Bell MT", 18)).pack()
    Label(customer_Cancel_booking_screen,text="").pack()
   
    Label(customer_Cancel_booking_screen,text="Select Room No To Cancel booking ", bg="cyan", width="300", height="2", font=("Calibri", 13)).pack()
    Label(customer_Cancel_booking_screen,text="").pack()
    
    mycursor = mydb.cursor()
    sql = "select room_no from Booking"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    count = mycursor.rowcount
    
    if count>0:
        tkvar2 = StringVar(customer_Cancel_booking_screen)
          
        
        s=""
        for x in myresult:
            s=s+str(x[0])+","
            
        choices=(s.split(","))    
        tkvar2.set(str(x[0]))
        popupMenu=OptionMenu(customer_Cancel_booking_screen,tkvar2,*choices)
        popupMenu.pack()
        Label(customer_Cancel_booking_screen,text="").pack()
        Button(customer_Cancel_booking_screen,text="Cancel Booking", height="2", width="30",  bg="cyan",command = cancel_book).pack()
        Label(customer_Cancel_booking_screen,text="").pack()
        
    else:
         Label(customer_Cancel_booking_screen, text="Room Details not found, contact Admin", fg="red", font=("calibri", 11)).pack()
def cancel_book():
    try:
        if tkvar2=="" :
            Label(customer_Cancel_booking_screen, text="Select a room no to cancel", fg="red", font=("calibri", 11)).pack()
        else:
            mycursor = mydb.cursor()
            room=""+tkvar2.get()
            sql = "delete from booking  where room_no="+room
            r=mycursor.execute(sql)

            mydb.commit()
            Label(customer_Cancel_booking_screen, text="Record deleted successfully", fg="red", font=("calibri", 11)).pack()
            Label(customer_Cancel_booking_screen, text="").pack()
            Button(customer_Cancel_booking_screen,text="Exit", height="2", width="30",  bg="cyan",command=Ex9).pack()
   
 
    except ConnectionError:
        Label(customer_Cancel_booking_screen, text="Failed to delete record", fg="green", font=("calibri", 11)).pack()
def Ex9():
    customer_Cancel_booking_screen.destroy()
def viewr():
    global view_room
    view_room = Toplevel(customer_menu_screen)
    view_room.title("View Rooms")
    view_room.geometry("450x450")
    mycursor = mydb.cursor()
    sql = "select * from Room"
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    count = mycursor.rowcount
    
    Lb1 = Listbox(view_room,bg="cyan", width="450", height="10")
    #Lb1.insert(1, "ID =>  Date                  => Room_ID=>Room_Type=>Food_Id=>Food_Type=>Room Charges=>Food_Charges=>Grand_Total=>UserName")
    i=1
    if count>0:
        for x in myresult:
           #st=str(x[0])+" => "+str(x[1])+" => "+ str(x[2])+" => "+str(x[3])+" => "+str(x[4])+" => "+str(x[5])+" => "+str(x[6])+" => "+str(x[7])+" => "+str(x[8])+" => "+str(x[9])
           Lb1.insert(i,x)
           i=i+1
    else:
        print('Rom Details not found')
    Lb1.pack()
    Button(view_room, text="Exit", command=ex21).pack()          
def ex21():
    view_room.destroy()
def viewf():
    global view_food
    view_food = Toplevel(customer_menu_screen)
    view_food.title("View Rooms")
    view_food.geometry("450x450")
    mycursor = mydb.cursor()
    sql = "select * from Food"
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    count = mycursor.rowcount
    
    Lb1 = Listbox(view_food,bg="cyan", width="450", height="10")
    #Lb1.insert(1, "ID =>  Date                  => Room_ID=>Room_Type=>Food_Id=>Food_Type=>Room Charges=>Food_Charges=>Grand_Total=>UserName")
    i=1
    if count>0:
        for x in myresult:
           #st=str(x[0])+" => "+str(x[1])+" => "+ str(x[2])+" => "+str(x[3])+" => "+str(x[4])+" => "+str(x[5])+" => "+str(x[6])+" => "+str(x[7])+" => "+str(x[8])+" => "+str(x[9])
           Lb1.insert(i,x)
           i=i+1
    else:
        print('Fooditem not found')
    Lb1.pack()
    Button(view_food, text="Exit", command=ex221).pack()          
def ex221():
    view_food.destroy()    
def Customer_Menu():
    global customer_menu_screen
    #staff_screen = Tk()
    customer_menu_screen = Toplevel(login_screen)
    customer_menu_screen.geometry("600x600")
    customer_menu_screen.title("CUSTOMER MENU")

    Label(customer_menu_screen,text="LOGIN SUCCESSFUL").pack()
    canvas = Canvas(customer_menu_screen, width = 250, height = 200)      
    canvas.pack()      
    img = PhotoImage(file="staff.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
   
    Label(customer_menu_screen,text="Great offers & packages when you book direct.", bg="cyan", width="300", height="2", font=("Calibri", 13)).pack()
    Label(customer_menu_screen,text="").pack()
    Button(customer_menu_screen,text="Booking", height="2", width="30", command=Booking).pack()
    Label(customer_menu_screen,text="").pack()
    Button(customer_menu_screen,text="View Room", height="2", width="30", command=viewr).pack()
    Label(customer_menu_screen,text="").pack()
    Button(customer_menu_screen,text="View Food", height="2", width="30", command=viewf).pack()
    Label(customer_menu_screen,text="").pack()
    Button(customer_menu_screen,text="Exit", height="2", width="30", command=ex33).pack()
    customer_menu_screen.mainloop()
def ex33():
    customer_menu_screen.destroy()

def Booking():
    #login_success_screen.destroy()
    global customer_booking_screen
    global popupMenu
    global tkvar
    global tkvar1
    global days
    days = IntVar()
    global days_entry
    customer_booking_screen = Toplevel(customer_menu_screen)
    customer_booking_screen.geometry("600x500")
    customer_booking_screen.title("Book a Room")
    Label(customer_booking_screen,text=" * * * BOOKING MENU * * * ", bg="cyan", width="300", height="2", font=("Bell MT", 18)).pack()
    Label(customer_booking_screen,text="").pack()
   
    Label(customer_booking_screen,text="Select Room No.", bg="cyan", width="300", height="2", font=("Calibri", 13)).pack()
    Label(customer_booking_screen,text="").pack()
    
    mycursor = mydb.cursor()
    sql = "select room_no from Room"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    count = mycursor.rowcount
    
    if count>0:
        tkvar = StringVar(customer_booking_screen)
          
        
        s=""
        for x in myresult:
            s=s+str(x[0])+","
            
        choices=(s.split(","))    
        tkvar.set(str(x[0]))
        popupMenu=OptionMenu(customer_booking_screen,tkvar,*choices)
        popupMenu.pack()
        Label(customer_booking_screen, text="").pack()
        name_lable = Label(customer_booking_screen, text="Enter no of Days * ")
        name_lable.pack()
        days_entry = Entry(customer_booking_screen, textvariable=days)
        days_entry.pack()
        Label(customer_booking_screen,text="").pack()
        mycursor1 = mydb.cursor()
        sql = "select food_type from food"
        mycursor1.execute(sql)
        myresult1 = mycursor1.fetchall()
        count1 = mycursor1.rowcount
    
        if count1>0:
            tkvar1 = StringVar(customer_booking_screen)
          
        
        #('101','102','103','104','201','202')
            s=""
            for x in myresult1:
                s=s+str(x[0])+","
            
            choices1=(s.split(","))    
            tkvar1.set(str(x[0]))
            Label(customer_booking_screen,text="Select Food Item.", bg="cyan", width="300", height="2", font=("Calibri", 13)).pack()
            Label(customer_booking_screen,text="").pack()
    
            popupMenu1=OptionMenu(customer_booking_screen,tkvar1,*choices1)
            popupMenu1.pack()
            Label(customer_booking_screen,text="").pack()
            Button(customer_booking_screen,text="Book", height="2", width="30",  bg="cyan",command = book_room).pack()
            Label(customer_booking_screen,text="").pack()
            Button(customer_booking_screen,text="Exit", height="2", width="30",  bg="cyan",command=delete_booking).pack()
        else:
            Label(customer_booking_screen, text="Food item not found, contact Admin", fg="red", font=("calibri", 11)).pack()
    else:
         Label(customer_booking_screen, text="Room Details not found, contact Admin", fg="red", font=("calibri", 11)).pack()
    
def delete_booking():
    customer_booking_screen.destroy()
def sdelete_password_not_recognised():
    spassword_not_recog_screen.destroy()
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
mydb = mysql.connector.connect(host="localhost",user="root", passwd="root",database="harshinee")

main_menu()
