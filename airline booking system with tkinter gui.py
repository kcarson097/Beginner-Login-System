#airline booking system with tkinter gui
#be able to book an airline seat on a flight
#economy, premium economy, business and first class
#store booking details in a database
#generate a booking ID for the customer from which they can query their booking
#once booking completed - send an email of the booking details to customer 
#in future better to repeat project using classes !!

from tkinter import *
import sqlite3
import smtplib
from tkinter import messagebox

#create database where booking details are stored
#connection = sqlite3.connect('booking_info1.db')
#c = connection.cursor()

#c.execute(''' CREATE TABLE bookings10(
            #first_name text,
            #last_name text,
            #passport_number text,
            #email text,
            #class_select VAR
#)''')

#connection.commit()
#connection.close()

#function to create booking and store details in database
#email details to customer

#main window config is found at bottom of code - booking_window

def check():
    #first check if seats are free - if there is then run create function
    
    Economy_Seats = 200
    Premium_Economy_Seats = 100
    Business_Seats = 50
    First_Seats = 0
        
        
    #check if selected seats available - note var is the output of the dropdown menu with the class choices in the booking_window
    if var.get() == 'Economy (50 pounds sterling)':
        
        if Economy_Seats > 0:
            Economy_Seats -= 1
            create()
        else:
            messagebox.showerror('Error','Sorry no seats remain in this class')
            booking = True
                
                
    if var.get() == 'Premium Economy (100 pounds sterling)':
        if  Premium_Economy_Seats > 0:
            Premium_Economy_Seats -= 1
            create()
        else:
            messagebox.showerror('Error','Sorry no seats remain in this class')
                
                
    if var.get() == 'Business (250 pounds sterling)':
        if Business_Seats > 0:
            Business_Seats -= 1
            create()
        else:
            messagebox.showerror('Error','Sorry no seats remain in this class')
                
    if var.get() == 'First Class (500 pounds sterling)':
        if First_Seats > 0:
            First_Seats -= 1
            create()
        else:
            messagebox.showerror('Error','Sorry no seats remain in this class')
                
                

def create():
        #store these detials on database
        connection = sqlite3.connect('booking_info1.db')
        c= connection.cursor()
     
        values = (f_name.get(), l_name.get(), passport.get(), email.get(), var.get())
        c.execute("INSERT INTO bookings10 VALUES (?,?,?,?,?)", values)
       
        connection.commit()
        
        #select details from database and create a booking summary for customer which can then be emailed to them
        c.execute('SELECT *, oid from bookings10')
        records = c.fetchall()
        for record in records:
            if record[2] == passport.get():
               
                booking_id = record[5]
                booking_info= (
                    'Subject - Booking Information' + '\n'
                    'From Booking' + '\n'
                    'To ' + f_name.get() + '\n' + '\n' + 
                    'Name -' + record[0] + ' ' + record[1] + '\n' + 
                                'Seat -' + ' ' + record[4]  + ' \n' +
                                 'BookingID -' + str(record[5])
                )
                print(booking_info)
                                
                
        connection.commit()
        connection.close()
       
        messagebox.showinfo('Booking Sucess','Booking successful ,your bookingID is ' + str(booking_id) + 
                            ' a confirmation email will be sent to '+ email.get())

       
        #send email to client
        send_email(booking_info)
        
        #clear entry fields for new booking
        f_name.delete(0, END)
        l_name.delete(0, END)
        passport.delete(0, END)
        email.delete(0, END)
        var.set('Economy £50')
        
        
        
def send_email(content):
        try:
            smtp_object = smtplib.SMTP('smtp.gmail.com',587)
            smtp_object.ehlo()
            smtp_object.starttls()

            email_database = 'enteremailhere'
            password = 'enterpassword here'
            smtp_object.login(email_database,password)
            print('login success')

            from_address = email_database
            to_address = email.get()

            subject = 'Booking Confirmation'
            message = content
            msg =  message
            smtp_object.sendmail(from_address, to_address, msg)
            print('Email Successfully Sent')
        except:
            messagebox.showerror('Email Error', 'Failed to send email')

