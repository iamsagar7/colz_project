import tkinter as tk
LARGE_FONT=("Verdana",13)
class SeaofBTCapp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container=tk.Frame(self)

        container.pack(side="top",fill="both",expand=True)
        #weight =prioity 0=minframe
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
         
        self.frames={} #empty dictionary

        frame=StartPage(container,self)

        self.frames[StartPage]=frame
        frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage) 
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()
class StartPage(tk.Frame):
    def __init__(self,parent,container):
        tk.Frame.__init__(self,parent)
        label =tk.Label(self,text="start page",font=LARGE_FONT)
        label.pack(pady=10,padx=10)


app=SeaofBTCapp()
app.mainloop()