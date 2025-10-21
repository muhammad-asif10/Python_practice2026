import tkinter as tk
from tkinter import ttk, messagebox, filedialog, font, simpledialog
import json
import os
from datetime import datetime

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Notes")
        self.root.geometry("1000x600")
        
        # Configure modern Windows 11 theme colors
        self.colors = {
            'bg': '#FFFFFF',
            'text_bg': '#FAFAFA',
            'text_fg': '#202020',
            'button_bg': '#F0F0F0',
            'button_fg': '#202020',
            'highlight': '#0078D4',
            'border': '#E6E6E6',
            'hover': '#ECF6FD'
        }
        
        # Configure root
        self.root.configure(bg=self.colors['bg'])
        
        # Initialize notes storage
        self.notes = {}
        self.current_note = None
        
        # Load existing notes
        self.notes_dir = "notes"
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)
            
        # Create the UI
        self.create_menu()
        self.create_widgets()
        self.load_notes()
        
    def create_menu(self):
        # Create main menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Note", command=self.new_note)
        file_menu.add_command(label="Save", command=self.save_note)
        file_menu.add_command(label="Delete", command=self.delete_note)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=lambda: self.text_editor.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text_editor.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text_editor.event_generate("<<Paste>>"))
        
        # Format menu
        format_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Format", menu=format_menu)
        format_menu.add_command(label="Bold", command=self.toggle_bold)
        format_menu.add_command(label="Italic", command=self.toggle_italic)
        format_menu.add_command(label="Underline", command=self.toggle_underline)
        
    def create_widgets(self):
        # Create main container
        main_container = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Left panel for notes list
        left_panel = ttk.Frame(main_container, style='Modern.TFrame')
        main_container.add(left_panel, weight=1)
        
        # Search frame
        search_frame = ttk.Frame(left_panel, style='Modern.TFrame')
        search_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Notes list with modern styling
        self.notes_list = tk.Listbox(left_panel, 
                                    bg=self.colors['text_bg'],
                                    fg=self.colors['text_fg'],
                                    selectbackground=self.colors['highlight'],
                                    selectforeground='white',
                                    font=('Segoe UI', 11),
                                    borderwidth=1,
                                    relief='solid',
                                    highlightthickness=0,
                                    activestyle='none')
        self.notes_list.pack(fill=tk.BOTH, expand=True)
        self.notes_list.bind('<<ListboxSelect>>', self.on_select_note)
        
        # Right panel for text editor
        right_panel = ttk.Frame(main_container)
        main_container.add(right_panel, weight=3)
        
        # Toolbar
        toolbar = ttk.Frame(right_panel)
        toolbar.pack(fill=tk.X, pady=5)
        
        # Modern font size selector
        ttk.Label(toolbar, text="Size:").pack(side=tk.LEFT, padx=5)
        
        self.font_size = ttk.Combobox(toolbar, 
                                     values=[8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72],
                                     width=5)
        self.font_size.set(11)
        self.font_size.pack(side=tk.LEFT, padx=5)
        self.font_size.bind('<<ComboboxSelected>>', self.change_font_size)
        
        # Modern style buttons
        style_frame = ttk.Frame(toolbar, style='Toolbar.TFrame')
        style_frame.pack(side=tk.LEFT, padx=10)
        
        # Create formatting buttons
        self.bold_button = tk.Button(style_frame, text="B", 
                                   font=('Segoe UI', 10, 'bold'),
                                   borderwidth=1,
                                   relief='solid',
                                   bg=self.colors['button_bg'],
                                   fg=self.colors['text_fg'],
                                   width=3,
                                   padx=10,
                                   pady=5,
                                   command=self.toggle_bold)
        self.bold_button.pack(side=tk.LEFT, padx=2)
        
        self.italic_button = tk.Button(style_frame, text="I",
                                     font=('Segoe UI', 10, 'italic'),
                                     borderwidth=1,
                                     relief='solid',
                                     bg=self.colors['button_bg'],
                                     fg=self.colors['text_fg'],
                                     width=3,
                                     padx=10,
                                     pady=5,
                                     command=self.toggle_italic)
        self.italic_button.pack(side=tk.LEFT, padx=2)
        
        self.underline_button = tk.Button(style_frame, text="U",
                                        font=('Segoe UI', 10, 'underline'),
                                        borderwidth=1,
                                        relief='solid',
                                        bg=self.colors['button_bg'],
                                        fg=self.colors['text_fg'],
                                        width=3,
                                        padx=10,
                                        pady=5,
                                        command=self.toggle_underline)
        self.underline_button.pack(side=tk.LEFT, padx=2)
        
        # Add hover effect to buttons
        for button in [self.bold_button, self.italic_button, self.underline_button]:
            button.bind('<Enter>', lambda e, b=button: b.configure(bg=self.colors['hover']))
            button.bind('<Leave>', lambda e, b=button: b.configure(bg=self.colors['button_bg']))
        
        # Modern text editor
        editor_frame = ttk.Frame(right_panel, style='Modern.TFrame')
        editor_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        self.text_editor = tk.Text(editor_frame, 
                                wrap=tk.WORD,
                                bg=self.colors['text_bg'],
                                fg=self.colors['text_fg'],
                                insertbackground=self.colors['text_fg'],
                                font=('Segoe UI', 11),
                                relief='solid',
                                borderwidth=1,
                                padx=10,
                                pady=10,
                                selectbackground=self.colors['highlight'],
                                selectforeground='white')
        self.text_editor.pack(fill=tk.BOTH, expand=True)
        
    def new_note(self):
        # Create new note dialog
        title = simpledialog.askstring("New Note", "Enter note title:")
        if title:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.notes[title] = {
                'content': '',
                'created': timestamp,
                'modified': timestamp
            }
            self.save_notes()
            self.refresh_notes_list()
            # Select the new note
            idx = list(self.notes.keys()).index(title)
            self.notes_list.selection_clear(0, tk.END)
            self.notes_list.selection_set(idx)
            self.on_select_note(None)
            
    def save_note(self):
        if self.current_note:
            # Remove any trailing newlines from the content
            content = self.text_editor.get("1.0", "end-1c")
            self.notes[self.current_note] = {
                'content': content,
                'modified': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'created': self.notes[self.current_note].get('created', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            }
            try:
                self.save_notes()
                messagebox.showinfo("Success", "Note saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save note: {str(e)}")
            
    def delete_note(self):
        if self.current_note:
            if messagebox.askyesno("Confirm Delete", f"Delete note '{self.current_note}'?"):
                try:
                    del self.notes[self.current_note]
                    self.save_notes()
                    self.refresh_notes_list()
                    self.text_editor.delete("1.0", tk.END)
                    self.current_note = None
                    messagebox.showinfo("Success", "Note deleted successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Could not delete note: {str(e)}")
                    return
                
    def load_notes(self):
        try:
            notes_file = os.path.join(self.notes_dir, "notes.json")
            backup_file = notes_file + ".backup"
            
            # Try to load the main file
            if os.path.exists(notes_file):
                try:
                    with open(notes_file, 'r', encoding='utf-8') as f:
                        self.notes = json.load(f)
                    self.refresh_notes_list()
                    return
                except:
                    # If main file is corrupted, try backup
                    if os.path.exists(backup_file):
                        with open(backup_file, 'r', encoding='utf-8') as f:
                            self.notes = json.load(f)
                        # Restore backup to main file
                        os.replace(backup_file, notes_file)
                        self.refresh_notes_list()
                        messagebox.showwarning("Recovery", "Notes were restored from backup.")
                        return
            
            # If no files exist, start with empty notes
            self.notes = {}
            self.refresh_notes_list()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error loading notes: {str(e)}")
            self.notes = {}
            
    def save_notes(self):
        try:
            # Ensure notes directory exists
            if not os.path.exists(self.notes_dir):
                os.makedirs(self.notes_dir)
            
            notes_file = os.path.join(self.notes_dir, "notes.json")
            # Create backup of existing file
            if os.path.exists(notes_file):
                backup_file = notes_file + ".backup"
                try:
                    os.replace(notes_file, backup_file)
                except:
                    pass
            
            # Write new content
            with open(notes_file, 'w', encoding='utf-8') as f:
                json.dump(self.notes, f, indent=4, ensure_ascii=False)
            
            # Remove backup if save was successful
            if os.path.exists(backup_file):
                os.remove(backup_file)
                
        except Exception as e:
            messagebox.showerror("Error", f"Error saving notes: {str(e)}")
            # Try to restore from backup
            if os.path.exists(backup_file):
                try:
                    os.replace(backup_file, notes_file)
                except:
                    pass
            raise e
            
    def refresh_notes_list(self):
        self.notes_list.delete(0, tk.END)
        # Sort notes by most recently modified
        sorted_notes = sorted(
            self.notes.items(),
            key=lambda x: x[1].get('modified', ''),
            reverse=True
        )
        for title, _ in sorted_notes:
            self.notes_list.insert(tk.END, title)
            
    def on_select_note(self, event):
        if self.notes_list.curselection():
            title = self.notes_list.get(self.notes_list.curselection())
            self.current_note = title
            self.text_editor.delete("1.0", tk.END)
            self.text_editor.insert("1.0", self.notes[title]['content'])
            
    def toggle_bold(self):
        try:
            current_tags = self.text_editor.tag_names("sel.first")
            if "bold" in current_tags:
                self.text_editor.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.text_editor.tag_add("bold", "sel.first", "sel.last")
                current_size = self.font_size.get()
                self.text_editor.tag_configure("bold", font=('Segoe UI', int(current_size), 'bold'))
        except tk.TclError:
            pass
            
    def toggle_italic(self):
        try:
            current_tags = self.text_editor.tag_names("sel.first")
            if "italic" in current_tags:
                self.text_editor.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.text_editor.tag_add("italic", "sel.first", "sel.last")
                current_size = self.font_size.get()
                self.text_editor.tag_configure("italic", font=('Segoe UI', int(current_size), 'italic'))
        except tk.TclError:
            pass
            
    def toggle_underline(self):
        try:
            current_tags = self.text_editor.tag_names("sel.first")
            if "underline" in current_tags:
                self.text_editor.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.text_editor.tag_add("underline", "sel.first", "sel.last")
                current_size = self.font_size.get()
                self.text_editor.tag_configure("underline", font=('Segoe UI', int(current_size), 'underline'))
        except tk.TclError:
            pass
            
    def change_font_size(self, event=None):
        try:
            size = int(self.font_size.get())
            self.text_editor.tag_add("size", "sel.first", "sel.last")
            self.text_editor.tag_configure("size", font=('Segoe UI', size))
        except tk.TclError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
