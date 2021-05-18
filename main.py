from tkinter import *
names = []

class Quiz:
    def __init__(self, parent):
 
        background_color="light cyan"
       
      
        self.quiz_frame=Frame(bg = background_color, padx=200, pady=200)
        
        self.quiz_frame.grid()#The purose of this is too make sure the widgets are organised.
               
        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="Python Quiz Test", font=("san serif","14",),bg=background_color)
        self.heading_label.grid(row=50, padx=50) 
        
        
        
        self.user_label=Label(self.quiz_frame, text="Enter First name below:", font=("san serif","14"),bg=background_color)
        self.user_label.grid(padx=20, pady=20) 
        
        
        self.entry_box=Entry(self.quiz_frame)     
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        #Over here im creating a button widget to show the continue button on my application.
        self.continue_button =Button(self.quiz_frame, text="Resume", font=("san serif", "13",), bg="", command=self.name_collection)
        self.continue_button.grid(row=3,  padx=17, pady=17)        
        
        
       

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) 
        self.continue_button.destroy()
        self.entry_box.destroy() 
      
           

if __name__ == "__main__":
    root = Tk()
    root.title("Python Quiz Test") 

    quiz_instance = Quiz(root) 
    root.mainloop()
 
    
