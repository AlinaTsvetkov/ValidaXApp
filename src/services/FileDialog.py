from tkinter.filedialog import askopenfilename

class FileDialog:
    @staticmethod
    def getFileContent() -> str:
        fileContent = None
        filePath = askopenfilename(
            title="Search any TXT File to validate its content",
            filetypes=[
                ("TXT Files", "*.txt"),
            ],
        )

        with open(file=filePath, mode="r", encoding="utf-8") as file:
            fileContent = file.read()

        return fileContent.split()