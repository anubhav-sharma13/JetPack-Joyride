import signal
from getch import _getChUnix as getChar
import numpy as np
from alarmexception import *
from functionality import *
from background import *


class Player:
	man = [['O','O','O'],['<','|','>'],['/',' ','\\']]
	shield = [[' ','O',' ',' ','\\'],['<','|','>','-','|'],['/',' ','\\',' ','/']]
	lives=1
	grav_factor=0

	def __init__(self,name,xcordi,ycordi,weight):
		self.name=name
		self.xcordi=xcordi
		self.ycordi=ycordi
		self.weight=weight

	def render_player(self):
		#print(self.man)
		obj5=render(self.xcordi,self.ycordi,3,self.man,inp)
		obj5.placement()

	def clear_player(self):
		clr=np.full((3,3)," ")
		obj5=render(self.xcordi,self.ycordi,3,clr,inp)
		obj5.placement()
	def move_player(self,init_c,final_c):


		def alarmhandler(signum, frame):
			raise AlarmException

		def user_input(timeout=0.1):
			signal.signal(signal.SIGALRM, alarmhandler)
			signal.setitimer(signal.ITIMER_REAL, timeout)
			try:
				text = getChar()()
				signal.alarm(0)
				return text
			except AlarmException:
				pass
			signal.signal(signal.SIGALRM, signal.SIG_IGN)
			return ''

		char=user_input()

		if self.ycordi<init_c+1:
			self.clear_player()
			self.ycordi=init_c+1
			obj5=render(self.xcordi,self.ycordi,3,self.man,inp)
			obj5.placement()


		if char=='q':
			quit()

		if char=='w' and self.xcordi>7:
			self.clear_player()
			self.xcordi=self.xcordi-3
			obj5=render(self.xcordi,self.ycordi,3,self.man,inp)
			obj5.placement()
			self.grav_factor=0

		if char=='d' and self.ycordi< final_c-4:
			self.clear_player()
			self.ycordi=self.ycordi+4
			obj5=render(self.xcordi,self.ycordi,3,self.man,inp)
			obj5.placement()
			self.grav_factor=0
		#move left with the condition
		if char=='a' and self.ycordi>init_c+2:
			self.clear_player()
			self.ycordi=self.ycordi-2
			obj5=render(self.xcordi,self.ycordi,3,self.man,inp)
			obj5.placement()
			self.grav_factor=0

		#Gravity
		if self.xcordi<row-6:
			self.clear_player()
			if self.grav_factor<8:
				self.grav_factor+=1
			else:
				self.grav_factor=1
			self.xcordi=min(self.xcordi+self.grav_factor,row-6)
			obj5=render(self.xcordi,self.ycordi,3,self.man,inp)
			obj5.placement()


		







    