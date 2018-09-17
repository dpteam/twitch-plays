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
		'l+a': 0x00,
		'l+r': 0x00,
		'a+b': 0x00,
		'b+up': 0x00,
		'b+down': 0x00,
		'b+left': 0x00,
		'b+right': 0x00,
		'r+up': 0x00,
		'r+down': 0x00,
		'r+left': 0x00,
		'r+right': 0x00,
		'y+up': 0x00,
		'y+down': 0x00,
		'y+left': 0x00,
		'y+right': 0x00,
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
		'b9': 0x00
	}

	def get_valid_buttons(self):
		return [button for button in self.keymap.keys()]

	def is_valid_button(self, button):
		return button in self.keymap.keys()

	def button_to_key(self, button):
		return self.keymap[button]

	def push_button(self, button):
		# How much elifs does it take to disorient a programmer?
		# Too many to count
		
		loopCntr=0
		
		if button == 'l+a':
			win32api.keybd_event(0x41, 0, 0, 0)
			win32api.keybd_event(0x34, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x34, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'l+r':
			win32api.keybd_event(0x41, 0, 0, 0)
			win32api.keybd_event(0x42, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x42, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'a+b':
			win32api.keybd_event(0x34, 0, 0, 0)
			win32api.keybd_event(0x35, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(0x34, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'b+up':
			win32api.keybd_event(0x35, 0, 0, 0)
			win32api.keybd_event(0x30, 0, 0, 0)
			time.sleep(3)
			win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x30, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'b+down':
			win32api.keybd_event(0x35, 0, 0, 0)
			win32api.keybd_event(0x31, 0, 0, 0)
			time.sleep(3)
			win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'b+left':
			win32api.keybd_event(0x35, 0, 0, 0)
			win32api.keybd_event(0x32, 0, 0, 0)
			time.sleep(3)
			win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x32, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'b+right':
			win32api.keybd_event(0x35, 0, 0, 0)
			win32api.keybd_event(0x33, 0, 0, 0)
			time.sleep(3)
			win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x33, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'r+up':
			win32api.keybd_event(0x42, 0, 0, 0)
			win32api.keybd_event(0x30, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(0x42, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x30, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'r+down':
			win32api.keybd_event(0x42, 0, 0, 0)
			win32api.keybd_event(0x31, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(0x42, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'r+left':
			win32api.keybd_event(0x42, 0, 0, 0)
			win32api.keybd_event(0x32, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(0x42, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x32, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'r+right':
			win32api.keybd_event(0x42, 0, 0, 0)
			win32api.keybd_event(0x33, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(0x42, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x33, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'y+up':
			win32api.keybd_event(0x37, 0, 0, 0)
			win32api.keybd_event(0x30, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(0x37, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x30, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'y+down':
			win32api.keybd_event(0x37, 0, 0, 0)
			win32api.keybd_event(0x31, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(0x37, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'y+left':
			win32api.keybd_event(0x37, 0, 0, 0)
			win32api.keybd_event(0x32, 0, 0, 0)
			time.sleep(.15)
			 win32api.keybd_event(0x37, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x32, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'y+right':
			win32api.keybd_event(0x37, 0, 0, 0)
			win32api.keybd_event(0x33, 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(0x37, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x33, 0, win32con.KEYEVENTF_KEYUP, 0)
		elif button == 'up2':
			while loopCntr < 2:
				win32api.keybd_event(0x30, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x30, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'up3':
			while loopCntr < 3:
				win32api.keybd_event(0x30, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x30, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'up4':
			while loopCntr < 4:
				win32api.keybd_event(0x30, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x30, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'up5':
			while loopCntr < 5:
				win32api.keybd_event(0x30, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x30, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'up6':
			while loopCntr < 6:
				win32api.keybd_event(0x30, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x30, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'up7':
			while loopCntr < 7:
				win32api.keybd_event(0x30, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x30, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'up8':
			while loopCntr < 8:
				win32api.keybd_event(0x30, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x30, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'up9':
			while loopCntr < 9:
				win32api.keybd_event(0x30, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x30, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'down2':
			while loopCntr < 2:
				win32api.keybd_event(0x31, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'down3':
			while loopCntr < 3:
				win32api.keybd_event(0x31, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'down4':
			while loopCntr < 4:
				win32api.keybd_event(0x31, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'down5':
			while loopCntr < 5:
				win32api.keybd_event(0x31, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'down6':
			while loopCntr < 6:
				win32api.keybd_event(0x31, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'down7':
			while loopCntr < 7:
				win32api.keybd_event(0x31, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'down8':
			while loopCntr < 8:
				win32api.keybd_event(0x31, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'down9':
			while loopCntr < 9:
				win32api.keybd_event(0x31, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'left2':
			while loopCntr < 2:
				win32api.keybd_event(0x32, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x32, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'left3':
			while loopCntr < 3:
				win32api.keybd_event(0x32, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x32, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'left4':
			while loopCntr < 4:
				win32api.keybd_event(0x32, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x32, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'left5':
			while loopCntr < 5:
				win32api.keybd_event(0x32, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x32, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'left6':
			while loopCntr < 6:
				win32api.keybd_event(0x32, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x32, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'left7':
			while loopCntr < 7:
				win32api.keybd_event(0x32, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x32, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'left8':
			while loopCntr < 8:
				win32api.keybd_event(0x32, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x32, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'left9':
			while loopCntr < 9:
				win32api.keybd_event(0x32, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x32, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'right2':
			while loopCntr < 2:
				win32api.keybd_event(0x33, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x33, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'right3':
			while loopCntr < 3:
				win32api.keybd_event(0x33, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x33, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'right4':
			while loopCntr < 4:
				win32api.keybd_event(0x33, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x33, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'right5':
			while loopCntr < 5:
				win32api.keybd_event(0x33, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x33, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'right6':
			while loopCntr < 6:
				win32api.keybd_event(0x33, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x33, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'right7':
			while loopCntr < 7:
				win32api.keybd_event(0x33, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x33, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'right8':
			while loopCntr < 8:
				win32api.keybd_event(0x33, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x33, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'right9':
			while loopCntr < 9:
				win32api.keybd_event(0x33, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x33, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'a2':
			while loopCntr < 2:
				win32api.keybd_event(0x34, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x34, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'a3':
			while loopCntr < 3:
				win32api.keybd_event(0x34, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x34, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'a4':
			while loopCntr < 4:
				win32api.keybd_event(0x34, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x34, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'a5':
			while loopCntr < 5:
				win32api.keybd_event(0x34, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x34, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'a6':
			while loopCntr < 6:
				win32api.keybd_event(0x34, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x34, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'a7':
			while loopCntr < 7:
				win32api.keybd_event(0x34, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x34, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'a8':
			while loopCntr < 8:
				win32api.keybd_event(0x34, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x34, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'a9':
			while loopCntr < 9:
				win32api.keybd_event(0x34, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x34, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'b2':
			while loopCntr < 2:
				win32api.keybd_event(0x35, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'b3':
			while loopCntr < 3:
				win32api.keybd_event(0x35, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'b4':
			while loopCntr < 4:
				win32api.keybd_event(0x35, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'b5':
			while loopCntr < 5:
				win32api.keybd_event(0x35, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'b6':
			while loopCntr < 6:
				win32api.keybd_event(0x35, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'b7':
			while loopCntr < 7:
				win32api.keybd_event(0x35, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'b8':
			while loopCntr < 8:
				win32api.keybd_event(0x35, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		elif button == 'b9':
			while loopCntr < 9:
				win32api.keybd_event(0x35, 0, 0, 0)
				time.sleep(.15)
				win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
				time.sleep(.5)
				loopCntr+=1
		else:
			win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
			time.sleep(.15)
			win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
