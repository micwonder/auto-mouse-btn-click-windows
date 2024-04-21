import pyautogui
import keyboard
import time
from pynput import mouse


def on_click(x, y, button, pressed, coords):
    """Capture mouse click coordinates when Ctrl is held and left button is clicked."""
    if pressed and button == mouse.Button.left and keyboard.is_pressed("shift"):
        coords.append((x, y))
        if len(coords) == 2:
            return False  # Stop listener after two coordinates


def get_coordinates():
    """Get two sets of coordinates using Ctrl + mouse click."""
    coords = []
    with mouse.Listener(
        on_click=lambda x, y, button, pressed: on_click(x, y, button, pressed, coords)
    ) as listener:
        listener.join()
    return coords


import pyautogui
import keyboard


def draw_grid(
    top_left_x: float, top_left_y: float, bottom_right_x: float, bottom_right_y: float
):
    """Draws a grid of dots in MS Paint using floating-point precision."""
    # Calculate spacing based on the number of dots per dimension (here assumed to be 10)
    x_spacing = (bottom_right_x - top_left_x) / 10.0
    y_spacing = (bottom_right_y - top_left_y) / 10.0

    # Determine loop direction for x and y (to handle cases where coordinates might be reversed)
    x_step = 1 if x_spacing > 0 else -1
    y_step = 1 if y_spacing > 0 else -1

    # Initialize loop variables
    x = top_left_x
    while x <= bottom_right_x if x_step > 0 else x >= bottom_right_x:
        y = top_left_y
        while y <= bottom_right_y if y_step > 0 else y >= bottom_right_y:
            if keyboard.is_pressed("s"):  # Break if 's' is pressed
                print("Breaking out of the grid drawing...")
                return True
            pyautogui.moveTo(
                int(x), int(y)
            )  # Move mouse to (x, y), converting to int for screen coordinates
            pyautogui.click()  # Click to draw a dot
            y += y_spacing  # Move y to the next position
        x += x_spacing  # Move x to the next position

    print("Completed!")
    return False


def main():
    running = False
    while True:
        if keyboard.is_pressed("s"):
            if running:
                print("Pausing...")
                running = False
                time.sleep(1)
            else:
                while True:
                    print(
                        "Please use Ctrl+Left Click to select two corners of the grid."
                    )
                    coords = get_coordinates()
                    if len(coords) < 2:
                        print("Insufficient coordinates, please try again.")
                        continue
                    else:
                        top_left_x, top_left_y = coords[0]
                        bottom_right_x, bottom_right_y = coords[1]
                        break

                print(
                    f"Coordinates set: Top Left ({top_left_x}, {top_left_y}), Bottom Right ({bottom_right_x}, {bottom_right_y})"
                )

                print("Starting...")
                running = True
                time.sleep(1)
                interrupted = draw_grid(
                    top_left_x, top_left_y, bottom_right_x, bottom_right_y
                )
                if interrupted:
                    running = False
                if not interrupted:
                    running = False
        time.sleep(0.05)


if __name__ == "__main__":
    main()
