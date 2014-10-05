from Tkinter import *
import ImageTk, cPickle, glob
from PIL import Image
class App( Frame ):
     
    def __init__( self, parent ):
         
        Frame.__init__( self, parent )
                 
        self.parent = parent
        self.parent.grid()
         
        self.train = dict()
        self.i = 0
        self.fns = glob.glob("*.jpeg")
         
        ## start up the UI
        self.initUI()
         
    def initUI( self ):
         
        ## set the key bindings for the Enter key, and the keypad Enter key
        self.parent.bind( '<Return>', self.submit_callback )
        self.parent.bind( '<KP_Enter>', self.submit_callback )
         
        ## name of the program
        self.parent.title( "Label Training Data" )
              
        ## open the image
        image = Image.open( self.fns[ self.i ] )
        photo = ImageTk.PhotoImage( image, master=self )
         
        ## put the image in a Label object
        img_label = Label( self, image=photo )
        img_label.image = photo
        img_label.grid(row=0,columnspan=2)
             
        ## entry
        ent_label = Label( self, text="Label:" )
        ent_label.grid( row=1, column=0 )
        self.entry = Entry( self )
        self.entry.grid( row=1, column=1 )
        self.entry.focus()
             
        ## submit button
        submit_btn = Button( self, text="Submit" )
        submit_btn.bind( '<Button-1>', self.submit_callback )
        submit_btn.grid( row=2, columnspan=2 )
         
        ## quit button
        quit_btn = Button( self, text="Save and Quit", command=self.quit_callback )
        quit_btn.grid( row=3, columnspan=2 )
              
        ## pack it up
        self.pack()
         
    def submit_callback( self, event=None ):
        ## associate the user input with the filename
        self.train[ self.fns[ self.i ] ] = self.entry.get()
        ## increment the counter
        self.i += 1
        ## if we're at the end of the data..
        if self.i == len( self.fns ):
            ## save/dump the data
            cPickle.dump( self.train, open( "train_complete.pkl", "w" ), -1 )
            ## kill the aplication
            self.parent.destroy()
        ## reload the window
        self.initUI()
         
    def quit_callback( self ):
        ## save/dump the data
        cPickle.dump( self.train, open( "train_partial.pkl", "w" ), -1 )
        ## kill the aplication
        self.parent.destroy()

def main():
    root = Tk()
    root.geometry("1000x1400+2800+1400")
    app = App( root )
    root.mainloop()
 
if __name__=="__main__":
    main()
