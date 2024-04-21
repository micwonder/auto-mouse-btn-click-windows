import pyautogui
import keyboard
import time


def draw_grid(top_left_x, top_left_y, bottom_right_x, bottom_right_y):
    """Draws a grid of dots in MS Paint from the top left to the bottom right coordinates."""
    # Calculate grid size and dot spacing (example spacing here is 10 pixels)
    spacing = 10
    for x in range(top_left_x, bottom_right_x, spacing):
        for y in range(top_left_y, bottom_right_y, spacing):
            pyautogui.moveTo(x, y)  # Move mouse to the calculated position
            pyautogui.click()  # Click to draw a dot


def main():
    running = False
    while True:
        if keyboard.is_pressed("s"):
            if running:
                print("Pausing...")
                running = False
                time.sleep(
                    1
                )  # pause for a bit to avoid multiple toggles on single press
            else:
                # Get grid boundaries from user input
                print("")
                top_left_x = int(input("Enter top left X coordinate: "))
                top_left_y = int(input("Enter top left Y coordinate: "))
                bottom_right_x = int(input("Enter bottom right X coordinate: "))
                bottom_right_y = int(input("Enter bottom right Y coordinate: "))

                print("Starting...")
                running = True
                time.sleep(
                    1
                )  # pause for a bit to avoid multiple toggles on single press
                draw_grid(top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        time.sleep(0.1)  # Slight delay to prevent high CPU usage


if __name__ == "__main__":
    main()
