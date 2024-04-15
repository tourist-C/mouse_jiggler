import pyautogui
import time

# config
mouse_offset_x = 10
mouse_offset_y = 10
jiggle_period = 5 # seoncds


def move_mouse():
    # Get the current mouse position
    original_x, original_y = pyautogui.position()

    # Calculate the new position slightly offset from the original position
    new_x = original_x + mouse_offset_x
    new_y = original_y + mouse_offset_y

    # Move the mouse to the new position
    pyautogui.moveTo(new_x, new_y, duration=0.1)

    # Move the mouse back to the original position
    pyautogui.moveTo(original_x, original_y, duration=0.5)

    print(f"current pos: {original_x, original_y}")


def jiggle_mouse(interval):
    while True:
        move_mouse()
        time.sleep(interval)

def main():
    

    print("Running mouse jiggler...")
    print("Press ctrl+c to quit")

    print(f"period: {jiggle_period} x: {mouse_offset_x}, y: {mouse_offset_y}")

    # Set the interval between mouse jiggles in seconds
    jiggle_interval = jiggle_period

    # Start the mouse jiggler
    jiggle_mouse(jiggle_interval)

if __name__ == "__main__":
    main()


