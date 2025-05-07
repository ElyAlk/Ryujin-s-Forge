from collections import defaultdict
import re
import tkinter as tk
from tkinter import filedialog

pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Create the main window
root = tk.Tk()
root.title("File Selector")

def open_file():
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        with open(file_path, "r") as file:
            file_contents = file.read()
            # extracting email through regx pattern
            emails = re.findall(pattern, file_contents, re.MULTILINE)
            total_emails = 0

            # sorting emails
            sorted_emails = defaultdict(list)
            for email in emails:
                domain = email[email.index("@") + 1: email.index(".")]
                if domain != "":
                    sorted_emails[domain].append(email)

            domains = list(sorted_emails.keys())
            print(len(domains))
            for dom in domains:
                emails_list = sorted_emails[dom]
                total_emails += len(emails_list)
                #print(dom, ": \n", emails_list)
                text_box.insert(tk.END, dom + ": " + " ".join(emails_list) + "\n")

            text_box.insert(tk.END, str(total_emails) + " emails found!")


# Add a button to open files
button = tk.Button(root, text="Open File", command=open_file)
button.pack(pady=10)

# Add a text box to display file contents
text_box = tk.Text(root, height=15, width=50)
text_box.pack(fill=tk.BOTH, expand=True)

root.mainloop()

