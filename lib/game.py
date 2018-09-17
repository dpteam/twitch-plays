import os
import time
if os.name == 'nt':
    import win32api
    import win32con
else:
    from subprocess import Popen

class Game:

    # Comment out any button(s) that would be unused
    if os.name == 'nt':
        keymap = {
            # Keys in WIN32
            # http://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
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
    else:
        keymap = {
            # Keys in X11 automation
            'up': ["0"],
            'down': ["1"],
            'left': ["2"],
            'right': ["3"],
            'a': ["4"],
            'b': ["5"],
            'x': ["6"],
            'y': ["7"],
            'start': ["8"],
            'select': ["9"],
            'l': ["a"],
            'r': ["b"]
        }

    def get_valid_buttons(self):
        return [button for button in self.keymap.keys()]

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        return self.keymap[button]

    def push_button(self, button):
        if os.name == 'nt':
            win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
            time.sleep(.15) # Time to wait before key depress; adjust if nessessary
            win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
        else:
            Popen(["xdotool", "keydown"] + self.button_to_key(button))
            time.sleep(.15) # Time to wait before key depress; adjust if nessessary
            Popen(["xdotool", "keyup"] + self.button_to_key(button))
