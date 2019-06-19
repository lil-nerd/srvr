#!/usr/bin/python3

import tkinter as tk

class Chat_window():

    def __init__(self, name):

        window = tk.Tk()
        window.title("Chat#~" + str(name))
        window.geometry("500x500")

        chat = tk.Text(window)
        chat.pack()

        message_box = tk.Entry(window, width = 50)
        message_box.pack(side= 'left')

        send_btn = tk.Button(window, text = "Send")
        send_btn.pack(side= 'right')


        window.mainloop()


#    def show_new_msg(self):
