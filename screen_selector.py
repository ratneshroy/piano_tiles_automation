import tkinter as tk


def start_selection(event, canvas, selection):
    """Capture the start coordinates when user clicks."""
    selection["start_x"] = canvas.canvasx(event.x)
    selection["start_y"] = canvas.canvasy(event.y)
    if selection["rect"]:
        canvas.delete(selection["rect"])


def draw_selection(event, canvas, selection):
    """Draw a rectangle as the user drags the mouse."""
    end_x = canvas.canvasx(event.x)
    end_y = canvas.canvasy(event.y)
    if selection["rect"]:
        canvas.delete(selection["rect"])
    selection["rect"] = canvas.create_rectangle(
        selection["start_x"], selection["start_y"], end_x, end_y, outline="red", width=2
    )


def end_selection(event, root, canvas, selection):
    """Save coordinates and close the window after selection."""
    end_x = canvas.canvasx(event.x)
    end_y = canvas.canvasy(event.y)
    selection["coords"] = (int(selection["start_x"]), int(selection["start_y"]), int(end_x), int(end_y))

    root.quit()  # Stop the Tkinter main loop
    root.destroy()  # Destroy the window


def get_screen_selection():
    """Creates a fullscreen overlay for screen selection and returns coordinates."""
    root = tk.Tk()
    root.title("Screen Selector")
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.3)  # Semi-transparent overlay
    root.configure(bg="black")

    selection = {"start_x": None, "start_y": None, "rect": None, "coords": None}

    canvas = tk.Canvas(root, cursor="cross", bg="black")
    canvas.pack(fill=tk.BOTH, expand=True)

    canvas.bind("<ButtonPress-1>", lambda event: start_selection(event, canvas, selection))
    canvas.bind("<B1-Motion>", lambda event: draw_selection(event, canvas, selection))
    canvas.bind("<ButtonRelease-1>", lambda event: end_selection(event, root, canvas, selection))

    root.mainloop()
    return selection["coords"]
