
#adding useful libs
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import shutil

#a dict,list which can be helpful for deleting account if wrong password is enterd 3 times
my_dict = {
    "email" : "none",
    "no_of_tries_left": int(3)
}

my_list = []
file = open("user_data.txt","r")
#append all emails in a list
for x in file:
    if x == "\n":
      continue
    data = x.split(',')
    print(data[1])
    my_list.append({"email":data[1],"no_of_tries_left":int(3)})
print(my_list)
    
#classes using inheritance
class Person:
    def __init__(self,type, name, email, password):
        self.type = type
        self.name = name
        self.email = email
        self.password = password
    

class Student(Person):
    def __init__(self,type, name, email, password,id):
        super().__init__(type,name, email, password)
        self.id = id

class Teacher(Person):
    def __init__(self,type,name, email, password, subject):
        super().__init__(type,name, email, password)
        self.subject = subject

class UGStudent(Student):
    def __init__(self,type, name, email, password,id, graduation_year):
            super().__init__(type,name, email, password, id)
            self.graduation_year = graduation_year

class PGStudent(Student):
    def __init__(self,type,name, email, password, id, course):
            super().__init__(type,name, email, password,id)
            self.course = course  


#functions to add data into a file
def save_data_teacher(teacher):
     with open("user_data.txt","a") as file:
          file.write(f"{teacher.type},{teacher.email},{teacher.password},{teacher.name},{teacher.subject}\n")
          my_list.append({"email":teacher.email,"no_of_tries_left":3})
          print(my_list)
          return "data saved successfully"
def save_data_UGstudent(UGstudent):
     with open("user_data.txt","a") as file:
          file.write(f"{UGstudent.type},{UGstudent.email},{UGstudent.password},{UGstudent.name},{UGstudent.id},{UGstudent.graduation_year}\n")
          my_list.append({"email":UGstudent.email,"no_of_tries_left":3})
          print(my_list)
          return "data saved successfully"
def save_data_PGstudent(PGstudent):
     with open("user_data.txt","a") as file:
          file.write(f"{PGstudent.type},{PGstudent.email},{PGstudent.password},{PGstudent.name},{PGstudent.id},{PGstudent.course}\n")
          my_list.append({"email":PGstudent.email,"no_of_tries_left":3})
          print(my_list)
          return "data saved successfully"

#function to check password
def check_password(password):
    flag =0
    flag1=0
    flag2 =0
    for x in password:
        if x.isupper():
            flag+=1
            break
    for x in password:
        if x.islower():
            flag+=1
            break
    for x in password:
        if x.isdigit():
            flag+=1
            break
    for x in password:
        if x=='!' or x=='@' or x=='#' or x=='%' or x=='$' or x=='&' or x=='*':
            flag1+=1
            break
    for x in password:
        if x==' ':
            flag2+=1
            break
    if  len(password)<8:
        return "Password too short"
    elif len(password)>12:
        return "Password too long"
    elif flag!=3:
        return "Password should contain at least one upper case, one digit, and one lower case"
    elif flag1!=1:
       return "It should contains one or more special character(s) from the list [! @ # $ % & *]"
    elif flag2==1:
       return "Password should not contain space"
    else: 
        return "Good password"

#function tocheck email
def check_email(email):
    if email.find("@gmail.com")==-1:
        return "Enter a valid email address"
    return "Good email"

#function to check graduation year
def check_graduation_year(graduation_year):
    if graduation_year.isdigit():
        if int(graduation_year)<0 or int(graduation_year)>2050:
            return "Enter a valid year"
        else:
            return "good"
    else:
        return "Enter a valid year"

#function which checks the email and password at time of sign in
def sign_in(email,password):
          file = open("user_data.txt","r")
          for x in file:
               if x == "\n":
                 continue
               data = x.split(',')
               if email!=data[1]:
                    continue
               if password == data[2]:
                    return "Sign In successfull"
               else:
                    return "Incorrect password"
               
          return "Email not found"
     
