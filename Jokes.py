from tkinter import *
import pyjokes

class Jokes:
    def __init__(self,root):
        self.root=root
        self.root.title("JOKES")
        self.root.geometry("510x300")
        self.root.resizable('0','0')
       # self.root.iconbitmap("happy.ico")


        #=================================================

        def on_enter1(e):
            generatejokes['background']="black"
            generatejokes['foreground']="cyan"
  
        def on_leave1(e):
            generatejokes['background']="SystemButtonFace"
            generatejokes['foreground']="SystemButtonText"


        def on_enter2(e):
            clear['background']="black"
            clear['foreground']="cyan"
  
        def on_leave2(e):
            clear['background']="SystemButtonFace"
            clear['foreground']="SystemButtonText"

        
        def clear():
            Txt.delete('1.0',END)


        def jokesgenerate():
            Txt.delete('1.0',END)
            global joke
            joke=pyjokes.get_joke()
            Txt.insert(END,joke)





        Mainframe=LabelFrame(self.root,text="Jokes of the day",font=("times new roman",14,'bold'),width=509,height=300,bg="#7777ff",fg="black")
        Mainframe.place(x=1,y=0)

        Txt=Text(Mainframe,font=('times new roman',12,'bold'),width=62,height=10,fg="cyan",bg="#3b3b3b",bd=3)
        Txt.place(x=1,y=0)

        generatejokes=Button(Mainframe,text="Jokes",width=12,font=('times new roman',11,'bold'),relief=RIDGE,bd=2,cursor="hand2",command=jokesgenerate)
        generatejokes.place(x=60,y=220)
        generatejokes.bind("<Enter>",on_enter1)
        generatejokes.bind("<Leave>",on_leave1)

        clear=Button(Mainframe,text="Clear",width=12,font=('times new roman',11,'bold'),relief=RIDGE,bd=2,cursor="hand2",command=clear)
        clear.place(x=330,y=220)
        clear.bind("<Enter>",on_enter2)
        clear.bind("<Leave>",on_leave2)


    
        



if __name__ == "__main__":
    root=Tk()
    app=Jokes(root)
    root.mainloop()
