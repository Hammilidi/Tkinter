from asyncio.windows_events import NULL
from fileinput import filename
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab


class Paint:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.root.geometry("800x520")
        self.root.configure(background="white")
        self.root.resizable(0, 0)

        # self.root.iconbitmap("icon.ico")

        image_icon = PhotoImage(file="logo.png")
        self.root.iconphoto(False, image_icon)
        # imp things...
        self.current_x = 0
        self.current_y = 0

        self.pen_color = 'black'
        self.eraser_color = "white"

        # creating canvas------------------------------

        self.canvas = Canvas(self.root, bg="white", bd=5,
                             relief=GROOVE, height=500, width=700)
        self.canvas.place(x=80, y=0)
        # adding widgets to tkinter  window-----------------------

        self.color_frame = LabelFrame(self.root, text="Color", font=(
            'cambria', 16), bd=5, relief=RIDGE, bg="white")
        self.color_frame.place(x=0, y=0, width=70, height=185)  # type: ignore

        colors = ['#ff0000', '#ff4dd2', '#ffff33',
                  '#000000', '#0066ff', '#660033', '#4dff4d', '#b300b3', '#0000ff', '#808080', '#99ffcc', '#336600', '#ff9966', '#ff0000', '#ff99ff', '#00cc99']

        i = j = 0
        for color in colors:
            Button(self.color_frame, bg=color, bd=2, width=3,
                   relief=RIDGE, command=lambda col=color: select_color(col)).grid(row=i, column=j)  # type: ignore
            i += 1
            if i == 6:
                i = 0
                j = 1
        # ---toutes les fonctions ------------------------------

        def paint(work):
            global current_x, current_y

            self. canvas.create_line((current_x, current_y, work.x, work.y), width=self.pen_size.get(
            ), fill=self.pen_color, capstyle=ROUND, smooth=TRUE)
            current_x, current_y = work.x, work.y
        # ------------------------------------

        def locate_xy(work):

            global current_x, current_y

            current_x = work.x
            current_y = work.y

        def select_color(col):
            self.pen_color = col

        def eraser():
            self.pen_color = self.eraser_color

        def canvas_color():
            color = colorchooser.askcolor
            self.canvas.configure(background=self.pen_color)  # type: ignore
            self.eraser_color = self.pen_color  # type: ignore

        def save_paint():
            try:
                filename = filedialog.asksaveasfilename(
                    defaultextension='.jpg')
                print(filename)

                x = self.root.winfo_rootx() + self.canvas.winfo_x()
                print(x)

                y = self.root.winfo_rooty() + self.canvas.winfo_y()
                print(y)

                x1 = x + self.canvas.winfo_width()
                print(x1)

                y1 = y + self.canvas.winfo_height()
                print(y1)

                ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
                messagebox.showinfo(
                    'paint says', 'image is saved as '+str(filename))

            except:
                print("Not saved something went wrong")
        # -------------------------------------------------------

        self.eraser_button = Button(self.root, text="ERASER", bd=4,
                                    relief=RIDGE, width=8, command=eraser, bg="white")  # type: ignore
        self.eraser_button.place(x=0, y=187)

        self.clear_button = Button(self.root, text="CLEAR", bd=4, relief=RIDGE,
                                   width=8, command=lambda: self.canvas.delete("all"), bg="white")  # type: ignore
        self.clear_button.place(x=0, y=217)

        self.save_button = Button(self.root, text="SAVE", bd=4, relief=RIDGE,
                                  width=8, command=save_paint, bg="white")  # type: ignore
        #self.eraser_button.place(x=0, y=247)
        self.save_button.place(x=0, y=157)

        self.canvas_color_button = Button(self.root, text="CANVAS", bd=4, relief=RIDGE,
                                          width=8, command=canvas_color, bg="white")  # type: ignore
        self.canvas_color_button.place(x=0, y=250)
        # ---liste des pen_types
        #choices = ['____', '----']
        #pen_type = StringVar(root)
        # pen_type.set('____')

        #w = OptionMenu(root, pen_type, *choices)
        # w.place(x=0,y=280)

        # creating a scale for pen and eraser size...

        self.pen_size_scale_frame = LabelFrame(
            self.root, text="size", bd=5, bg="white", font=("arial", 15, "bold"), relief=RIDGE)
        self.pen_size_scale_frame.place(x=0, y=310, height=200, width=70)

        self.pen_size = Scale(self.pen_size_scale_frame,
                              orient=VERTICAL, from_=50, to=0, length=70)
        self.pen_size.set(1)
        self.pen_size.grid(row=0, column=1, padx=15)

        # bind the canvas with mouse drag

        self.canvas.bind("<B1-Motion>", paint)  # type: ignore

        self.canvas.bind('<Button-1>', locate_xy)
        # Functions are defined here


if __name__ == "__main__":
    root = Tk()
    p = Paint(root)
    root.mainloop()
