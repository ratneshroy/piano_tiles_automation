import pyautogui
import cv2
import numpy as np

def show_mouse_position():
    """Displays real-time mouse position over the screen."""
    while True:
        x, y = pyautogui.position()  # Get mouse coordinates
        screen = np.zeros((300, 500, 3), dtype=np.uint8)  # Create a black window

        text = f"X: {x}, Y: {y}"
        cv2.putText(screen, text, (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Mouse Position", screen)  # Show position
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cv2.destroyAllWindows()

show_mouse_position()
