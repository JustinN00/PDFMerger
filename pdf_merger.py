from pypdf import PdfWriter
import os


class PDFMerger: 
    def merge_files(self, export_directory: str, import_directory: str | None = None, import_files: list[str] | None = None):

        merger = PdfWriter()

        if import_directory:
            for file in os.listdir(import_directory):
                if ".pdf" not in file:
                    continue
                merger.append(f"{import_directory}\\{file}")
        elif import_files:
            print('hi')
            for file in [i for i in import_files if ".pdf" in i]:
                merger.append(file)
        else:
            raise ValueError("Must provide an import directory or import files...")
        
        merger.write(export_directory + "\\merged.pdf")


if __name__ == "__main__":
    pass
               