#function for teacher sign up gui     
def teacher_gui(email,password,name):
    root = tk.Tk()
    root.geometry("300x300")

    subject_label = tk.Label(root, text="subject")
    subject_label.pack()
    subject_entry = tk.Entry(root)
    subject_entry.pack()
    
    def enter():
         subject = subject_entry.get()
         teacher = Teacher("teacher",name,email,password,subject)
         result = save_data_teacher(teacher)
         messagebox.showinfo("Sign In",result)
         if result == "data saved successfully":
             root.destroy()
             main_menu()

    sign_up_button = tk.Button(root, text="sign_up", command=enter)
    sign_up_button.pack(pady=5)
    def go_to_main_menu():
         root.destroy()
         main_menu()
    main_menu_button = tk.Button(root, text="Main Menu", command=go_to_main_menu)
    main_menu_button.pack(pady=5)
    
    root.mainloop()

#function for student sign up gui 
def student_gui(email,password,name):
    root = tk.Tk()
    root.geometry("300x300")

    id_label = tk.Label(root, text="ID")
    id_label.pack()
    id_entry = tk.Entry(root)
    id_entry.pack()

    values = ["UGstudent", "PGstudent"]
    combobox = ttk.Combobox(root, values=values)
    combobox.set("Select account type")  
    combobox['values']=values
    combobox.pack(pady=20)
    
    def enter():
         id = id_entry.get()
         if combobox.current()==0:
            root.destroy()
            UGstudent_gui(email,password,name,id)
         else:
            root.destroy()
            PGstudent_gui(email,password,name,id)

    sign_up_button = tk.Button(root, text="sign_up", command=enter)
    sign_up_button.pack(pady=5)
    def go_to_main_menu():
         root.destroy()
         main_menu()
    main_menu_button = tk.Button(root, text="Main Menu", command=go_to_main_menu)
    main_menu_button.pack(pady=5)
    
    root.mainloop()

#function for UGstudent sign up gui 
def UGstudent_gui(email,password,name,id):
    root = tk.Tk()
    root.geometry("300x300")

    graduation_year_label = tk.Label(root, text="graduation year")
    graduation_year_label.pack()
    graduation_year_entry = tk.Entry(root)
    graduation_year_entry.pack()
    
    def enter():
        graduation_year = graduation_year_entry.get()
        if check_graduation_year(graduation_year)!="good":
             messagebox.showinfo("Bad year",check_graduation_year(graduation_year))
        else:
         UGstudent = UGStudent("UGstudent",name,email,password,id,graduation_year)
         result = save_data_UGstudent(UGstudent)
         messagebox.showinfo("Sign In",result)
         if result == "data saved successfully":
             root.destroy()
             main_menu()

    sign_up_button = tk.Button(root, text="sign_up", command=enter)
    sign_up_button.pack(pady=5)
    def go_to_main_menu():
         root.destroy()
         main_menu()
    main_menu_button = tk.Button(root, text="Main Menu", command=go_to_main_menu)
    main_menu_button.pack(pady=5)
    
    root.mainloop()

#function for PGstudent sign up gui 
def PGstudent_gui(email,password,name,id):
    root = tk.Tk()
    root.geometry("300x300")

    course_label = tk.Label(root, text="course name")
    course_label.pack()
    course_entry = tk.Entry(root)
    course_entry.pack()
    
    def enter():
         course = course_entry.get()
         PGstudent =    PGStudent("PGstudent",name,email,password,id,course)
         result = save_data_PGstudent(PGstudent)
         messagebox.showinfo("Sign In",result)
         if result == "data saved successfully":
             root.destroy()
             main_menu()

    sign_up_button = tk.Button(root, text="sign_up", command=enter)
    sign_up_button.pack(pady=5)
    def go_to_main_menu():
         root.destroy()
         main_menu()
    main_menu_button = tk.Button(root, text="Main Menu", command=go_to_main_menu)
    main_menu_button.pack(pady=5)
    
    root.mainloop()

#functon of sign up gui
def sign_up_gui():
    root = tk.Tk()
    root.geometry("300x300")
    name_label = tk.Label(root, text="name")
    name_label.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()
    
    email_label = tk.Label(root, text="Email")
    email_label.pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    password_label = tk.Label(root, text="Password")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    
    values = ["Teacher", "Student"]
    combobox = ttk.Combobox(root, values=values)
    combobox.set("Select account type")  
    combobox['values']=values
    combobox.pack(pady=20)

    def enter():
        email = email_entry.get()
        password = password_entry.get()
        name = name_entry.get()
        if check_email(email)!="Good email":
            messagebox.showinfo("Bad email",check_email(email))
        elif check_password(password)!="Good password":
            messagebox.showinfo("Bad password",check_password(password))
        elif combobox.current()==0:
            root.destroy()
            teacher_gui(email,password,name)
        else:
             root.destroy()
             student_gui(email,password,name)

    sign_up_button = tk.Button(root, text="sign_up", command=enter)
    sign_up_button.pack(pady=5)
    def go_to_main_menu():
         root.destroy()
         main_menu()
    main_menu_button = tk.Button(root, text="Main Menu", command=go_to_main_menu)
    main_menu_button.pack(pady=5)


    root.mainloop()

