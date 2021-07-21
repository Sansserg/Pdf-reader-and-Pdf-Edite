import tkinter as tk
from tkinter import ttk
import PyPDF2               # python 3
from tkinter import font as tkfont  # python 3
from tkinter import messagebox
from tkinter.filedialog import askopenfile #ptext version == 1.8.7.
from ptext.pdf.document import Document #ptext version == 1.8.7.
from ptext.pdf.page.page import Page    #ptext version == 1.8.7.
from ptext.pdf.pdf import PDF   #ptext version == 1.8.7.
from ptext.pdf.canvas.layout.paragraph import Paragraph #ptext version == 1.8.7.
from ptext.pdf.canvas.layout.page_layout import SingleColumnLayout  #ptext version == 1.8.7.
from ptext.io.read.types import Decimal #ptext version == 1.8.7.
from PIL import Image
from PIL import ImageTk
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.geometry("600x500")
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Choose what you need", font="Courier 60") ##########
        tk.Label(self, text="Choose what you need").pack(side="top", fill="x", pady=20)

        button1 = tk.Button(self, text="Pdf Reader", font="Courier 15",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Pdf Editor", font="Courier 15",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()





class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button_text = tk.StringVar()
        label = tk.Label(self, text = "Welcome to my pdf reader. \n Choose your file", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        def open_file():
            button_text.set("Loading")
            file = askopenfile (parent = self, mode= 'rb', title = "Chose your file", filetypes = [("Pdf file", "*.pdf")])
            if file:
                button_text.set("Sucessfuly")
                read_pdf = PyPDF2.PdfFileReader(file)
                page = read_pdf.getPage(0)
                page_content = page.extractText()
                #text box
                text_box = tk.Text(self, height=10, width=50, padx=15, pady=15)
                text_box.insert(1.0, page_content)
                text_box.tag_configure("center", justify="center")
                text_box.tag_add("center", 1.0, "end")
                text_box.pack(side="top", fill="x", pady=10)
                button_text.set("Browse")
        button = tk.Button(self, textvariable = button_text, command=lambda:open_file())
        button_text.set("Browse")
        button1 = tk.Button(self, text="back", command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button.pack()




class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller




        comboExample = ttk.Combobox(self, 
                                    values=["courier","courier-bold",
                                    "courier-bold-oblique","courier-oblique",
                                    "helvetica","helvetica-bold",
                                    "helvetica-bold-oblique","helvetica-oblique",
                                    "symbol", "times-bold",
                                    "times-bold-italic", "times-italic",
                                    "times-roman", "zapfdingbats",
                                    "Polaris-Regular", "Sverdlovsk"])

        
        vfont_name = 0
        def acccept():
            global vfont_name
            font_name = comboExample.get()
            if font_name == "courier":
                vfont_name = "courier"
            if font_name == "courier-bold":
                vfont_name = "courier-bold"
            if font_name == "courier-bold-obliqu":
                vfont_name = "courier-bold-obliqu"
            if font_name == "courier-oblique":
                vfont_name = "courier-oblique"
            if font_name == "helvetica":
                vfont_name = "helvetica"            
            if font_name == "helvetica-bold":
                vfont_name = "helvetica-bold"
            if font_name == "helvetica-bold-oblique":
                vfont_name = "helvetica-bold-oblique"
            if font_name == "helvetica-oblique":
                vfont_name = "helvetica-oblique"
            if font_name == "Polaris-Regular":
                vfont_name = "Polaris-Regular"            
            if font_name == "symbol":
                vfont_name = "symbol"
            if font_name == "times-bold":
                vfont_name = "times-bold"
            if font_name == "times-bold-italic":
                vfont_name = "times-bold-italic"
            if font_name == "times-italic":
                vfont_name = "times-italic"
            if font_name == "times-roman":
                vfont_name = "times-roman"
            if font_name == "zapfdingbats":
                vfont_name = "zapfdingbats"
            if font_name == "Sverdlovsk":
                vfont_name = "Sverdlovsk"


        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)




        button = tk.Button(self, text="start program",
                           command=lambda:pdf_ed())
        button1 = tk.Button(self, text="back", command=lambda: controller.show_frame("StartPage"))
        
        
        message = tk.StringVar()
        message_entry = tk.Entry(self, textvariable=message)
        message_entry.pack(side="top", fill="x", pady=10)
        name_file = tk.StringVar()
        name_file_entry = tk.Entry(self, textvariable=name_file)
        name_file_entry.pack(side="top", fill="x",padx= 250)


        bt1= tk.Button(self, text = "accept font",command=lambda:acccept())
        bt1.pack(side="bottom", pady=10)
        comboExample.pack(side="bottom", fill="x", pady=10)
        comboExample.current(1)
        text_label = tk.Label(self, text="choose font", font=controller.title_font)
        text_label.pack(side="bottom", fill="x", pady=10)









        def pdf_ed():
            global vfont_name
            document = Document()
            page = Page()
            layout = SingleColumnLayout(page)
            layout.add(Paragraph(message.get(), font_size=Decimal(20), font = vfont_name))
        
            document.append_page(page)
        
            with open(name_file.get(), "wb") as pdf_file_handle:
                PDF.dumps(pdf_file_handle, document)
        
        button.pack()
        button1.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()