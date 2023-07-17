import tkinter as tk
import webbrowser
def navigate_to_website():
    url = entry.get()
    print("https://chat.openai.com/", url)
    webbrowser.open("{https://chat.openai.com/}")
obj = tk.Tk()
obj.title("Assignment_10")
entry = tk.Entry(obj, width=100)
entry.pack()
button = tk.Button(obj, text="Search", command=navigate_to_website)
button.pack()
obj.mainloop()