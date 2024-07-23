import tkinter
from tkinter import messagebox

file = 'new.txt'
clients = 'clients.txt'
accounts = []


class logInPrompt():
    global file
    global accounts
    def __init__(self):

        def load_value(file1):
            with open(file1, 'r') as f:
                read = f.read()
            return read

        def register():
            self.root.destroy()
            a = signUpPrompt()
            a.run()

        def signin():
            name = self.name_label_entry.get()
            password = self.password_entry.get()
            person = {'|  ' +'Name: ' + name + '   |   '+ 'Password: '+ password + '  |'}

            a = load_value(file)
            if str(person) not in a:
                messagebox.showerror('Error', 'Invalid log in details')
            else:
                messagebox.showinfo('success', 'Sign in successful')
                self.name_label_entry.delete(0, 'end')
                self.password_entry.delete(0, 'end')
                self.root.destroy()
                a = mainScreen()
                a.run()

        self.root = tkinter.Tk()
        self.root.geometry('400x500')
        self.root.resizable(False, False)
        self.label = tkinter.Label(self.root, text='Sign In', font=('Ink Free', 30, 'bold'))
        self.label.place(x=140, y=80)
        self.name_label = tkinter.Label(self.root, text='Name', font=('Ink Free', 10, 'bold'))
        self.name_label.place(x=100, y=180)
        self.name_label_entry = tkinter.Entry(self.root, relief='solid', width=25)
        self.name_label_entry.place(x=140, y=180)
        self.password_label = tkinter.Label(self.root, text='Password', font=('Ink Free', 10, 'bold'))
        self.password_label.place(x=65, y=230)
        self.password_entry = tkinter.Entry(self.root, relief='solid', width=25, show='*')
        self.password_entry.place(x=140, y=230)
        self.log_in_button = tkinter.Button(self.root, text='Sign in', command=signin)
        self.log_in_button.place(x=180, y=270)
        self.account_label = tkinter.Label(self.root, text="Don't have an account?", fg='blue')
        self.account_label.place(x=80, y=310)
        self.sign_up_button = tkinter.Button(self.root, text='sign up', border=0, command=register)
        self.sign_up_button.place(x=225, y=309)

    def run(self):
        self.root.mainloop()


class signUpPrompt():
    global accounts
    def __init__(self):

        def register():
            self.root.destroy()
            a = logInPrompt()
            a.run()

        def signup():

            name = self.name_label_entry.get()
            password = self.password_entry.get()
            conf_pass = self.confirm_password_label_entry.get()
            person = {'|  ' +'Name: ' + name + '   |   '+ 'Password: '+ password + '  |'}
            person2 = '|  ' + 'Name: ' + name + '   |   ' + 'Password: ' + password + '  |' + '\n'


            if password == conf_pass:
                with open(clients, 'a') as c:
                    c.write(str(person2))
                with open(file, 'a') as f:
                    f.write(str(person))

                    messagebox.showinfo('success', 'account registered')
                    self.name_label_entry.delete(0, 'end')
                    self.password_entry.delete(0, 'end')
                    self.confirm_password_label_entry.delete(0, 'end')

            else:
                messagebox.showerror('Error', "Passwords don't match")
                self.confirm_password_label_entry.delete(0, 'end')

        self.root = tkinter.Tk()
        self.root.geometry('400x500')
        self.root.resizable(False, False)
        self.label = tkinter.Label(self.root, text='Sign Up', font=('Ink Free', 30, 'bold'))
        self.label.place(x=140, y=80)
        self.rname_label = tkinter.Label(self.root, text='Name', font=('Ink Free', 10, 'bold'))
        self.rname_label.place(x=110, y=180)
        self.name_label_entry = tkinter.Entry(self.root, relief='solid', width=25)
        self.name_label_entry.place(x=170, y=180)
        self.password_label = tkinter.Label(self.root, text='Password', font=('Ink Free', 10, 'bold'))
        self.password_label.place(x=85, y=230)
        self.password_entry = tkinter.Entry(self.root, relief='solid', width=25, show='*')
        self.password_entry.place(x=170, y=230)
        self.confirm_password_label = tkinter.Label(self.root, text='Confirm password', font=('Ink Free', 10, 'bold'))
        self.confirm_password_label.place(x=30, y=280)
        self.confirm_password_label_entry = tkinter.Entry(self.root, relief='solid', width=25, show='*')
        self.confirm_password_label_entry.place(x=170, y=280)
        self.log_in_button = tkinter.Button(self.root, text='Sign up', command=signup)
        self.log_in_button.place(x=180, y=320)
        self.account_label = tkinter.Label(self.root, text='Already have an account?', fg='blue')
        self.account_label.place(x=110, y=370)
        self.sign_in_button = tkinter.Button(self.root, text='sign in', border=0, command=register)
        self.sign_in_button.place(x=255, y=369)

    def run(self):
        self.root.mainloop()

class mainScreen():
    global accounts
    def __init__(self):

        root = tkinter.Tk()
        root.geometry('800x500')
        root.configure(bg='green')

        display = tkinter.Label(root, font=('Ink Free',20), text='Congratulations, You have successfully signed in!', bg='green', fg='white')
        display.place(x=130, y=180)

        root.mainloop()

    def run(self):
        self.root.mainloop()






a = signUpPrompt()
a.run()
