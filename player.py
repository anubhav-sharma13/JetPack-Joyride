import signal
from getch import _getChUnix as getChar
import numpy as np
import random
from alarmexception import *
from functionality import *
from background import *
from detect import *
import time
class Magnet():
	def __init__(self,char1,char2):
		self.char1=char1
		self.char2=char2
	#mag_arr=np.full((2,10)," ")
	mag_arr=[]
	def make_magnet(self):
		for i in range(5):
			rand_x=random.randint(7,30)
			rand_y=random.randrange(150,5000,200)
			self.mag_arr.append([rand_x,rand_y])
			inp[rand_x][rand_y+0]=self.char1
			inp[rand_x][rand_y+1]=self.char2


obj8=Magnet("M","M")
obj8.make_magnet()

class Player:
	man = [['O','O','O'],['<','|','>'],['/',' ','\\']]
	lives=4
	grav_factor=0
	coins=0
	nitros_flag=0
	nitros_time=0
	shield_flag=0
	shield_time=0
	shield_permission=1
	nitros_permission=1
	step=1

	def __init__(self,name,xcordi,ycordi,weight):
		self.name=name
		self.xcordi=xcordi
		self.ycordi=ycordi
		self.weight=weight

	def render_player(self):
		obj5=render(self.xcordi,self.ycordi,3,self.man,inp)
		obj5.placement()
	# def check_player(self):
	# 	for i in range(3):
	#		for j in range(3):
	# 			if inp[self.xcordi+i][self.ycordi+j]=="$":
	# 				self.increase_coin()

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

		for i in obj8.mag_arr:
			if i[1]-self.ycordi<30 and i[1]-self.ycordi > 0:
				self.clear_player()
				self.ycordi=self.ycordi+4
				detector = detect_things(self.xcordi, self.ycordi)
				detector.detect_coins(self)
				detector.detect_obstacles(self)
				detector.break_obstacles(self)
				obj5=render(self.xcordi,self.ycordi,3,self.man,inp)
				obj5.placement()
				del detector
			if self.ycordi - i[1] < 30 and self.ycordi - i[1] > 0:
				self.clear_player()
				self.ycordi=self.ycordi-3
				detector = detect_things(self.xcordi, self.ycordi)
				detector.detect_coins(self)
				detector.detect_obstacles(self)
				detector.break_obstacles(self)
				obj5=render(self.xcordi,self.ycordi,3,self.man,inp)
				obj5.placement()
				del detector



		if char=='q':
			quit()

		if char=='w' and self.xcordi>7:
			self.clear_player()
			if self.nitros_flag==0:
				self.xcordi=self.xcordi-3
			else:
				self.xcordi=self.xcordi-3
			detector = detect_things(self.xcordi, self.ycordi)
			detector.detect_coins(self)
			detector.detect_obstacles(self)
			detector.break_obstacles(self)
			#self.check_player()
			obj5=render(self.xcordi,self.ycordi,3,self.man,inp)
			obj5.placement()
			del detector
			self.grav_factor=0

		if char=='d' and self.ycordi< final_c-4:
			self.clear_player()
			if self.nitros_flag==0:
			 	self.ycordi=self.ycordi+4
			else:
			 	self.ycordi=self.ycordi+6
			detector = detect_things(self.xcordi, self.ycordi)
			detector.detect_coins(self)
			detector.detect_obstacles(self)
			detector.break_obstacles(self)
			obj5=render(self.xcordi,self.ycordi,3,self.man,inp)
			obj5.placement()
			del detector
			self.grav_factor=1
		#move left with the condition
		if char=='a' and self.ycordi>init_c+2:
			self.clear_player()
			self.ycordi=self.ycordi-3
			detector = detect_things(self.xcordi, self.ycordi)
			detector.detect_coins(self)
			detector.detect_obstacles(self)
			detector.break_obstacles(self)
			obj5=render(self.xcordi,self.ycordi,3,self.man,inp)
			obj5.placement()
			del detector
			self.grav_factor=0

		#activate the shield
		if char==' ' and self.shield_permission==1:
			self.man=[[' ','O',' '],['<','|','>'],['/','|','\\']]
			self.shield_flag=1
			self.shield_time=time.time()
		if char=='n' and self.nitros_permission == 1 :
			self.nitros_time=time.time()
			self.nitros_flag=1
			self.step=3

		#Gravity
		if self.xcordi<row-6:
			self.clear_player()
			if self.grav_factor<8:
				self.grav_factor+=1
			else:
				self.grav_factor=1
			#self.xcordi=min(self.xcordi+self.grav_factor,row-6)
			tempo=0
			while(tempo<self.grav_factor):
				tempo+=1
				self.xcordi=min(self.xcordi+tempo,row-6)
				detector = detect_things(self.xcordi, self.ycordi)
				detector.detect_coins(self)
				detector.detect_obstacles(self)
				detector.break_obstacles(self)
			obj5=render(self.xcordi,self.ycordi,3,self.man,inp)
			obj5.placement()
			#del detector

	def position_player(self):
		return self.xcordi,self.ycordi
	def count_coin(self):
		return self.coins
	def increase_coin(self):
		self.coins+=1
		return int(self.coins)
	def decrease_life(self):
		self.lives-=1
	def count_life(self):
		return self.lives
	shield_flag=0




		







    