import tkinter as tk
from screen_selector import get_screen_selection  # Import selection module

class OverlayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Overlay Control")
        self.root.geometry("200x200+100+100")  # Default size and position
        self.root.attributes("-topmost", True)  # Keep window on top
        self.root.configure(bg="gray")

        # Allow resizing
        self.root.resizable(True, True)

        # Get Coordinates
        self.coord_button = tk.Button(root, text="Get Coordinates", command=self.get_coordinates, bg="blue", fg="white")
        self.coord_button.pack(fill="both", expand=True, padx=10, pady=5)

        # Start Button
        self.start_button = tk.Button(root, text="Start", command=self.start_action, bg="green", fg="white")
        self.start_button.pack(fill="both", expand=True, padx=10, pady=5)

        # Stop Button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_action, bg="red", fg="white")
        self.stop_button.pack(fill="both", expand=True, padx=10, pady=5)

        # Variable to store coordinates
        self.coords = None

    def get_coordinates(self):
        """Gets coordinates from screen selection and stores them."""
        self.coords = get_screen_selection()
        if self.coords:
            x1, y1, x2, y2 = self.coords
            print(f"Selected Region: X={x1}, Y={y1}, Width={x2 - x1}, Height={y2 - y1}")

    def start_action(self):
        """Start action (modify with your own logic)."""
        print("Start clicked!")
        if self.coords:
            print(f"Using Selected Region: {self.coords}")
        else:
            print("No region selected yet.")

    def stop_action(self):
        """Stop action (modify with your own logic)."""
        print("Stop clicked!")

def run_overlay():
    """Function to start the overlay app, useful when importing as a module."""
    root = tk.Tk()
    app = OverlayApp(root)
    root.mainloop()

if __name__ == "__main__":
    print(run_overlay())
