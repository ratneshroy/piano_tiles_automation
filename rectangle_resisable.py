import tkinter as tk
from tkinter import ttk


class ResizableDraggableBox:
    def __init__(self, root, x, y, width, height, color="black"):
        self.root = root
        self.frame = tk.Frame(root, bg=color, width=width, height=height)
        self.frame.place(x=x, y=y)

        self.frame.bind("<ButtonPress-1>", self.start_move)
        self.frame.bind("<B1-Motion>", self.on_move)

        self.resizer = ttk.Sizegrip(self.frame)
        self.resizer.place(relx=1.0, rely=1.0, anchor="se")
        self.resizer.bind("<ButtonPress-1>", self.start_resize)
        self.resizer.bind("<B1-Motion>", self.on_resize)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        x = self.frame.winfo_x() + (event.x - self.x)
        y = self.frame.winfo_y() + (event.y - self.y)
        self.frame.place(x=x, y=y)

    def start_resize(self, event):
        self.start_width = self.frame.winfo_width()
        self.start_height = self.frame.winfo_height()
        self.start_x = event.x
        self.start_y = event.y

    def on_resize(self, event):
        new_width = max(50, self.start_width + (event.x - self.start_x))
        new_height = max(50, self.start_height + (event.y - self.start_y))
        self.frame.config(width=new_width, height=new_height)


class ContentHiderOverlay:
    def __init__(self, root):
        self.root = root
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.attributes("-transparentcolor", "white")
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        self.root.configure(bg="white")

        self.boxes = []

        # Floating Control Panel
        self.control_panel = tk.Frame(root, bg="gray", relief="raised", bd=2)
        self.control_panel.place(x=20, y=20)

        self.add_box_button = tk.Button(self.control_panel, text="Add Box", command=self.add_box)
        self.add_box_button.pack(padx=5, pady=5)

        self.exit_button = tk.Button(self.control_panel, text="Exit", command=root.destroy)
        self.exit_button.pack(padx=5, pady=5)

    def add_box(self):
        box = ResizableDraggableBox(self.root, 100, 100, 150, 100)
        self.boxes.append(box)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContentHiderOverlay(root)
    root.mainloop()
