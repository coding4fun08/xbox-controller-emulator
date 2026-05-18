import threading
from pynput import keyboard
import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()


key_bindings = {
    'w': 'dpad_up',
    'a': 'dpad_left',
    's': 'dpad_down',
    'd': 'dpad_right',
    'v': 'b',
    'q': 'y',
    keyboard.Key.space: 'a',

    keyboard.Key.shift_l: 'lb',
    keyboard.Key.shift_r: 'lb',
    keyboard.Key.left: 'x',
    keyboard.Key.right: 'rb',
  
}



button_map = {
    'a': vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    'b': vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    'x': vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    'y': vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
    'start': vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
    'lb': vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
    'rb': vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
    'dpad_up': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    'dpad_down': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    'dpad_left': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    'dpad_right': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
}

active_keys = {key: False for key in button_map | {'lt', 'rt'}}

input_lock = threading.Lock()
running = True



def normalize_key(key):
    try:
        return key.char.lower()
    except AttributeError:
        return key


def update_gamepad():
    with input_lock:
 
        for name, button in button_map.items():
            if active_keys[name]:
                gamepad.press_button(button=button)
            else:
                gamepad.release_button(button=button)


        gamepad.left_trigger_float(1.0 if active_keys['lt'] else 0.0)
        gamepad.right_trigger_float(1.0 if active_keys['rt'] else 0.0)

        gamepad.update()




def handle_key(key, pressed):
    if key == keyboard.Key.f6:
        global running
        running = False
        return False

    normalized = normalize_key(key)
    binding = key_bindings.get(normalized) or key_bindings.get(key)

    if binding:
        with input_lock:
            active_keys[binding] = pressed
        update_gamepad()


def on_press(key):
    handle_key(key, True)


def on_release(key):
    handle_key(key, False)



def format_keybinds():
    lines = []
    for key, binding in key_bindings.items():
        if isinstance(key, str):
            key_str = key
        else:
            key_str = str(key).split('.')[-1]
        lines.append(f"  {key_str:<15} → {binding}")
    return "\n".join(lines)


def main():
    print("=" * 50)
    print("key-to-xbox-controller - by @coding4fun08\n")
    print("=" * 50)
    print("\nKeybindings:")
    print(format_keybinds())
    print("\nF6 to turn off\n")

    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            while running:
                time.sleep(0.01)

    finally:
        gamepad.reset()
        gamepad.update()
        print("turned off")


if __name__ == "__main__":
    main()
