from tkinter import *
from tkinter import ttk
from Chat import getResponse, bot_name


BG_GRAY="#ABB2B9"
BG_COLOR="#000"
TEXT_COLOR="#FFF"
FONT="Helvetica 14"
FONT_BOLD="Helvetica 13 bold"

class ChatBot:
    def __init__(self):
        #initialize tkinter window
        self.window=Tk()
        self.main_window()
        
    #run window
    def run(self):
        self.window.mainloop()

    
    def main_window(self):
        #add title to window and configure it
        self.window.title("ChatBot")
        self.window.resizable(width=False,height=False)
        self.window.configure(width=1000 ,height=550,bg=BG_COLOR)
        self.add_bot()
        
        
        
    def add_bot(self):
        #Add heading to the Chabot window
        head_label=Label(self.window,bg=BG_COLOR,fg=TEXT_COLOR,text="Welcome to Sukkur IBA Universty",font=FONT_BOLD,pady=10)
        head_label.place(relwidth=1)

        # #divider
        line= Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1,rely=0.07, relheight=0.012)


        # # area where we display the text
        self.text_widget=Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5 ,pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow",state=DISABLED)

        # #create scrollbar
        # scrollbar=Scrollbar(self.text_widget)
        # scrollbar.place(relheight=1,relx=0.974)
        # scrollbar.configure(command=self.text_widget.yview)


        #bottom label
        bottom_label=Label(self.window,bg=BG_GRAY,height=80)
        bottom_label.place(relwidth=1,rely=0.825)

        #message entry box
        self.msg_entry=Entry(bottom_label,bg="#2C3E50",fg=TEXT_COLOR,font=FONT)
        self.msg_entry.place(relwidth=0.74,relheight=0.06,rely=0.008,relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self.on_enter)

        #send button which will call on_enter function to send the query
        send_button=Button(bottom_label,text="Send",font=FONT_BOLD,width=8,bg="Green",command=lambda: self.on_enter(None))
        send_button.place(relx=0.77,rely=0.008,relheight=0.06,relwidth=0.22)
        
    def on_enter(self,event):
        #get user query and bot response
        msg=self.msg_entry.get()
        self.my_msg(msg,"You")
        # self.bot_response(msg,"Bot")


    def my_msg(self,msg,sender):
        #it will display user query and bot response in text_widget
        if not msg:
            return

        self.msg_entry.delete(0,END)
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,str(sender)+" : "+str(msg)+"\n\n")
        self.text_widget.configure(state=DISABLED)

        self.msg_entry.delete(0,END)
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,str(bot_name)+" : "+str(getResponse(msg))+"\n\n")
        self.text_widget.configure(state=DISABLED)


        self.text_widget.see(END)

if __name__=="__main__":
    app = ChatBot()
    app.run()