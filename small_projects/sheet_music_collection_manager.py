# import relevant modules
import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from collections import Counter
import matplotlib.pyplot as plt

# define class: Piece
class Piece:
    def __init__(self, title, composer, time_period, instrumentation, difficulty):
        # initialise attributes of piece
        self.title = title
        self.composer = composer
        self.time_period = time_period
        self.instrumentation = instrumentation
        self.difficulty = difficulty

# define class: collection manager
class CollectionManager:
    def __init__(self):
        # create empty list to hold pieces
        self.pieces = []
    
    # add new piece to collection
    def add_piece(self, piece):
        self.pieces.append(piece)
    
    # remove piece by title
    def remove_piece(self, title):
        # filters out the piece with the given title
        self.pieces = [p for p in self.pieces if p.title != title]
    
    # edit piece in table by updating the attributes, pass variable number of arguments without saying each argument in list
    def edit_piece(self, title, **kwargs):
        for piece in self.pieces:
            if piece.title == title:
                # update piece's attributes with new values
                for key, value in kwargs.items():
                    if hasattr(piece, key): # has attribute
                        setattr(piece, key, value) # set attribute
                return True
        return False
    
    # sort collection based on specified attribute
    def sort_by(self, attribute):
        try:
            # sort pieces by given attribute (converted to string to have uniform sorting)
            self.pieces.sort(key=lambda piece: str(getattr(piece, attribute, '')).strip().lower())
        except Exception as e:
            print(f"Error during sorting: {e}")
    
    # displays collection
    def display_collection(self):
        for piece in self.pieces:
            print(piece)
    
    # imports collection data from a CSV file
    def import_from_csv(self, file_path):
        try:
            # open CSV file in read mode and utf-8 encoding because its a CSV and read contents
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                # check if 'title column exists in CSV file
                if not reader.fieldnames or 'title' not in reader.fieldnames:
                    raise ValueError("CSV file missing required 'title' column")
                # create Piece objects from the CSV rows and add to colection
                for row in reader:
                    piece = Piece(
                        title=row.get('title', '').strip(),
                        composer=row.get('composer', '').strip(),
                        time_period=row.get('time_period', '').strip(),
                        instrumentation=row.get('instrumentation', '').strip(),
                        difficulty=row.get('difficulty', '').strip()
                    )
                    self.add_piece(piece)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
        
    # export collection to CSV
    def export_to_csv(self, file_path):
        try:
            with open(file_path, mode='w', encoding='utf-8', newline='') as file:
                # write header and rows to CSV in same order so it can be reopened and used in this program
                writer = csv.DictWriter(file, fieldnames=['title', 'composer', 'time_period', 'instrumentation', 'difficulty'])
                writer.writeheader()
                for piece in self.pieces:
                    writer.writerow({
                        'title': piece.title,
                        'composer': piece.composer,
                        'time_period': piece.time_period,
                        'instrumentation': piece.instrumentation,
                        'difficulty': piece.difficulty
                    })
        except Exception as e:
            print(f"Error writing to CSV file: {e}")

