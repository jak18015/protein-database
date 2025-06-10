import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to insert data into the database
def submit_data():
    name = entry_name.get()
    accession = entry_accession.get()
    function = entry_function.get()
    domains = entry_domains.get()
    crispr_score = entry_crispr.get()
    reference = entry_reference.get()

    try:
        conn = sqlite3.connect('proteins.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO proteins (name, accession, function, domains, crispr_score, reference)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, accession, function, domains, float(crispr_score), reference))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Protein data added successfully!")

        # Clear entries after submission
        entry_name.delete(0, tk.END)
        entry_accession.delete(0, tk.END)
        entry_function.delete(0, tk.END)
        entry_domains.delete(0, tk.END)
        entry_crispr.delete(0, tk.END)
        entry_reference.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# Create the main window
root = tk.Tk()
root.title("Protein Entry Form")

# Labels and Entry Fields
labels = ["Protein Name", "Accession Number", "Function", "Conserved Domains", "CRISPR Score", "Reference"]
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
    
entry_name = tk.Entry(root, width=40)
entry_name.grid(row=0, column=1)

entry_accession = tk.Entry(root, width=40)
entry_accession.grid(row=1, column=1)

entry_function = tk.Entry(root, width=40)
entry_function.grid(row=2, column=1)

entry_domains = tk.Entry(root, width=40)
entry_domains.grid(row=3, column=1)

entry_crispr = tk.Entry(root, width=40)
entry_crispr.grid(row=4, column=1)

entry_reference = tk.Entry(root, width=40)
entry_reference.grid(row=5, column=1)

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit_data)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10)

# Start the GUI loop
root.mainloop()
