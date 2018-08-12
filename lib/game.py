import win32api
import win32con
import time

class Game:

    keymap = {
        'up': 0x30,
        'down': 0x31,
        'left': 0x32,
        'right': 0x33,
        'a': 0x34,
        'b': 0x35,
        'x': 0x36,
        'y': 0x37,
        'start': 0x38,
        'select': 0x39,
        'l': 0x41,
        'r': 0x42
    }

    def get_valid_buttons(self):
        return [button for button in self.keymap.keys()]

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        return self.keymap[button]

    def push_button(self, button):
        win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
        time.sleep(.15)
        win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