#function to delete a line from the file
def delete_line(email):
    file = open("user_data.txt","r")
    for x in file:
        data = x.split(',')
        if x == "\n":
          continue
        for y in my_list:
            if y["email"] == email:
                my_list.remove(y)
                break
        print(my_list)
        if(email == data[1]):
          file_path = 'user_data.txt'
          temp_file_path = 'temp_file.txt'
          with open(file_path, 'r') as original_file:
              with open(temp_file_path, 'w') as temp_file:
                  for line in original_file:
                     if line.strip() != x.strip():
                       temp_file.write(line)
          shutil.move(temp_file_path, file_path)
          return "DELETED SUCCESSFULLY"

#functon of teacher update gui
def update_teacher_gui(email):
    root = tk.Tk()
    root.geometry("300x400")
    root.title("Update information")

    label = tk.Label(root,text="Enter the new details",font=('Arial',14))
    label.pack(padx=10,pady=5)
    
    values = ["name", "email","password","subject"]
    combobox = ttk.Combobox(root, values=values)
    combobox.set("Select option")  
    combobox['values']=values
    combobox.pack(pady=20)

    new_label = tk.Label(root, text="new detail")
    new_label.pack()
    new_entry = tk.Entry(root)
    new_entry.pack()
    
    def enter():
      new_detail = new_entry.get()
      file = open("user_data.txt","r")
      for x in file:
       if x == "\n":
        continue
       data = x.split(',')
       if data[1] == email:
        if combobox.current()==0:
             data[3] = new_detail
             teacher = Teacher(data[0],data[3],data[1],data[2],data[4])
             delete_line(data[1])
             save_data_teacher(teacher)
             messagebox.showinfo("Sign In","Data updated")
             root.destroy()
             sign_in_menu(email)
        elif combobox.current()==1:
            if check_email(new_detail)!="Good email":
               messagebox.showinfo("Bad email",check_email(new_detail))
            else:
                delete_line(data[1])
                data[1] = new_detail
                teacher = Teacher(data[0],data[3],data[1],data[2],data[4])
                save_data_teacher(teacher)
                messagebox.showinfo("Sign In","Data updated")
                root.destroy()
                sign_in_menu(data[1])
        elif combobox.current()==2:
            if check_password(new_detail)!="Good password":
                messagebox.showinfo("Bad password",check_password(new_detail))
            else:
                data[2] = new_detail
                teacher = Teacher(data[0],data[3],data[1],data[2],data[4])
                delete_line(data[1])
                save_data_teacher(teacher)
                messagebox.showinfo("Sign In","Data updated")
                root.destroy()
                sign_in_menu(email)
        else:
            data[4] = new_detail
            teacher = Teacher(data[0],data[3],data[1],data[2],data[4])
            delete_line(data[1])
            save_data_teacher(teacher)
            messagebox.showinfo("Sign In","Data updated")
            root.destroy()
            sign_in_menu(email)

    update_button = tk.Button(root, text="update", command=enter)
    update_button.pack(pady=5)

    def go_to_main_menu():
         root.destroy()
         main_menu()
    main_menu_button = tk.Button(root, text="Main Menu", command=go_to_main_menu)
    main_menu_button.pack(pady=5)