#this will produce a summary of a booking using the provided booking number from customer
def view():
    view = Tk()
    view.title('View bookings')
    view.geometry('350x150')
    
    
    quote_label = Label(view, text = 'Please Enter your Booking ID Number :').grid(row = 0, column = 0 , columnspan = 2)
    quote1 = Entry(view)
    quote1.grid(row = 1, column = 0, columnspan = 2, padx = 7, pady = 7)
    
    quote_btn = Button(view, text = 'View Booking', command = lambda : quote(quote1.get()),height = 1, width = 15)
    quote_btn.grid(row = 2, column = 0 , columnspan = 2, padx = 7, pady = 7)
    
    def quote(ID):
        
        print(quote1.get())
        try:
            connection = sqlite3.connect('booking_info1.db')
            c = connection.cursor()
            c.execute('SELECT * FROM bookings10 WHERE oid = ' + str(quote1.get()))
            records = c.fetchall()
            print(records[0][1])
            details = 'Please see your details below :' + '\n' + 'Name : ' + records[0][0] + ' ' + records[0][1] + '\n' + 'Class : ' + records[0][4]
            details_label = Label(view, text = details).grid(row = 3 , column = 0, columnspan = 2, padx = 15, pady = 15)
            print(details)
        except:
            details = 'Sorry there is no booking corresponding to this ID, try again'
            details_label = Label(view, text = details).grid(row = 3 , column = 0, columnspan = 2, padx = 15, pady = 15)
            
    
    view.mainloop()
    


#create the main booking booking window
booking_window = Tk()
booking_window.geometry('380x260')
booking_window.title('New Booking')

var = StringVar()
var.set('Economy (50 pounds sterling)')

clss_list = ['Economy (50 pounds sterling)',
             'Premium Economy (100 pounds sterling)',
             'Business Economy (250 pounds sterling)',
             'First Class (500 pounds sterling)'
            ]

drop = OptionMenu(booking_window,var, *clss_list).grid(row = 5, column = 1)
    
drop_label = Label(booking_window, text = 'Select your class')
drop_label.grid(row = 5, column = 0,  pady = (15 , 0))

label = Label(booking_window, text = 'Please complete the following details :')
label.grid(row = 0, column = 0, columnspan = 2, padx = 15, pady = 15)

f_name = Entry(booking_window,width = 30)
f_name.grid(row = 1 , column = 1, padx = 20, pady = (10 , 0))

l_name = Entry(booking_window,width = 30)
l_name.grid(row = 2 , column = 1, padx = 20, pady = (10 , 0))

passport = Entry(booking_window,width = 30)
passport.grid(row = 3 , column = 1, padx = 20, pady = (10 , 0))

email = Entry(booking_window, width = 30)
email.grid(row = 4 , column = 1, padx = 20, pady = (10 , 0))

f_name_label = Label(booking_window, text = 'First Name')
f_name_label.grid(row = 1 , column = 0, pady = (10 , 0))

l_name_label = Label(booking_window, text = 'Last Name')
l_name_label.grid(row = 2 , column = 0, pady = (10 , 0))

passport_label = Label(booking_window, text = 'Passport Number')
passport_label.grid(row = 3 , column = 0, pady = (10 , 0))

email_label = Label(booking_window, text = 'Email')
email_label.grid(row = 4 , column = 0, pady = (10 , 0))

booking_button = Button(booking_window, text = 'Create booking', command = check, height = 1, width = 15)
booking_button.grid(row = 6, column = 0, columnspan = 1, pady = 15, padx = 10)

view_button = Button(booking_window, text = 'View Existing Booking', command = view, height = 1 , width = 20)
view_button.grid(row = 6, column = 1 , columnspan = 1, pady = 15)


booking_window.mainloop()
