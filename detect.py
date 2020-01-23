import numpy as np
import colorama
from colorama import Fore,Back,Style
import os
import random
from background import *
from characters import *
from player import *

class detect_things():
	def __init__(self,position_x,position_y):
		self.position_y=position_y
		self.position_x=position_x
	def detect_coins(self, obj):
		for i in range(3):
			for j in range(3):
				if inp[self.position_x+i][self.position_y+j]=='$':
					obj.increase_coin()
	def detect_nitros(self,obj):
		for i in range(3):
			for j in range(3):
				pass
			#	if inp[self.position_x+i][self.position_y+j]=='N':

	def detect_obstacles(self,obj):
		ft=0
		if ft==0:
			for i in range(5):
				for j in range(5):
					if inp[self.position_x+i][self.position_y+j]=='/' or inp[self.position_x+i][self.position_y+j]=='\\' or inp[self.position_x+i][self.position_y+j] =='|' or inp[self.position_x+i][self.position_y+j] == '-':
						if obj.shield_flag==0 and ft==0 :
							obj.decrease_life()
							obj.xcordi=10
							obj.ycordi+=10
							ft=1
		if ft==1:
			tempo=min(row-self.position_x,10)
			for i in range(tempo):
				for j in range(10):
					if inp[self.position_x+i][self.position_y+j]=='/' or inp[self.position_x+i][self.position_y+j]=='\\' or inp[self.position_x+i][self.position_y+j] =='|' or inp[self.position_x+i][self.position_y+j] == '-':
						inp[self.position_x+i][self.position_y+j]=' '

			tempo2=min(self.position_x,10)
			for i in range(tempo2):
					for j in range(10):
						if inp[self.position_x+i-10][self.position_y+j]=='/' or inp[self.position_x+i-10][self.position_y+j]=='\\' or inp[self.position_x+i-10][self.position_y+j] =='|' or inp[self.position_x+i-10][self.position_y+j] == '-':
							inp[self.position_x+i-10][self.position_y+j]=' '

			for i in range(tempo):
				for j in range(10):
					if inp[self.position_x+i][self.position_y+j-10]=='/' or inp[self.position_x+i][self.position_y+j-10]=='\\' or inp[self.position_x+i][self.position_y+j-10] =='|' or inp[self.position_x+i][self.position_y+j-10] == '-':
						inp[self.position_x+i][self.position_y+j-10]=" "

			for i in range(tempo2):
					for j in range(10):
						if inp[self.position_x+i-10][self.position_y+j+10]=='/' or inp[self.position_x+i-10][self.position_y+j+10]=='\\' or inp[self.position_x+i-10][self.position_y+j+10] =='|' or inp[self.position_x+i-10][self.position_y+j+10] == '-':
							inp[self.position_x+i-10][self.position_y+j+10]=' '

			for i in range(tempo):
				for j in range(10):
					if inp[self.position_x+i][self.position_y+j+10]=='/' or inp[self.position_x+i][self.position_y+j+10]=='\\' or inp[self.position_x+i][self.position_y+j+10] =='|' or inp[self.position_x+i][self.position_y+j+10] == '-':
						inp[self.position_x+i][self.position_y+j+10]=" "
			for i in range(tempo2):
					for j in range(10):
						if inp[self.position_x+i-10][self.position_y+j-10]=='/' or inp[self.position_x+i-10][self.position_y+j-10]=='\\' or inp[self.position_x+i-10][self.position_y+j-10] =='|' or inp[self.position_x+i-10][self.position_y+j-10] == '-':
							inp[self.position_x+i-10][self.position_y+j-10]=' '

	def break_obstacles(self,obj):
		l_flag=0
		for i in range(5):
			for j in range(5):
				if inp[self.position_x+i][self.position_y+j]=='/' or inp[self.position_x+i][self.position_y+j]=='\\' or inp[self.position_x+i][self.position_y+j] =='|' or inp[self.position_x+i][self.position_y+j] == '-':
					if obj.shield_flag==1:
						l_flag=1
		if l_flag==1:
			tempo=min(row-self.position_x,10)
			for i in range(tempo):
				for j in range(10):
					if inp[self.position_x+i][self.position_y+j]=='/' or inp[self.position_x+i][self.position_y+j]=='\\' or inp[self.position_x+i][self.position_y+j] =='|' or inp[self.position_x+i][self.position_y+j] == '-':
						inp[self.position_x+i][self.position_y+j]=' '

			tempo2=min(self.position_x,10)
			for i in range(tempo2):
					for j in range(10):
						if inp[self.position_x+i-10][self.position_y+j]=='/' or inp[self.position_x+i-10][self.position_y+j]=='\\' or inp[self.position_x+i-10][self.position_y+j] =='|' or inp[self.position_x+i-10][self.position_y+j] == '-':
							inp[self.position_x+i-10][self.position_y+j]=' '

			for i in range(tempo):
				for j in range(10):
					if inp[self.position_x+i][self.position_y+j-10]=='/' or inp[self.position_x+i][self.position_y+j-10]=='\\' or inp[self.position_x+i][self.position_y+j-10] =='|' or inp[self.position_x+i][self.position_y+j-10] == '-':
						inp[self.position_x+i][self.position_y+j-10]=" "

			for i in range(tempo2):
					for j in range(10):
						if inp[self.position_x+i-10][self.position_y+j+10]=='/' or inp[self.position_x+i-10][self.position_y+j+10]=='\\' or inp[self.position_x+i-10][self.position_y+j+10] =='|' or inp[self.position_x+i-10][self.position_y+j+10] == '-':
							inp[self.position_x+i-10][self.position_y+j+10]=' '

			for i in range(tempo):
				for j in range(10):
					if inp[self.position_x+i][self.position_y+j+10]=='/' or inp[self.position_x+i][self.position_y+j+10]=='\\' or inp[self.position_x+i][self.position_y+j+10] =='|' or inp[self.position_x+i][self.position_y+j+10] == '-':
						inp[self.position_x+i][self.position_y+j+10]=" "
			for i in range(tempo2):
					for j in range(10):
						if inp[self.position_x+i-10][self.position_y+j-10]=='/' or inp[self.position_x+i-10][self.position_y+j-10]=='\\' or inp[self.position_x+i-10][self.position_y+j-10] =='|' or inp[self.position_x+i-10][self.position_y+j-10] == '-':
							inp[self.position_x+i-10][self.position_y+j-10]=' '



				
	