#functon of UGstudent update gui
def update_UGstudent_gui(email):
    root = tk.Tk()
    root.geometry("300x400")
    root.title("Update information")

    label = tk.Label(root,text="Enter the new details",font=('Arial',14))
    label.pack(padx=10,pady=5)
    
    values = ["name", "email","password","ID","graduation_year"]
    combobox = ttk.Combobox(root, values=values)
    combobox.set("Select option")  
    combobox['values']=values
    combobox.pack(pady=20)

    new_label = tk.Label(root, text="new detail")
    new_label.pack()
    new_entry = tk.Entry(root)
    new_entry.pack()
    
    def enter():
      new_detail = new_entry.get()
      file = open("user_data.txt","r")
      for x in file:
       if x == "\n":
        continue
       data = x.split(',')
       if data[1] == email:
        if combobox.current()==0:
             data[3] = new_detail
             student = UGStudent(data[0],data[3],data[1],data[2],data[4],data[5])
             delete_line(data[1])
             save_data_UGstudent(student)
             messagebox.showinfo("Sign In","Data updated")
             root.destroy()
             sign_in_menu(email)
        elif combobox.current()==1:
            if check_email(new_detail)!="Good email":
               messagebox.showinfo("Bad email",check_email(new_detail))
            else:
                delete_line(data[1])
                data[1] = new_detail
                student = UGStudent(data[0],data[3],data[1],data[2],data[4],data[5])
                save_data_UGstudent(student)
                messagebox.showinfo("Sign In","Data updated")
                root.destroy()
                sign_in_menu(data[1])
        elif combobox.current()==2:
            if check_password(new_detail)!="Good password":
                messagebox.showinfo("Bad password",check_password(new_detail))
            else:
                data[2] = new_detail
                student = UGStudent(data[0],data[3],data[1],data[2],data[4],data[5])
                delete_line(data[1])
                save_data_UGstudent(student)
                messagebox.showinfo("Sign In","Data updated")
                root.destroy()
                sign_in_menu(email)
        elif combobox.current()==3:
            data[4] = new_detail
            student =UGStudent(data[0],data[3],data[1],data[2],data[4],data[5])
            delete_line(data[1])
            save_data_UGstudent(student)
            messagebox.showinfo("Sign In","Data updated")
            root.destroy()
            sign_in_menu(email)
        else:
         data[5] = new_detail
         if check_graduation_year(new_detail)!="good":
            messagebox.showinfo("Bad year","Enter a valid year")
         else:
            student =UGStudent(data[0],data[3],data[1],data[2],data[4],data[5])
            delete_line(data[1])
            save_data_UGstudent(student)
            messagebox.showinfo("Sign In","Data updated")
            root.destroy()
            sign_in_menu(email)

    update_button = tk.Button(root, text="update", command=enter)
    update_button.pack(pady=5)

    def go_to_main_menu():
         root.destroy()
         main_menu()
    main_menu_button = tk.Button(root, text="Main Menu", command=go_to_main_menu)
    main_menu_button.pack(pady=5)

#functon of PGstudent update gui
def update_PGstudent_gui(email):
    root = tk.Tk()
    root.geometry("300x400")
    root.title("Update information")

    label = tk.Label(root,text="Enter the new details",font=('Arial',14))
    label.pack(padx=10,pady=5)
    
    values = ["name", "email","password","ID","course"]
    combobox = ttk.Combobox(root, values=values)
    combobox.set("Select option")  
    combobox['values']=values
    combobox.pack(pady=20)

    new_label = tk.Label(root, text="new detail")
    new_label.pack()
    new_entry = tk.Entry(root)
    new_entry.pack()
    
    def enter():
      new_detail = new_entry.get()
      file = open("user_data.txt","r")
      for x in file:
       if x == "\n":
        continue
       data = x.split(',')
       if data[1] == email:
        if combobox.current()==0:
             data[3] = new_detail
             student = PGStudent(data[0],data[3],data[1],data[2],data[4],data[5])
             delete_line(data[1])
             save_data_PGstudent(student)
             messagebox.showinfo("Sign In","Data updated")
             root.destroy()
             sign_in_menu(email)
        elif combobox.current()==1:
            if check_email(new_detail)!="Good email":
               messagebox.showinfo("Bad email",check_email(new_detail))
            else:
                delete_line(data[1])
                data[1] = new_detail
                student = PGStudent(data[0],data[3],data[1],data[2],data[4],data[5])
                save_data_PGstudent(student)
                messagebox.showinfo("Sign In","Data updated")
                root.destroy()
                sign_in_menu(data[1])
        elif combobox.current()==2:
            if check_password(new_detail)!="Good password":
                messagebox.showinfo("Bad password",check_password(new_detail))
            else:
                data[2] = new_detail
                student = PGStudent(data[0],data[3],data[1],data[2],data[4],data[5])
                delete_line(data[1])
                save_data_PGstudent(student)
                messagebox.showinfo("Sign In","Data updated")
                root.destroy()
                sign_in_menu(email)
        elif combobox.current()==3:
            data[4] = new_detail
            student =PGStudent(data[0],data[3],data[1],data[2],data[4],data[5])
            delete_line(data[1])
            save_data_PGstudent(student)
            messagebox.showinfo("Sign In","Data updated")
            root.destroy()
            sign_in_menu(email)
        else:
            data[5] = new_detail
            student =PGStudent(data[0],data[3],data[1],data[2],data[4],data[5])
            delete_line(data[1])
            save_data_PGstudent(student)
            messagebox.showinfo("Sign In","Data updated")
            root.destroy()
            sign_in_menu(email)

    update_button = tk.Button(root, text="update", command=enter)
    update_button.pack(pady=5)

    def go_to_main_menu():
         root.destroy()
         main_menu()
    main_menu_button = tk.Button(root, text="Main Menu", command=go_to_main_menu)
    main_menu_button.pack(pady=5)

