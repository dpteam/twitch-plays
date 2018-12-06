import win32api
import win32con
import time

class Game:
	keymap = {
		# Comment out any button(s) that would be unused
		'u': 0x30,
		'd': 0x31,
		'l': 0x32,
		'r': 0x33,
		'a': 0x34,
		'b': 0x35,
		'x': 0x36,
		'y': 0x37,
		'st': 0x38,
		'sl': 0x39,
		'l*': 0x41,
		'r*': 0x42,
		'save': 0x00,
		'load': 0x00,
		'l*+a': 0x00,
		'l*+r*': 0x00,
		'a+b': 0x00,
		'b+u': 0x00,
		'b+d': 0x00,
		'b+l': 0x00,
		'b+r': 0x00,
		'b+ul': 0x00,
		'b+ur': 0x00,
		'b+dl': 0x00,
		'b+dr': 0x00,
        'b+lu': 0x00,
		'b+ru': 0x00,
		'b+ld': 0x00,
		'b+rd': 0x00,
		'r*+a': 0x00,
		'r*+u': 0x00,
		'r*+d': 0x00,
		'r*+l': 0x00,
		'r*+r': 0x00,
		'x+u': 0x00,
		'x+d': 0x00,
		'x+l': 0x00,
		'x+r': 0x00,
		'y+u': 0x00,
		'y+d': 0x00,
		'y+l': 0x00,
		'y+r': 0x00,
		'u+l': 0x00,
		'u+r': 0x00,
		'd+l': 0x00,
		'd+r': 0x00,
        'l+u': 0x00,
		'r+u': 0x00,
		'l+d': 0x00,
		'r+d': 0x00,
		'u2': 0x00,
		'u3': 0x00,
		'u4': 0x00,
		'u5': 0x00,
		'u6': 0x00,
		'u7': 0x00,
		'u8': 0x00,
		'u9': 0x00,
		'd2': 0x00,
		'd3': 0x00,
		'd4': 0x00,
		'd5': 0x00,
		'd6': 0x00,
		'd7': 0x00,
		'd8': 0x00,
		'd9': 0x00,
		'l2': 0x00,
		'l3': 0x00,
		'l4': 0x00,
		'l5': 0x00,
		'l6': 0x00,
		'l7': 0x00,
		'l8': 0x00,
		'l9': 0x00,
		'r2': 0x00,
		'r3': 0x00,
		'r4': 0x00,
		'r5': 0x00,
		'r6': 0x00,
		'r7': 0x00,
		'r8': 0x00,
		'r9': 0x00,
		'a2': 0x00,
		'a3': 0x00,
		'a4': 0x00,
		'a5': 0x00,
		'a6': 0x00,
		'a7': 0x00,
		'a8': 0x00,
		'a9': 0x00,
		'b2': 0x00,
		'b3': 0x00,
		'b4': 0x00,
		'b5': 0x00,
		'b6': 0x00,
		'b7': 0x00,
		'b8': 0x00,
		'b9': 0x00,
		'u+l2': 0x00,
		'u+l3': 0x00,
		'u+l4': 0x00,
		'u+l5': 0x00,
		'u+l6': 0x00,
		'u+l7': 0x00,
		'u+l8': 0x00,
		'u+l9': 0x00,
		'u+r2': 0x00,
		'u+r3': 0x00,
		'u+r4': 0x00,
		'u+r5': 0x00,
		'u+r6': 0x00,
		'u+r7': 0x00,
		'u+r8': 0x00,
		'u+r9': 0x00,
		'd+l2': 0x00,
		'd+l3': 0x00,
		'd+l4': 0x00,
		'd+l5': 0x00,
		'd+l6': 0x00,
		'd+l7': 0x00,
		'd+l8': 0x00,
		'd+l9': 0x00,
		'd+r2': 0x00,
		'd+r3': 0x00,
		'd+r4': 0x00,
		'd+r5': 0x00,
		'd+r6': 0x00,
		'd+r7': 0x00,
		'd+r8': 0x00,
		'd+r9': 0x00
	}
	def get_valid_buttons(self):
		return [button for button in self.keymap.keys()]
	def is_valid_button(self, button):
		return button in self.keymap.keys()
	def button_to_key(self, button):
		return self.keymap[button]
	def btnCombo(self, x, y):
		win32api.keybd_event(x, 0, 0, 0)
		win32api.keybd_event(y, 0, 0, 0)
		time.sleep(.15)
		win32api.keybd_event(x, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(y, 0, win32con.KEYEVENTF_KEYUP, 0)
    def btnHoldCombo(self, x, y):
		win32api.keybd_event(x, 0, 0, 0)
		win32api.keybd_event(y, 0, 0, 0)
		time.sleep(.5)
		win32api.keybd_event(x, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(y, 0, win32con.KEYEVENTF_KEYUP, 0)
	def btnRun(self, x):
		win32api.keybd_event(0x35, 0, 0, 0)
		win32api.keybd_event(x, 0, 0, 0)
		time.sleep(3)
		win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(x, 0, win32con.KEYEVENTF_KEYUP, 0)
	def btnRunCombo(self, x, y):
		win32api.keybd_event(0x35, 0, 0, 0)
		win32api.keybd_event(x, 0, 0, 0)
		win32api.keybd_event(y, 0, 0, 0)
		time.sleep(3)
		win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(x, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(y, 0, win32con.KEYEVENTF_KEYUP, 0)
	def btnLoop(self, x, y):
		loopCntr=0
		while loopCntr < y:
			win32api.keybd_event(x, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(x, 0, win32con.KEYEVENTF_KEYUP, 0)
			time.sleep(.5)
			loopCntr+=1
	def btnLoopCombo(self, x, y, z):
		loopCntr=0
		while loopCntr < z:
			win32api.keybd_event(x, 0, 0, 0)
			win32api.keybd_event(y, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(x, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(y, 0, win32con.KEYEVENTF_KEYUP, 0)
			time.sleep(.5)
			loopCntr+=1
	# Ensure bot.py provides the username
	def push_button(self, button, username):
		# How much elifs does it take to disorient a programmer?
		# Too many to count
		if button == 'l*+a':
			self.btnCombo(0x41, 0x34)
		elif button == 'l*+r*':
			self.btnCombo(0x41, 0x42)
		elif button == 'b+u':
			self.btnRun(0x30)
		elif button == 'b+d':
			self.btnRun(0x31)
		elif button == 'b+l':
			self.btnRun(0x32)
		elif button == 'b+r':
			self.btnRun(0x33)
		elif button == 'a+b':
			self.btnRun(0x34)
		elif button == 'b+ul' or button == 'b+lu':
			self.btnRunCombo(0x30, 0x32)
		elif button == 'b+ur' or button == 'b+ru':
			self.btnRunCombo(0x30, 0x33)
		elif button == 'b+dl' or button == 'b+ld':
			self.btnRunCombo(0x31, 0x32)
		elif button == 'b+dr' or button == 'b+rd':
			self.btnRunCombo(0x31, 0x33)
		elif button == 'r*+u':
			self.btnCombo(0x42, 0x30)
		elif button == 'r*+d':
			self.btnCombo(0x42, 0x31)
		elif button == 'r*+l':
			self.btnCombo(0x42, 0x32)
		elif button == 'r*+r':
			self.btnCombo(0x42, 0x33)
		elif button == 'r*+a':
			self.btnCombo(0x42, 0x34)
		elif button == 'u+l' or button == 'l+u':
			self.btnCombo(0x30, 0x32)
		elif button == 'u+r' or button == 'r+u':
			self.btnCombo(0x30, 0x33)
		elif button == 'd+l' or button == 'l+d':
			self.btnCombo(0x31, 0x32)
		elif button == 'd+r' or button == 'r+d':
			self.btnCombo(0x31, 0x33)
		elif button == 'x+u':
			self.btnCombo(0x36, 0x30)
		elif button == 'x+d':
			self.btnCombo(0x36, 0x31)
		elif button == 'x+l':
			self.btnCombo(0x36, 0x32)
		elif button == 'x+r':
			self.btnCombo(0x36, 0x33)
		elif button == 'y+u':
			self.btnHoldCombo(0x37, 0x30)
		elif button == 'y+d':
			self.btnHoldCombo(0x37, 0x31)
		elif button == 'y+l':
			self.btnHoldCombo(0x37, 0x32)
		elif button == 'y+r':
			self.btnHoldCombo(0x37, 0x33)
		elif button == 'u2':
			self.btnLoop(0x30, 2)
		elif button == 'u3':
			self.btnLoop(0x30, 3)
		elif button == 'u4':
			self.btnLoop(0x30, 4)
		elif button == 'u5':
			self.btnLoop(0x30, 5)
		elif button == 'u6':
			self.btnLoop(0x30, 6)
		elif button == 'u7':
			self.btnLoop(0x30, 7)
		elif button == 'u8':
			self.btnLoop(0x30, 8)
		elif button == 'u9':
			self.btnLoop(0x30, 9)
		elif button == 'd2':
			self.btnLoop(0x31, 2)
		elif button == 'd3':
			self.btnLoop(0x31, 3)
		elif button == 'd4':
			self.btnLoop(0x31, 4)
		elif button == 'd5':
			self.btnLoop(0x31, 5)
		elif button == 'd6':
			self.btnLoop(0x31, 6)
		elif button == 'd7':
			self.btnLoop(0x31, 7)
		elif button == 'd8':
			self.btnLoop(0x31, 8)
		elif button == 'd9':
			self.btnLoop(0x31, 9)
		elif button == 'l2':
			self.btnLoop(0x32, 2)
		elif button == 'l3':
			self.btnLoop(0x32, 3)
		elif button == 'l4':
			self.btnLoop(0x32, 4)
		elif button == 'l5':
			self.btnLoop(0x32, 5)
		elif button == 'l6':
			self.btnLoop(0x32, 6)
		elif button == 'l7':
			self.btnLoop(0x32, 7)
		elif button == 'l8':
			self.btnLoop(0x32, 8)
		elif button == 'l9':
			self.btnLoop(0x32, 9)
		elif button == 'r2':
			self.btnLoop(0x33, 2)
		elif button == 'r3':
			self.btnLoop(0x33, 3)
		elif button == 'r4':
			self.btnLoop(0x33, 4)
		elif button == 'r5':
			self.btnLoop(0x33, 5)
		elif button == 'r6':
			self.btnLoop(0x33, 6)
		elif button == 'r7':
			self.btnLoop(0x33, 7)
		elif button == 'r8':
			self.btnLoop(0x33, 8)
		elif button == 'r9':
			self.btnLoop(0x33, 9)
		elif button == 'a2':
			self.btnLoop(0x34, 2)
		elif button == 'a3':
			self.btnLoop(0x34, 3)
		elif button == 'a4':
			self.btnLoop(0x34, 4)
		elif button == 'a5':
			self.btnLoop(0x34, 5)
		elif button == 'a6':
			self.btnLoop(0x34, 6)
		elif button == 'a7':
			self.btnLoop(0x34, 7)
		elif button == 'a8':
			self.btnLoop(0x34, 8)
		elif button == 'a9':
			self.btnLoop(0x34, 9)
		elif button == 'b2':
			self.btnLoop(0x35, 2)
		elif button == 'b3':
			self.btnLoop(0x35, 3)
		elif button == 'b4':
			self.btnLoop(0x35, 4)
		elif button == 'b5':
			self.btnLoop(0x35, 5)
		elif button == 'b6':
			self.btnLoop(0x35, 6)
		elif button == 'b7':
			self.btnLoop(0x35, 7)
		elif button == 'b8':
			self.btnLoop(0x35, 8)
		elif button == 'b9':
			self.btnLoop(0x35, 9)
		elif button == 'u+l2' or button == 'l+u2':
			self.btnLoopCombo(0x30, 0x32, 2)
		elif button == 'u+l3' or button == 'l+u3':
			self.btnLoopCombo(0x30, 0x32, 3)
		elif button == 'u+l4' or button == 'l+u4':
			self.btnLoopCombo(0x30, 0x32, 4)
		elif button == 'u+l5' or button == 'l+u5':
			self.btnLoopCombo(0x30, 0x32, 5)
		elif button == 'u+l6' or button == 'l+u6':
			self.btnLoopCombo(0x30, 0x32, 6)
		elif button == 'u+l7' or button == 'l+u7':
			self.btnLoopCombo(0x30, 0x32, 7)
		elif button == 'u+l8' or button == 'l+u8':
			self.btnLoopCombo(0x30, 0x32, 8)
		elif button == 'u+l9' or button == 'l+u9':
			self.btnLoopCombo(0x30, 0x32, 9)
		elif button == 'u+r2' or button == 'r+u2':
			self.btnLoopCombo(0x30, 0x33, 2)
		elif button == 'u+r3' or button == 'r+u3':
			self.btnLoopCombo(0x30, 0x33, 3)
		elif button == 'u+r4' or button == 'r+u4':
			self.btnLoopCombo(0x30, 0x33, 4)
		elif button == 'u+r5' or button == 'r+u5':
			self.btnLoopCombo(0x30, 0x33, 5)
		elif button == 'u+r6' or button == 'r+u6':
			self.btnLoopCombo(0x30, 0x33, 6)
		elif button == 'u+r7' or button == 'r+u7':
			self.btnLoopCombo(0x30, 0x33, 7)
		elif button == 'u+r8' or button == 'r+u8':
			self.btnLoopCombo(0x30, 0x33, 8)
		elif button == 'u+r9' or button == 'r+u9':
			self.btnLoopCombo(0x30, 0x33, 9)
		elif button == 'd+l2' or button == 'l+d2':
			self.btnLoopCombo(0x31, 0x32, 2)
		elif button == 'd+l3' or button == 'l+d3':
			self.btnLoopCombo(0x31, 0x32, 3)
		elif button == 'd+l4' or button == 'l+d4':
			self.btnLoopCombo(0x31, 0x32, 4)
		elif button == 'd+l5' or button == 'l+d5':
			self.btnLoopCombo(0x31, 0x32, 5)
		elif button == 'd+l6' or button == 'l+d6':
			self.btnLoopCombo(0x31, 0x32, 6)
		elif button == 'd+l7' or button == 'l+d7':
			self.btnLoopCombo(0x31, 0x32, 7)
		elif button == 'd+l8' or button == 'l+d8':
			self.btnLoopCombo(0x31, 0x32, 8)
		elif button == 'd+l9' or button == 'l+d9':
			self.btnLoopCombo(0x31, 0x32, 9)
		elif button == 'd+r2' or button == 'r+d2':
			self.btnLoopCombo(0x31, 0x33, 2)
		elif button == 'd+r3' or button == 'r+d3':
			self.btnLoopCombo(0x31, 0x33, 3)
		elif button == 'd+r4' or button == 'r+d4':
			self.btnLoopCombo(0x31, 0x33, 4)
		elif button == 'd+r5' or button == 'r+d5':
			self.btnLoopCombo(0x31, 0x33, 5)
		elif button == 'd+r6' or button == 'r+d6':
			self.btnLoopCombo(0x31, 0x33, 6)
		elif button == 'd+r7' or button == 'r+d7':
			self.btnLoopCombo(0x31, 0x33, 7)
		elif button == 'd+r8' or button == 'r+d8':
			self.btnLoopCombo(0x31, 0x33, 8)
		elif button == 'd+r9' or button == 'r+d9':
			self.btnLoopCombo(0x31, 0x33, 9)
		elif button == 'save' and (username == 'mod1' or username == 'mod2' or username == 'mod3'):
			win32api.keybd_event(0x43, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(0x43, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'load' and (username == 'mod1' or username == 'mod2' or username == 'mod3'):
			win32api.keybd_event(0x44, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(0x44, 0, win32con.KEYEVENTF_KEYUP, 0)
		else:
			win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
