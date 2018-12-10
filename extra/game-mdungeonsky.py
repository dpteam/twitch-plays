import win32api
import win32con
import time

class Game:
	keymap = {
		# Comment out any button(s) that would be unused
		'n': 0x30,
		's': 0x31,
		'w': 0x32,
		'e': 0x33,
		'a': 0x34,
		'b': 0x35,
		'x': 0x36,
		'y': 0x37,
		'st': 0x38,
		'sl': 0x39,
		'l': 0x41,
		'r': 0x42,
		'save': 0x00,
		'load': 0x00,
		'l+a': 0x00,
		'l+b': 0x00,
		'l+r': 0x00,
		'a+b': 0x00,
		'b+n': 0x00,
		'b+s': 0x00,
		'b+w': 0x00,
		'b+e': 0x00,
		'b+nw': 0x00,
		'b+ne': 0x00,
		'b+sw': 0x00,
		'b+se': 0x00,
		'r+a': 0x00,
		'r+n': 0x00,
		'r+s': 0x00,
		'r+w': 0x00,
		'r+e': 0x00,
		'x+n': 0x00,
		'x+s': 0x00,
		'x+w': 0x00,
		'x+e': 0x00,
		'y+n': 0x00,
		'y+s': 0x00,
		'y+w': 0x00,
		'y+e': 0x00,
		'nw': 0x00,
		'ne': 0x00,
		'sw': 0x00,
		'se': 0x00,
		'n2': 0x00,
		'n3': 0x00,
		'n4': 0x00,
		'n5': 0x00,
		'n6': 0x00,
		'n7': 0x00,
		'n8': 0x00,
		'n9': 0x00,
		's2': 0x00,
		's3': 0x00,
		's4': 0x00,
		's5': 0x00,
		's6': 0x00,
		's7': 0x00,
		's8': 0x00,
		's9': 0x00,
		'w2': 0x00,
		'w3': 0x00,
		'w4': 0x00,
		'w5': 0x00,
		'w6': 0x00,
		'w7': 0x00,
		'w8': 0x00,
		'w9': 0x00,
		'e2': 0x00,
		'e3': 0x00,
		'e4': 0x00,
		'e5': 0x00,
		'e6': 0x00,
		'e7': 0x00,
		'e8': 0x00,
		'e9': 0x00,
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
		'nw2': 0x00,
		'nw3': 0x00,
		'nw4': 0x00,
		'nw5': 0x00,
		'nw6': 0x00,
		'nw7': 0x00,
		'nw8': 0x00,
		'nw9': 0x00,
		'ne2': 0x00,
		'ne3': 0x00,
		'ne4': 0x00,
		'ne5': 0x00,
		'ne6': 0x00,
		'ne7': 0x00,
		'ne8': 0x00,
		'ne9': 0x00,
		'sw2': 0x00,
		'sw3': 0x00,
		'sw4': 0x00,
		'sw5': 0x00,
		'sw6': 0x00,
		'sw7': 0x00,
		'sw8': 0x00,
		'sw9': 0x00,
		'se2': 0x00,
		'se3': 0x00,
		'se4': 0x00,
		'se5': 0x00,
		'se6': 0x00,
		'se7': 0x00,
		'se8': 0x00,
		'se9': 0x00,
		'w+u2': 0x00,
		'w+u3': 0x00,
		'w+u4': 0x00,
		'w+u5': 0x00,
		'w+u6': 0x00,
		'w+u7': 0x00,
		'w+u8': 0x00,
		'w+u9': 0x00,
		'e+u2': 0x00,
		'e+u3': 0x00,
		'e+u4': 0x00,
		'e+u5': 0x00,
		'e+u6': 0x00,
		'e+u7': 0x00,
		'e+u8': 0x00,
		'e+u9': 0x00,
		'w+d2': 0x00,
		'w+d3': 0x00,
		'w+d4': 0x00,
		'w+d5': 0x00,
		'w+d6': 0x00,
		'w+d7': 0x00,
		'w+d8': 0x00,
		'w+d9': 0x00,
		'e+d2': 0x00,
		'e+d3': 0x00,
		'e+d4': 0x00,
		'e+d5': 0x00,
		'e+d6': 0x00,
		'e+d7': 0x00,
		'e+d8': 0x00,
		'e+d9': 0x00,
		'dialog': 0x00
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
		if button == 'l+a':
			self.btnCombo(0x41, 0x34)
		elif button == 'l+b':
			self.btnCombo(0x41, 0x35)
		elif button == 'l+r':
			self.btnCombo(0x41, 0x42)
		elif button == 'b+n':
			self.btnRun(0x30)
		elif button == 'b+s':
			self.btnRun(0x31)
		elif button == 'b+w':
			self.btnRun(0x32)
		elif button == 'b+e':
			self.btnRun(0x33)
		elif button == 'a+b':
			self.btnRun(0x34)
		elif button == 'b+nw':
			self.btnRunCombo(0x30, 0x32)
		elif button == 'b+ne':
			self.btnRunCombo(0x30, 0x33)
		elif button == 'b+sw':
			self.btnRunCombo(0x31, 0x32)
		elif button == 'b+se':
			self.btnRunCombo(0x31, 0x33)
		elif button == 'r+n':
			self.btnCombo(0x42, 0x30)
		elif button == 'r+s':
			self.btnCombo(0x42, 0x31)
		elif button == 'r+w':
			self.btnCombo(0x42, 0x32)
		elif button == 'r+e':
			self.btnCombo(0x42, 0x33)
		elif button == 'r+a':
			self.btnCombo(0x42, 0x34)
		elif button == 'nw':
			self.btnCombo(0x30, 0x32)
		elif button == 'ne':
			self.btnCombo(0x30, 0x33)
		elif button == 'sw':
			self.btnCombo(0x31, 0x32)
		elif button == 'se':
			self.btnCombo(0x31, 0x33)
		elif button == 'x+n':
			self.btnCombo(0x36, 0x30)
		elif button == 'x+s':
			self.btnCombo(0x36, 0x31)
		elif button == 'x+w':
			self.btnCombo(0x36, 0x32)
		elif button == 'x+e':
			self.btnCombo(0x36, 0x33)
		elif button == 'y+n':
			self.btnHoldCombo(0x37, 0x30)
		elif button == 'y+s':
			self.btnHoldCombo(0x37, 0x31)
		elif button == 'y+w':
			self.btnHoldCombo(0x37, 0x32)
		elif button == 'y+e':
			self.btnHoldCombo(0x37, 0x33)
		elif button == 'n2':
			self.btnLoop(0x30, 2)
		elif button == 'n3':
			self.btnLoop(0x30, 3)
		elif button == 'n4':
			self.btnLoop(0x30, 4)
		elif button == 'n5':
			self.btnLoop(0x30, 5)
		elif button == 'n6':
			self.btnLoop(0x30, 6)
		elif button == 'n7':
			self.btnLoop(0x30, 7)
		elif button == 'n8':
			self.btnLoop(0x30, 8)
		elif button == 'n9':
			self.btnLoop(0x30, 9)
		elif button == 's2':
			self.btnLoop(0x31, 2)
		elif button == 's3':
			self.btnLoop(0x31, 3)
		elif button == 's4':
			self.btnLoop(0x31, 4)
		elif button == 's5':
			self.btnLoop(0x31, 5)
		elif button == 's6':
			self.btnLoop(0x31, 6)
		elif button == 's7':
			self.btnLoop(0x31, 7)
		elif button == 's8':
			self.btnLoop(0x31, 8)
		elif button == 's9':
			self.btnLoop(0x31, 9)
		elif button == 'w2':
			self.btnLoop(0x32, 2)
		elif button == 'w3':
			self.btnLoop(0x32, 3)
		elif button == 'w4':
			self.btnLoop(0x32, 4)
		elif button == 'w5':
			self.btnLoop(0x32, 5)
		elif button == 'w6':
			self.btnLoop(0x32, 6)
		elif button == 'w7':
			self.btnLoop(0x32, 7)
		elif button == 'w8':
			self.btnLoop(0x32, 8)
		elif button == 'w9':
			self.btnLoop(0x32, 9)
		elif button == 'e2':
			self.btnLoop(0x33, 2)
		elif button == 'e3':
			self.btnLoop(0x33, 3)
		elif button == 'e4':
			self.btnLoop(0x33, 4)
		elif button == 'e5':
			self.btnLoop(0x33, 5)
		elif button == 'e6':
			self.btnLoop(0x33, 6)
		elif button == 'e7':
			self.btnLoop(0x33, 7)
		elif button == 'e8':
			self.btnLoop(0x33, 8)
		elif button == 'e9':
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
		elif button == 'nw2':
			self.btnLoopCombo(0x30, 0x32, 2)
		elif button == 'nw3':
			self.btnLoopCombo(0x30, 0x32, 3)
		elif button == 'nw4':
			self.btnLoopCombo(0x30, 0x32, 4)
		elif button == 'nw5':
			self.btnLoopCombo(0x30, 0x32, 5)
		elif button == 'nw6':
			self.btnLoopCombo(0x30, 0x32, 6)
		elif button == 'nw7':
			self.btnLoopCombo(0x30, 0x32, 7)
		elif button == 'nw8':
			self.btnLoopCombo(0x30, 0x32, 8)
		elif button == 'nw9':
			self.btnLoopCombo(0x30, 0x32, 9)
		elif button == 'ne2':
			self.btnLoopCombo(0x30, 0x33, 2)
		elif button == 'ne3':
			self.btnLoopCombo(0x30, 0x33, 3)
		elif button == 'ne4':
			self.btnLoopCombo(0x30, 0x33, 4)
		elif button == 'ne5':
			self.btnLoopCombo(0x30, 0x33, 5)
		elif button == 'ne6':
			self.btnLoopCombo(0x30, 0x33, 6)
		elif button == 'ne7':
			self.btnLoopCombo(0x30, 0x33, 7)
		elif button == 'ne8':
			self.btnLoopCombo(0x30, 0x33, 8)
		elif button == 'ne9':
			self.btnLoopCombo(0x30, 0x33, 9)
		elif button == 'sw2':
			self.btnLoopCombo(0x31, 0x32, 2)
		elif button == 'sw3':
			self.btnLoopCombo(0x31, 0x32, 3)
		elif button == 'sw4':
			self.btnLoopCombo(0x31, 0x32, 4)
		elif button == 'sw5':
			self.btnLoopCombo(0x31, 0x32, 5)
		elif button == 'sw6':
			self.btnLoopCombo(0x31, 0x32, 6)
		elif button == 'sw7':
			self.btnLoopCombo(0x31, 0x32, 7)
		elif button == 'sw8':
			self.btnLoopCombo(0x31, 0x32, 8)
		elif button == 'sw9':
			self.btnLoopCombo(0x31, 0x32, 9)
		elif button == 'se2':
			self.btnLoopCombo(0x31, 0x33, 2)
		elif button == 'se3':
			self.btnLoopCombo(0x31, 0x33, 3)
		elif button == 'se4':
			self.btnLoopCombo(0x31, 0x33, 4)
		elif button == 'se5':
			self.btnLoopCombo(0x31, 0x33, 5)
		elif button == 'se6':
			self.btnLoopCombo(0x31, 0x33, 6)
		elif button == 'se7':
			self.btnLoopCombo(0x31, 0x33, 7)
		elif button == 'se8':
			self.btnLoopCombo(0x31, 0x33, 8)
		elif button == 'se9':
			self.btnLoopCombo(0x31, 0x33, 9)
		elif button == 'dialog':
			self.btnLoop(0x34, 25)
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
