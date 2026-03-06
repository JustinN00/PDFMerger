import tkinter
from tkinter.filedialog import askopenfilenames, askdirectory
from pdf_merger import PDFMerger
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class PDFGui:
    def __init__(self) -> None:
        self.import_files = []
        self.export_directory = ""

        root = tkinter.Tk()
        root.title("Agarthan PDF Merger")

        root.iconbitmap(resource_path("Agarthan.ico"))
        bg = tkinter.PhotoImage(file=resource_path("Agarthan.png"))
        canvas = tkinter.Canvas(root, width=800, height=500)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0,0, image=bg, anchor="nw")

        import_files_button = tkinter.Button(text="Select PDFs", command = self.set_import_files)
        export_location_button = tkinter.Button(text="Select Export Folder", command = self.set_export_directory)
        go_button = tkinter.Button(text="Merge", command = self.merge_files)

        import_files_button.pack()
        export_location_button.pack()
        go_button.pack()

        root.mainloop()

    def set_import_files(self) -> None:
        self.import_files = askopenfilenames()

    def set_export_directory(self) -> None:
        self.export_directory = askdirectory()
    
    def merge_files(self) -> None:
        if not self.import_files or not self.export_directory:
            return
        
        merger = PDFMerger()
        merger.merge_files(self.export_directory, import_files = self.import_files)

if __name__ == "__main__":
    PDFGui()