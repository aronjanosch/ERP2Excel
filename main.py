import tkinter as tk
from tkinter import filedialog
import XlsWriter


class App(tk.Frame):

    idnum = None
    token = None
    valid_i = False
    valid_o = False


    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.master.title("ERP to Excel Tool")

        self.message = tk.StringVar()

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)

        self.id_label = tk.Label(master, text="ID: ")
        self.token_label = tk.Label(master, text="Token: ")
        self.message_label = tk.Label(master, textvariable=self.message)

        self.id_entry = tk.Entry(master)
        self.token_entry = tk.Entry(master)

        self.i_path_button = tk.Button(master, width=8, text="Vorlage File", command=lambda: self.get_input_path())
        self.o_path_button = tk.Button(master, width=8, text="Speicherort", command=lambda: self.get_output_path())

        self.go_button = tk.Button(master, width=17, text="GO!", command=lambda: self.run_tool())

        # LAYOUT

        self.id_label.grid(row=0, column=0, sticky='W')
        self.id_entry.grid(row=1, columnspan=2,)

        self.token_label.grid(row=2, column=0, sticky='W')
        self.token_entry.grid(row=3, columnspan=2,)

        self.i_path_button.grid(row=4, column=0)
        self.o_path_button.grid(row=4, column=1)
        self.message_label.grid(row=5,columnspan=2)
        self.go_button.grid(row=6, columnspan=2)

    def placeholder(self):
        pass

    def get_input_path(self):
        self.ipath = tk.filedialog.askopenfilename(initialdir = "/Users/aronwiederkehr/Desktop/", defaultextension=".xlsx", title = "Select xlsx file",filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
        self.message.set("Import File set!")
        self.valid_i = True

    def get_output_path(self):
        self.opath = tk.filedialog.asksaveasfilename(initialdir = "/Users/aronwiederkehr/Desktop/", defaultextension=".xlsx", title = "Save xlsx file",filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
        self.message.set("Export File set!")
        self.valid_o = True

    def run_tool(self):
        if self.valid_i is True and self.valid_o is True:
            self.run_xlstool(self.ipath, self.opath)
        else:
            self.message.set("Please select import and export File")

    def run_xlstool(self, input_path, output_path):
        idmun = self.id_entry.get()
        if idmun:
            result = XlsWriter.get_items(idmun)
            if type(result) == int:
                self.message.set("Error {res}".format(res=result))
            else:
                XlsWriter.write_xlsx(input_path, output_path, result[0], result[1])
                self.message.set("Success")
        else:
            self.message.set("Please type smthing")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