#functon of update gui
def update_user_gui(email):
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Update information")
    

    file = open("user_data.txt","r")
    def enter():
     for x in file:
        data = x.split(',')
        if x == "\n":
          continue
        if(email == data[1]):
            if data[0] == "teacher":
                root.destroy()
                #delete_line(email)
                update_teacher_gui(email)
            elif data[0] == "UGstudent":
                root.destroy()
                #delete_line(email)
                update_UGstudent_gui(email)
            else:
                root.destroy()
                #delete_line(email)
                update_PGstudent_gui(email)

    enter()
    def go_to_main_menu():
         root.destroy()
         main_menu()
    main_menu_button = tk.Button(root, text="Main Menu", command=go_to_main_menu)
    main_menu_button.pack(pady=5)

#function for sign in main menu
def sign_in_menu(email):
     root = tk.Tk()
     root.geometry("300x300")
     
     label = tk.Label(root,text="WELCOME",font=('Arial',16))
     label.pack(padx=10,pady=5)
     label = tk.Label(root,text=email,font=('Arial',12))
     label.pack(padx=10,pady=5)
     label = tk.Label(root,text="What's in your mind",font=('Arial',10))
     label.pack(padx=10,pady=5)

     def do_update():
          root.destroy()
          update_user_gui(email)
     def do_delete():
      root.destroy()
      result = delete_line(email)
      messagebox.showinfo("DELETE",result)   
      main_menu()

     update_user_button = tk.Button(root,text="Update User",command=do_update)
     update_user_button.pack(pady=5)
     delete_user_button = tk.Button(root,text="Delete User",command=do_delete)
     delete_user_button.pack(pady=5)

     def go_to_main_menu():
         root.destroy()
         main_menu()
     main_menu_button = tk.Button(root, text="Main Menu", command=go_to_main_menu)
     main_menu_button.pack(pady=5)
     root.mainloop()

#function for main menu
def main_menu():
    root = tk.Tk()
    root.geometry("300x300")
    label = tk.Label(root,text="WELCOME",font=('Arial',16))
    label.pack(padx=10,pady=10)
    
    email_label = tk.Label(root, text="Email")
    email_label.pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    password_label = tk.Label(root, text="Password")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def submit():
        email = email_entry.get()
        password = password_entry.get()
        result = sign_in(email,password)
        messagebox.showinfo("Sign In",result)
        if result == "Sign In successfull":
             root.destroy()
             for x in my_list:
                if x["email"] == email:
                    x['no_of_tries_left'] =3
             sign_in_menu(email)
        elif result == "Incorrect password":
            for x in my_list:
                if x["email"] == email:
                    x["no_of_tries_left"] -=1 
                    messagebox.showinfo("Sign In","No. of tries left "+ str(x["no_of_tries_left"]))
                    if x["no_of_tries_left"] ==0:
                      delete_line(email)
                      messagebox.showinfo("Sign In","Max no. of tries exceedes\ndeactivating account")
     
    submit_button = tk.Button(root, text="Sign In", command=submit)
    submit_button.pack()

    def do_sign_up():
         root.destroy()
         sign_up_gui()
    label = tk.Label(root,text="\n\nDont have an account!",font=('Arial',12))
    label.pack(padx=10,pady=5)
    sign_up_button = tk.Button(root, text="Sign Up", command=do_sign_up)
    sign_up_button.pack(pady=5)
    root.mainloop()

#calling main menu
main_menu()