import cv2
import numpy as np
import pyautogui
import keyboard
import mss
import time
from pynput.mouse import Controller, Button
from overlay_Bt import run_overlay


running = False  # Flag to track whether the script is active

def capture_strip(GAME_X_START,GAME_X_END,GAME_Y_START):
    """Fast screen capture using mss."""
    with mss.mss() as sct:
        monitor = {"top": GAME_Y_START, "left": GAME_X_START, "width": GAME_X_END - GAME_X_START, "height": 2}  # Game strip area
        screen = sct.grab(monitor)
        gray = cv2.cvtColor(np.array(screen), cv2.COLOR_BGRA2GRAY)  # Convert to grayscale
        return gray


def find_black_tiles(gray_strip):
    """Detects large black tiles while ignoring thin vertical dividers."""
    _, binary = cv2.threshold(gray_strip, 100, 255, cv2.THRESH_BINARY_INV)  # Binarize image
    black_pixels = np.where(binary[0] == 255)[0]  # Get X positions of black pixels

    tile_positions = []
    min_tile_width = 30  # Minimum width to be considered a tile (adjust if needed)

    if len(black_pixels) > 10:
        start = black_pixels[0]
        for i in range(1, len(black_pixels)):
            if black_pixels[i] - black_pixels[i - 1] > 10:  # Detect separate tiles
                end = black_pixels[i - 1]
                width = end - start  # Calculate tile width

                if width >= min_tile_width:  # Ignore narrow dividers
                    tile_positions.append((start + end) // 2)  # Midpoint of tile

                start = black_pixels[i]

        # Check last detected tile
        width = black_pixels[-1] - start
        if width >= min_tile_width:
            tile_positions.append((start + black_pixels[-1]) // 2)

    return tile_positions
mouse = Controller()


# def tap_tiles(tile_positions):
#     """Click tiles using low-level Windows API (better for MEmu)."""
#     for x in tile_positions:
#         screen_x = GAME_X_START + x
#         screen_y = GAME_Y_START + 5
#         mouse.position = (screen_x, screen_y)  # Move mouse
#         mouse.click(Button.left)  # Click
def tap_tiles(tile_positions,GAME_X_START,GAME_Y_START):
    """Converts tile positions to screen coordinates and clicks them."""
    for x in tile_positions:
        screen_x = GAME_X_START + x
        screen_y = GAME_Y_START + 5  # Click slightly below strip
        pyautogui.click(screen_x, screen_y)
def main():
    global running
    run_overlay()
    while True:
        if keyboard.is_pressed('s'):  # Start detection
            running = True
            print("Started!")
            time.sleep(0.5)  # Prevent accidental double press

        if keyboard.is_pressed('q'):  # Stop detection
            running = False
            print("Stopped!")
            time.sleep(0.5)

        if running:

            strip = capture_strip()
            tile_positions = find_black_tiles(strip)

            tap_tiles(tile_positions)

if __name__ == "__main__":
    main()
