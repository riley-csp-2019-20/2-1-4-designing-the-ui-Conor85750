import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.title("Authentication")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid()

lbl_username = tk.Label(frame_login, text='Username:',font="Courier")
lbl_username.pack(padx=50)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text='Password:',font="Courier")
lbl_password.pack(padx=50)

ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)

def test_button():
    print("clicked")
    frame_auth.tkraise()
    password = ent_password.get()
    lbl_disply_pass.config(text = password)

button_login = tk.Button(frame_login, text="Login", command=test_button)
button_login.pack()

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

lbl_disply_pass = tk.Label(frame_auth, text = "test")
lbl_disply_pass.pack()

frame_login.tkraise()

root.mainloop()