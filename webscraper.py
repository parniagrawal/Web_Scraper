import tkinter as tk
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox

def scrape_website():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a URL!")
        return
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, soup.get_text())
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch the webpage: {e}")

# Create main window
root = tk.Tk()
root.title("Web Scraper App")
root.geometry("600x400")

# URL Entry
tk.Label(root, text="Enter Website URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Scrape Button
scrape_button = tk.Button(root, text="Scrape Website", command=scrape_website)
scrape_button.pack(pady=10)

# Output Text Box
text_output = tk.Text(root, wrap=tk.WORD, height=15, width=70)
text_output.pack(pady=10)

# Run the application
root.mainloop()
