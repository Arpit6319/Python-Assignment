import tkinter as tk
from tkinter import ttk

def submit_form():
    selected_source = source_var.get()

    faq_pages = {
        "Instagram Ads": "https://www.instagram.com",
        "YouTube Ads": "https://www.youtube.com",
    }

    if selected_source in faq_pages:
        faq_url = faq_pages[selected_source]
        print(f"Navigating to {faq_url}")

app = tk.Tk()
app.title("Course Enquiry Form")

label = ttk.Label(app, text="Enter your course enquiry details:")
label.pack(pady=10)

source_var = tk.StringVar()
source_var.set("Instagram Ads") 

source_label = ttk.Label(app, text="Where did you hear about the course?")
source_label.pack()

source_dropdown = ttk.OptionMenu(app, source_var, "Instagram Ads", "Instagram Ads", "YouTube Ads")
source_dropdown.pack(pady=5)

submit_button = ttk.Button(app, text="Submit", command=submit_form)
submit_button.pack(pady=10)

app.mainloop()