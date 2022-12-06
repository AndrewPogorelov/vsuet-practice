import json
import requests
from tkinter import*
def buttonAction():
    with open("file.txt","w") as file:
        user = txtField.get()
        url = f"https://api.github.com/users/{user}"
        userInfo = requests.get(url).json()
        enum = ['company', 'created_at', 'email', 'id', 'name', 'url']
        data = userInfo.keys()
        for i in data:
            if i in enum:
                file.write(f"{i}:{userInfo[i]}" + '\n')
    head.configure(text = "Выполнено")


root = Tk()
root.title('GIT request')
root.geometry('600x400')
root["bg"] ="grey"

head = Label(root, bg = "grey", fg = "black", text = 'Введите git', font = ('Franklin Gothic Medium', 20))
head.pack(expand=True)
txtField = Entry(root,width=20,font=('Franklin Gothic Medium', 20))
txtField.pack(expand=True)
button = Button(root, bg = "white", fg = "green", text = 'Сделать запрос',command = buttonAction)
button.pack(expand=True)

root.mainloop()
