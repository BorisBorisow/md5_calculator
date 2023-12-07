import tkinter as tk
from tkinter import filedialog, messagebox
import os
from md5_diff_checker import find_different_md5_sums  # Replace with the actual name of your script

class MD5SumsGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("MD5 Sums Checker")

        tk.Label(master, text="Original Directory:").grid(row=0, column=0)
        tk.Label(master, text="New Directory:").grid(row=1, column=0)

        self.original_entry = tk.Entry(master, width=50)
        self.original_entry.grid(row=0, column=1)

        self.new_entry = tk.Entry(master, width=50)
        self.new_entry.grid(row=1, column=1)

        tk.Button(master, text="Browse", command=self.browse_original).grid(row=0, column=2)
        tk.Button(master, text="Browse", command=self.browse_new).grid(row=1, column=2)

        tk.Button(master, text="Run", command=self.run_script).grid(row=2, column=1)
        tk.Button(master, text="Open Result", command=self.open_result).grid(row=3, column=1)

    def browse_original(self):
        original_directory = filedialog.askdirectory()
        self.original_entry.delete(0, tk.END)
        self.original_entry.insert(0, original_directory)

    def browse_new(self):
        new_directory = filedialog.askdirectory()
        self.new_entry.delete(0, tk.END)
        self.new_entry.insert(0, new_directory)

    def run_script(self):
        try:
            original_directory = self.original_entry.get()
            new_directory = self.new_entry.get()

            different_md5_sums = find_different_md5_sums(original_directory, new_directory)

            output_file_path = "different_md5_sums.txt"
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                for file_path, md5_sum in different_md5_sums.items():
                    file_name = os.path.basename(file_path)
                    output_file.write(f"{file_name}: {md5_sum}\n")

            messagebox.showinfo("Success", f"Different MD5 sums written to {output_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def open_result(self):
        try:
            output_file_path = "different_md5_sums.txt"
            os.system(f'start {output_file_path}')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MD5SumsGUI(root)
    root.mainloop()
