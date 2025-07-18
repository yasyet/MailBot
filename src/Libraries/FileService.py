
# --//[LIBRARY IMPORTS]\\--
import tkinter as tk
from tkinter import filedialog

# --//[FILE FUNCTIONS]\\--
def askOpenFile():
    root = tk.Tk()
    root.withdraw()

    filePath = filedialog.askopenfilename(
        title="Select a file to open",
        filetypes=[("CSV files", "*.csv")]
    )
    
    if filePath:
        return filePath
    else:
        raise FileNotFoundError("No file selected.")
