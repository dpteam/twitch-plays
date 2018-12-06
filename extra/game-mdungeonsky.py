import win32api
import win32con
import time

class Game:
	keymap = {
		# Comment out any button(s) that would be unused
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
		'r': 0x42,
		'save': 0x43,
		'l+a': 0x00,
		'l+r': 0x00,
		'a+b': 0x00,
		'b+up': 0x00,
		'b+down': 0x00,
		'b+left': 0x00,
		'b+right': 0x00,
		'b+uleft': 0x00,
		'b+uright': 0x00,
		'b+dleft': 0x00,
		'b+dright': 0x00,
		'r+a': 0x00,
		'r+up': 0x00,
		'r+down': 0x00,
		'r+left': 0x00,
		'r+right': 0x00,
		'x+up': 0x00,
		'x+down': 0x00,
		'x+left': 0x00,
		'x+right': 0x00,
		'y+up': 0x00,
		'y+down': 0x00,
		'y+left': 0x00,
		'y+right': 0x00,
		'u+left': 0x00,
		'u+right': 0x00,
		'd+left': 0x00,
		'd+right': 0x00,
		'up2': 0x00,
		'up3': 0x00,
		'up4': 0x00,
		'up5': 0x00,
		'up6': 0x00,
		'up7': 0x00,
		'up8': 0x00,
		'up9': 0x00,
		'down2': 0x00,
		'down3': 0x00,
		'down4': 0x00,
		'down5': 0x00,
		'down6': 0x00,
		'down7': 0x00,
		'down8': 0x00,
		'down9': 0x00,
		'left2': 0x00,
		'left3': 0x00,
		'left4': 0x00,
		'left5': 0x00,
		'left6': 0x00,
		'left7': 0x00,
		'left8': 0x00,
		'left9': 0x00,
		'right2': 0x00,
		'right3': 0x00,
		'right4': 0x00,
		'right5': 0x00,
		'right6': 0x00,
		'right7': 0x00,
		'right8': 0x00,
		'right9': 0x00,
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
		'u+left2': 0x00,
		'u+left3': 0x00,
		'u+left4': 0x00,
		'u+left5': 0x00,
		'u+left6': 0x00,
		'u+left7': 0x00,
		'u+left8': 0x00,
		'u+left9': 0x00,
		'u+right2': 0x00,
		'u+right3': 0x00,
		'u+right4': 0x00,
		'u+right5': 0x00,
		'u+right6': 0x00,
		'u+right7': 0x00,
		'u+right8': 0x00,
		'u+right9': 0x00,
		'd+left2': 0x00,
		'd+left3': 0x00,
		'd+left4': 0x00,
		'd+left5': 0x00,
		'd+left6': 0x00,
		'd+left7': 0x00,
		'd+left8': 0x00,
		'd+left9': 0x00,
		'd+right2': 0x00,
		'd+right3': 0x00,
		'd+right4': 0x00,
		'd+right5': 0x00,
		'd+right6': 0x00,
		'd+right7': 0x00,
		'd+right8': 0x00,
		'd+right9': 0x00
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
	def push_button(self, button):
		# How much elifs does it take to disorient a programmer?
		# Too many to count
		if button == 'l+a':
			self.btnCombo(0x41, 0x34)
		elif button == 'l+r':
			self.btnCombo(0x41, 0x42)
		elif button == 'a+b':
			self.btnCombo(0x34, 0x35)
		elif button == 'b+up':
			self.btnRun(0x30)
		elif button == 'b+down':
			self.btnRun(0x31)
		elif button == 'b+left':
			self.btnRun(0x32)
		elif button == 'b+right':
			self.btnRun(0x33)
		elif button == 'b+uleft':
			self.btnRunCombo(0x30, 0x32)
		elif button == 'b+uright':
			self.btnRunCombo(0x30, 0x33)
		elif button == 'b+dleft':
			self.btnRunCombo(0x31, 0x32)
		elif button == 'b+dright':
			self.btnRunCombo(0x31, 0x33)
		elif button == 'r+up':
			self.btnCombo(0x42, 0x30)
		elif button == 'r+down':
			self.btnCombo(0x42, 0x31)
		elif button == 'r+left':
			self.btnCombo(0x42, 0x32)
		elif button == 'r+right':
			self.btnCombo(0x42, 0x33)
		elif button == 'r+a':
			self.btnCombo(0x42, 0x34)
		elif button == 'u+left':
			self.btnCombo(0x30, 0x32)
		elif button == 'u+right':
			self.btnCombo(0x30, 0x33)
		elif button == 'd+left':
			self.btnCombo(0x31, 0x32)
		elif button == 'd+right':
			self.btnCombo(0x31, 0x33)
		elif button == 'x+up':
			self.btnCombo(0x36, 0x30)
		elif button == 'x+down':
			self.btnCombo(0x36, 0x31)
		elif button == 'x+left':
			self.btnCombo(0x36, 0x32)
		elif button == 'x+right':
			self.btnCombo(0x36, 0x33)
		elif button == 'y+up':
			self.btnCombo(0x37, 0x30)
		elif button == 'y+down':
			self.btnCombo(0x37, 0x31)
		elif button == 'y+left':
			self.btnCombo(0x37, 0x32)
		elif button == 'y+right':
			self.btnCombo(0x37, 0x33)
		elif button == 'up2':
			self.btnLoop(0x30, 2)
		elif button == 'up3':
			self.btnLoop(0x30, 3)
		elif button == 'up4':
			self.btnLoop(0x30, 4)
		elif button == 'up5':
			self.btnLoop(0x30, 5)
		elif button == 'up6':
			self.btnLoop(0x30, 6)
		elif button == 'up7':
			self.btnLoop(0x30, 7)
		elif button == 'up8':
			self.btnLoop(0x30, 8)
		elif button == 'up9':
			self.btnLoop(0x30, 9)
		elif button == 'down2':
			self.btnLoop(0x31, 2)
		elif button == 'down3':
			self.btnLoop(0x31, 3)
		elif button == 'down4':
			self.btnLoop(0x31, 4)
		elif button == 'down5':
			self.btnLoop(0x31, 5)
		elif button == 'down6':
			self.btnLoop(0x31, 6)
		elif button == 'down7':
			self.btnLoop(0x31, 7)
		elif button == 'down8':
			self.btnLoop(0x31, 8)
		elif button == 'down9':
			self.btnLoop(0x31, 9)
		elif button == 'left2':
			self.btnLoop(0x32, 2)
		elif button == 'left3':
			self.btnLoop(0x32, 3)
		elif button == 'left4':
			self.btnLoop(0x32, 4)
		elif button == 'left5':
			self.btnLoop(0x32, 5)
		elif button == 'left6':
			self.btnLoop(0x32, 6)
		elif button == 'left7':
			self.btnLoop(0x32, 7)
		elif button == 'left8':
			self.btnLoop(0x32, 8)
		elif button == 'left9':
			self.btnLoop(0x32, 9)
		elif button == 'right2':
			self.btnLoop(0x33, 2)
		elif button == 'right3':
			self.btnLoop(0x33, 3)
		elif button == 'right4':
			self.btnLoop(0x33, 4)
		elif button == 'right5':
			self.btnLoop(0x33, 5)
		elif button == 'right6':
			self.btnLoop(0x33, 6)
		elif button == 'right7':
			self.btnLoop(0x33, 7)
		elif button == 'right8':
			self.btnLoop(0x33, 8)
		elif button == 'right9':
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
		elif button == 'u+left2':
			self.btnLoopCombo(0x30, 0x32, 2)
		elif button == 'u+left3':
			self.btnLoopCombo(0x30, 0x32, 3)
		elif button == 'u+left4':
			self.btnLoopCombo(0x30, 0x32, 4)
		elif button == 'u+left5':
			self.btnLoopCombo(0x30, 0x32, 5)
		elif button == 'u+left6':
			self.btnLoopCombo(0x30, 0x32, 6)
		elif button == 'u+left7':
			self.btnLoopCombo(0x30, 0x32, 7)
		elif button == 'u+left8':
			self.btnLoopCombo(0x30, 0x32, 8)
		elif button == 'u+left9':
			self.btnLoopCombo(0x30, 0x32, 9)
		elif button == 'u+right2':
			self.btnLoopCombo(0x30, 0x33, 2)
		elif button == 'u+right3':
			self.btnLoopCombo(0x30, 0x33, 3)
		elif button == 'u+right4':
			self.btnLoopCombo(0x30, 0x33, 4)
		elif button == 'u+right5':
			self.btnLoopCombo(0x30, 0x33, 5)
		elif button == 'u+right6':
			self.btnLoopCombo(0x30, 0x33, 6)
		elif button == 'u+right7':
			self.btnLoopCombo(0x30, 0x33, 7)
		elif button == 'u+right8':
			self.btnLoopCombo(0x30, 0x33, 8)
		elif button == 'u+right9':
			self.btnLoopCombo(0x30, 0x33, 9)
		elif button == 'd+left2':
			self.btnLoopCombo(0x31, 0x32, 2)
		elif button == 'd+left3':
			self.btnLoopCombo(0x31, 0x32, 3)
		elif button == 'd+left4':
			self.btnLoopCombo(0x31, 0x32, 4)
		elif button == 'd+left5':
			self.btnLoopCombo(0x31, 0x32, 5)
		elif button == 'd+left6':
			self.btnLoopCombo(0x31, 0x32, 6)
		elif button == 'd+left7':
			self.btnLoopCombo(0x31, 0x32, 7)
		elif button == 'd+left8':
			self.btnLoopCombo(0x31, 0x32, 8)
		elif button == 'd+left9':
			self.btnLoopCombo(0x31, 0x32, 9)
		elif button == 'd+right2':
			self.btnLoopCombo(0x31, 0x33, 2)
		elif button == 'd+right3':
			self.btnLoopCombo(0x31, 0x33, 3)
		elif button == 'd+right4':
			self.btnLoopCombo(0x31, 0x33, 4)
		elif button == 'd+right5':
			self.btnLoopCombo(0x31, 0x33, 5)
		elif button == 'd+right6':
			self.btnLoopCombo(0x31, 0x33, 6)
		elif button == 'd+right7':
			self.btnLoopCombo(0x31, 0x33, 7)
		elif button == 'd+right8':
			self.btnLoopCombo(0x31, 0x33, 8)
		elif button == 'd+right9':
			self.btnLoopCombo(0x31, 0x33, 9)
		else:
			win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