# define class: main collection app with UI
class CollectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sheet Music Collection Manager")
        self.manager = CollectionManager()
        # create main frame for app
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        # create Treeview 'widget' to display collection
        self.tree = ttk.Treeview(self.main_frame, columns=("Title","Composer", "Time Period", "Instrumentation", "Difficulty"), show="headings")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Composer", text="Composer")
        self.tree.heading("Time Period", text="Time Period")
        self.tree.heading("Instrumentation", text="Instrumentation")
        self.tree.heading("Difficulty", text="Difficulty")
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # button frame to hold action buttons
        button_frame = ttk.Frame(self.main_frame, padding="10")
        button_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # buttons for every function I defined
        ttk.Button(button_frame, text="Add Piece", command=self.add_piece).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Edit Piece", command=self.edit_piece).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Remove Piece", command=self.remove_piece).grid(row=0, column=2, padx=5)
        ttk.Button(button_frame, text="Import CSV", command=self.import_csv).grid(row=0, column=3, padx=5)
        ttk.Button(button_frame, text="Export CSV", command=self.export_csv).grid(row=0, column=4, padx=5)
        
        # sorting buttons
        ttk.Button(button_frame, text="Sort by Title", command=lambda: self.sort_by("title")).grid(row=1, column=0, padx=5)
        ttk.Button(button_frame, text="Sort by Composer", command=lambda: self.sort_by("composer")).grid(row=1, column=1, padx=5)
        ttk.Button(button_frame, text="Sort by Time Period", command=lambda: self.sort_by("time_period")).grid(row=1, column=2, padx=5)
        ttk.Button(button_frame, text="Sort by Difficulty", command=lambda: self.sort_by("difficulty")).grid(row=1, column=3, padx=5)
        ttk.Button(button_frame, text="Sort by Instrumentation", command=lambda: self.sort_by("instrumentation")).grid(row=1, column=4, padx=5)
        
        # buttons for visualising the data
        ttk.Button(button_frame, text="Dashboard", command=self.show_dashboard).grid(row=2, column=0, padx=5)
        ttk.Button(button_frame, text="Visualise Difficulty", command=self.visualise_difficulty).grid(row=2, column=1, padx=5)
        ttk.Button(button_frame, text="Visualise Time Periods", command=self.visualise_time_periods).grid(row=2, column=2, padx=5)
        ttk.Button(button_frame, text="Visualise Instrumentation", command=self.visualise_instrumentation).grid(row=2, column=3, padx=5)
        ttk.Button(button_frame, text="Visualize Top Composers", command=self.visualise_top_composers).grid(row=2, column=4, padx=5)
    
    # visualising function for difficulty
    def visualise_difficulty(self):
        difficulties = [piece.difficulty for piece in self.manager.pieces if piece.difficulty]
        if not difficulties:
            messagebox.showinfo("No Data", "No difficulty data available to visualise.")
            return

        plt.figure(figsize=(8, 6))
        plt.hist(difficulties, bins=range(1, 11), align='left', rwidth=0.8, color='skyblue', edgecolor='black')
        plt.title("Distribution of Pieces by Difficulty")
        plt.xlabel("Difficulty Level")
        plt.ylabel("Number of Pieces")
        plt.xticks(range(1, 11))
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
    
    # visualising function for time period distribution
    def visualise_time_periods(self):
        time_periods = [piece.time_period for piece in self.manager.pieces if piece.time_period]
        if not time_periods:
            messagebox.showinfo("No Data", "No time period data available to visualise.")
            return

        time_period_count = Counter(time_periods)
        time_period_labels = list(time_period_count.keys())
        time_period_values = list(time_period_count.values())

        plt.figure(figsize=(10, 6))
        plt.bar(time_period_labels, time_period_values, color='lightgreen', edgecolor='black')
        plt.title("Distribution of Pieces by Time Period")
        plt.xlabel("Time Period")
        plt.ylabel("Number of Pieces")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    
    # visualising function for instrument distribution
    def visualise_instrumentation(self):
        instrumentations = [piece.instrumentation for piece in self.manager.pieces if piece.instrumentation]
        if not instrumentations:
            messagebox.showinfo("No Data", "No instrumentation data available to visualise.")
            return

        instrumentation_count = Counter(instrumentations)
        labels = list(instrumentation_count.keys())
        sizes = list(instrumentation_count.values())

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.title("Distribution of Pieces by Instrumentation")
        plt.axis('equal')
        plt.show()
    
    # visualising function for top composers (top 10)
    def visualise_top_composers(self):
        composers = [piece.composer for piece in self.manager.pieces if piece.composer]
        if not composers:
            messagebox.showinfo("No Data", "No composer data available to visualise.")
            return

        composer_count = Counter(composers)
        top_composers = composer_count.most_common(10)
        names, counts = zip(*top_composers)

        plt.figure(figsize=(10, 6))
        plt.bar(names, counts, color='salmon', edgecolor='black')
        plt.title("Top 10 Composers by Number of Pieces")
        plt.xlabel("Composer")
        plt.ylabel("Number of Pieces")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    
    # function to show summary dashboard
    def show_dashboard(self):
        composers = [piece.composer for piece in self.manager.pieces]
        summary = Counter(composers)
        total_pieces = len(self.manager.pieces)
        most_common_composer = summary.most_common(1)[0][0] if summary else "None"

        dashboard_window = tk.Toplevel(self.root)
        dashboard_window.title("Dashboard")
        dashboard_window.geometry("400x300")

        ttk.Label(dashboard_window, text=f"Total Pieces: {total_pieces}").pack(pady=10)
        ttk.Label(dashboard_window, text=f"Most Common Composer: {most_common_composer}").pack(pady=10)
    
    # function to sort by attribute
    def sort_by(self, attribute):
        self.manager.sort_by(attribute)
        self.update_table()
    
    # function to add piece including function to save piece to table
    def add_piece(self):
        def save_piece():
            title = title_entry.get()
            composer = composer_entry.get()
            time_period = time_period_entry.get()
            instrumentation = instrumentation_entry.get()
            difficulty = difficulty_entry.get()
            
            # validating inputs
            if not title or not composer:
                messagebox.showwarning("Input Error", "Title and Composer are required.")
                return
            # create new piece object with input data and add to collection
            piece = Piece(title, composer, time_period, instrumentation, difficulty)
            self.manager.add_piece(piece)
            self.update_table() # update table
            add_window.destroy()
        
        # create new window for entering piece details
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Piece")
        add_window.geometry("400x300") # set window size
        
        # create and position labels for each attribute
        ttk.Label(add_window, text="Title").grid(row=0, column=0, padx=10, pady=5)
        title_entry = ttk.Entry(add_window)
        title_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(add_window, text="Composer").grid(row=1, column=0, padx=10, pady=5)
        composer_entry = ttk.Entry(add_window)
        composer_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(add_window, text="Time Period").grid(row=2, column=0, padx=10, pady=5)
        time_period_entry = ttk.Entry(add_window)
        time_period_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(add_window, text="Instrumentation").grid(row=3, column=0, padx=10, pady=5)
        instrumentation_entry = ttk.Entry(add_window)
        instrumentation_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(add_window, text="Difficulty").grid(row=4, column=0, padx=10, pady=5)
        difficulty_entry = ttk.Entry(add_window)
        difficulty_entry.grid(row=4, column=1, padx=10, pady=5)
        
        # save button calling svae_piece function
        ttk.Button(add_window, text="Save", command=save_piece).grid(row=5, column=0, columnspan=2, pady=10)
    
    # function to edit details of existing piece
    def edit_piece(self):
        # get selected piece
        selected_item = self.tree.selection()
        if not selected_item:
            # warning displayed if no selection
            messagebox.showwarning("Edit Piece", "No piece selected!")
            return
        # retrieve title of selected piece
        title = self.tree.item(selected_item[0], 'values')[0]
        piece_to_edit = None
        # find piece in collection
        for piece in self.manager.pieces:
            if piece.title == title:
                piece_to_edit = piece
                break

        if not piece_to_edit:
            # if piece is not found, give warning to user
            messagebox.showwarning("Edit Piece", "Piece not found.")
            return
        
        # nested function to save changes
        def save_changes():
            # update attributes with changes
            piece_to_edit.title = title_entry.get()
            piece_to_edit.composer = composer_entry.get()
            piece_to_edit.time_period = time_period_entry.get()
            piece_to_edit.instrumentation = instrumentation_entry.get()
            piece_to_edit.difficulty = difficulty_entry.get()
            # update table
            self.update_table()
            # close edit window
            edit_window.destroy()
        
        # create a new window for editing piece details
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"Edit Piece: {piece_to_edit.title}")
        edit_window.geometry("400x300") #set window size
        # create labels and pre-fill entry fields with current attributes
        ttk.Label(edit_window, text="Title").grid(row=0, column=0, padx=10, pady=5)
        title_entry = ttk.Entry(edit_window)
        title_entry.insert(0, piece_to_edit.title)
        title_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(edit_window, text="Composer").grid(row=1, column=0, padx=10, pady=5)
        composer_entry = ttk.Entry(edit_window)
        composer_entry.insert(0, piece_to_edit.composer)
        composer_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(edit_window, text="Time Period").grid(row=2, column=0, padx=10, pady=5)
        time_period_entry = ttk.Entry(edit_window)
        time_period_entry.insert(0, piece_to_edit.time_period)
        time_period_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(edit_window, text="Instrumentation").grid(row=3, column=0, padx=10, pady=5)
        instrumentation_entry = ttk.Entry(edit_window)
        instrumentation_entry.insert(0, piece_to_edit.instrumentation)
        instrumentation_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(edit_window, text="Difficulty").grid(row=4, column=0, padx=10, pady=5)
        difficulty_entry = ttk.Entry(edit_window)
        difficulty_entry.insert(0, piece_to_edit.difficulty)
        difficulty_entry.grid(row=4, column=1, padx=10, pady=5)
        # save button calling save_piece function
        ttk.Button(edit_window, text="Save", command=save_changes).grid(row=5, column=0, columnspan=2, pady=10)
    
    # function to remove selected piece from collection
    def remove_piece(self):
        # get selected piece
        selected_item = self.tree.selection()
        if not selected_item:
            # gives warning if it doesn't exist
            messagebox.showwarning("Remove Piece", "No piece selected!")
            return
        # get title and remove from table
        title = self.tree.item(selected_item[0], 'values')[0]
        self.manager.remove_piece(title)
        self.update_table()
    
    # function to import data from CSV
    def import_csv(self):
        # open file dialog to select CSV file
        file_path = filedialog.askopenfilename(filetypes=[["CSV Files", "*.csv"]])
        if file_path:
            # imports data from CSV and updates table to display imported data
            self.manager.import_from_csv(file_path)
            self.update_table()
    
    # function to export collection to CSV file
    def export_csv(self):
        # open file dialog to specify file path for saving CSV
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[["CSV Files", "*.csv"]])
        if file_path:
            # export data
            self.manager.export_to_csv(file_path)
    
    # function to refresh table to display current collection
    def update_table(self):
        # clear all rows in the current table
        for item in self.tree.get_children():
            self.tree.delete(item)
        # add each piece in collection as new row in the table
        for piece in self.manager.pieces:
            self.tree.insert("", "end", values=(piece.title, piece.composer, piece.time_period, piece.instrumentation, piece.difficulty))
        # make GUI redraw table
        self.tree.update_idletasks()

# just to run the main function if its run directly
if __name__ == "__main__":
    root = tk.Tk()
    app = CollectionApp(root)
    root.mainloop()