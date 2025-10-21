import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PyPDF2 import PdfMerger, PdfReader
import os
from tkinter import simpledialog

class PageSelectionDialog(tk.Toplevel):
    def __init__(self, parent, filename, max_pages):
        super().__init__(parent)
        self.title(f"Select Pages - {os.path.basename(filename)}")
        self.geometry("200x150")
        
        self.pages = ""
        
        # Create and pack widgets
        label = ttk.Label(self, text="Enter page numbers/ranges (e.g., 1-3,5,7-9):")
        label.pack(pady=10)
        
        self.entry = ttk.Entry(self)
        self.entry.pack(pady=5)
        
        info_label = ttk.Label(self, text=f"Total pages in PDF: {max_pages}")
        info_label.pack(pady=5)
        
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="OK", command=self.ok_clicked).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Cancel", command=self.cancel_clicked).pack(side=tk.LEFT, padx=5)
        
        self.transient(parent)
        self.grab_set()
        
    def ok_clicked(self):
        self.pages = self.entry.get()
        self.destroy()
        
    def cancel_clicked(self):
        self.pages = ""
        self.destroy()

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger by asif")
        self.root.geometry("600x400")
        self.page_selections = {}
        
        # Configure rainbow theme
        self.root.configure(bg="#C7B7BF")  # Hot pink background
        
        # Create custom buttons instead of ttk for better color control
        self.button_styles = {
            'add': {'bg': '#77DD77', 'fg': 'white', 'activebackground': '#66CC66'},  # Green
            'remove': {'bg': "#5E4040", 'fg': 'white', 'activebackground': '#EE5555'},  # Red
            'clear': {'bg': '#FFB347', 'fg': 'white', 'activebackground': '#EEA236'},  # Orange
            'merge': {'bg': '#87CEEB', 'fg': 'white', 'activebackground': '#76BDD9'}   # Sky blue
        }
        
        # Configure ttk style for frames and labels
        style = ttk.Style()
        style.configure('TFrame', background='#FF69B4')
        style.configure('TLabelframe', background='#FF69B4', foreground='white')
        style.configure('TLabelframe.Label', background='#FF69B4', foreground='white')
        
        # List to store PDF files
        self.pdf_files = []
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # File list frame
        list_frame = ttk.LabelFrame(self.root, text="Selected PDF Files")
        list_frame.pack(padx=10, pady=5, fill="both", expand=True)
        
        # Listbox to display selected files
        self.file_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, 
                                    bg='#FFF0F5', fg='#333333', selectbackground='#FF69B4',
                                    selectforeground='white', highlightbackground='#FF1493',
                                    highlightcolor='#FF69B4')
        self.file_listbox.pack(padx=5, pady=5, fill="both", expand=True)
        
        # Buttons frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(padx=10, pady=5, fill="x")
        
        # Add files button
        add_button = tk.Button(button_frame, text="Add PDF Files", command=self.add_files,
                           **self.button_styles['add'])
        add_button.pack(side="left", padx=5)
        
        # Remove selected button
        remove_button = tk.Button(button_frame, text="Remove Selected", command=self.remove_selected,
                              **self.button_styles['remove'])
        remove_button.pack(side="left", padx=5)
        
        # Clear all button
        clear_button = tk.Button(button_frame, text="Clear All", command=self.clear_all,
                             **self.button_styles['clear'])
        clear_button.pack(side="left", padx=5)
        
        # Merge button
        merge_button = tk.Button(button_frame, text="Merge PDFs", command=self.merge_pdfs,
                             **self.button_styles['merge'])
        merge_button.pack(side="right", padx=5)
        
    def add_files(self):
        files = filedialog.askopenfilenames(
            title="Select PDF Files",
            filetypes=[("PDF files", "*.pdf")]
        )
        for file in files:
            if file not in self.pdf_files:
                try:
                    # Get number of pages in PDF
                    reader = PdfReader(file)
                    num_pages = len(reader.pages)
                    
                    # Show page selection dialog
                    dialog = PageSelectionDialog(self.root, file, num_pages)
                    self.root.wait_window(dialog)
                    
                    # If pages were selected (not cancelled)
                    if dialog.pages:
                        self.pdf_files.append(file)
                        self.page_selections[file] = dialog.pages
                        filename = os.path.basename(file)
                        display_text = f"{filename} (Pages: {dialog.pages})"
                        self.file_listbox.insert(tk.END, display_text)
                except Exception as e:
                    messagebox.showerror("Error", f"Error reading PDF file: {str(e)}")
                
    def remove_selected(self):
        try:
            selection = self.file_listbox.curselection()[0]
            self.file_listbox.delete(selection)
            self.pdf_files.pop(selection)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a file to remove")
            
    def clear_all(self):
        self.file_listbox.delete(0, tk.END)
        self.pdf_files.clear()
        
    def parse_page_ranges(self, range_string, max_pages):
        pages = []
        ranges = range_string.split(',')
        
        for r in ranges:
            r = r.strip()
            if '-' in r:
                start, end = map(int, r.split('-'))
                if 1 <= start <= end <= max_pages:
                    pages.extend(range(start-1, end))
            else:
                page = int(r)
                if 1 <= page <= max_pages:
                    pages.append(page-1)
        
        return sorted(list(set(pages)))  # Remove duplicates and sort
    
    def merge_pdfs(self):
        if len(self.pdf_files) < 2:
            messagebox.showwarning("Warning", "Please select at least 2 PDF files to merge")
            return
            
        output_file = filedialog.asksaveasfilename(
            title="Save Merged PDF",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        
        if output_file:
            try:
                merger = PdfMerger()
                for pdf in self.pdf_files:
                    reader = PdfReader(pdf)
                    max_pages = len(reader.pages)
                    
                    # Get selected pages for this PDF
                    page_range = self.page_selections.get(pdf, "")
                    if page_range:
                        try:
                            pages = self.parse_page_ranges(page_range, max_pages)
                            merger.append(pdf, pages=pages)
                        except (ValueError, IndexError) as e:
                            messagebox.showerror("Error", f"Invalid page range for {os.path.basename(pdf)}")
                            return
                    else:
                        merger.append(pdf)  # If no selection, include all pages
                    
                merger.write(output_file)
                merger.close()
                messagebox.showinfo("Success", "PDFs merged successfully!")
                
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while merging PDFs:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
