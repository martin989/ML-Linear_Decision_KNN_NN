from Assignment10.Form import Form
from Assignment10.Data import Data
from tkinter import *


def main():
    file_name = "Dataset.csv"
    data = Data(file_name)
    root = Tk()
    form = Form(root, data)
    root.mainloop()


if __name__ == '__main__':
    main()
