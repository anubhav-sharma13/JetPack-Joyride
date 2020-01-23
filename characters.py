import numpy as np
import colorama
from colorama import Fore,Back,Style
import os
from background import *
colorama.init()
class Obstacles:
	def __init__(self,size,temp):
		self.size=int(size)
		self.temp=temp
	def Straight(self):
		for i in range(self.size):
			self.temp[i][0]='|'
			self.temp[i][1]='|'
		return self.temp
	def Horizontal(self):
		for i in range(self.size):
			self.temp[0][i]='-'
			self.temp[1][i]='-'
		return self.temp
	def Cleaner (self):
		for i in range(self.size-1):
			for j in range(self.size-1):
				self.temp[i][j]=" "
	def Printarr (self):
		for i in range(self.size):
			for j in range(self.size):
				print(self.temp[i][j],end="")
			print()
#here I have used polymorphism
class Slant(Obstacles):
	def __init__(self,size,temp,direction):
		super().__init__(size,temp)
		self.direction=direction
	def make_slant(self):
		if self.direction=="left":
			for i in range(self.size):
				for j in range(self.size-1):
					if i==j:
						self.temp[i][j]="\\"
						self.temp[i][j+1]="\\"
		elif self.direction=="right":
			for i in range(self.size):
				for j in range(self.size-1):
					if i==self.size-1-j:
						self.temp[i][j]="/"
						self.temp[i][j+1]="/"
		return self.temp
	def Cleaner (self):
		for i in range(self.size):
			for j in range(self.size):
				self.temp[i][j]=" "

class coins():
	def __init__(self,size,char):
		self.size=size
		self.char=char
	def make_coin(self,inp_row,inp_col):
		for i in range(self.size):
			for j in range(self.size):
				if inp[inp_row+i][inp_col+j]==" ":
					inp[inp_row+i][inp_col+j]='$'
				else:
					continue

class bullet():
	jump=4
	life_flag=0
	def __init__(self,xcordinate,ycordinate,symbol):
		self.xcordinate=xcordinate
		self.ycordinate=ycordinate
		self.symbol=symbol

	def make_bullet(self):
		inp[self.xcordinate+1][self.ycordinate+1]=self.symbol

	def clear_bullet(self):
		if inp[self.xcordinate][self.ycordinate]=='$':
			inp[self.xcordinate][self.ycordinate]=='$'
		else:
			inp[self.xcordinate][self.ycordinate]=" "

	def move_bullet(self):
		if inp[self.xcordinate][self.ycordinate+self.jump]=='$':
			inp[self.xcordinate][self.ycordinate+self.jump]="$"
		else:
			inp[self.xcordinate][self.ycordinate+self.jump]=self.symbol

	def destroy(self):

		tempo=min(row-self.xcordinate,10)

		for i in range(tempo):
			for j in range(10):
				if inp[self.xcordinate+i][self.ycordinate+j]=='/' or inp[self.xcordinate+i][self.ycordinate+j]=='\\' or inp[self.xcordinate+i][self.ycordinate+j] =='|' or inp[self.xcordinate+i][self.ycordinate+j] == '-':
					inp[self.xcordinate+i][self.ycordinate+j]=' '
					self.life_flag=1

		tempo2=min(self.xcordinate-5,10)

		for i in range(tempo2):
				for j in range(10):
					if inp[self.xcordinate+i-10][self.ycordinate+j]=='/' or inp[self.xcordinate+i-10][self.ycordinate+j]=='\\' or inp[self.xcordinate+i-10][self.ycordinate+j] =='|' or inp[self.xcordinate+i-10][self.ycordinate+j] == '-':
						inp[self.xcordinate+i-10][self.ycordinate+j]=' '
						self.life_flag=1

		for i in range(tempo):
			for j in range(10):
				if inp[self.xcordinate+i][self.ycordinate+j-10]=='/' or inp[self.xcordinate+i][self.ycordinate+j-10]=='\\' or inp[self.xcordinate+i][self.ycordinate+j-10] =='|' or inp[self.xcordinate+i][self.ycordinate+j-10] == '-':
					inp[self.xcordinate+i][self.ycordinate+j-10]=" "
					self.life_flag=1

		for i in range(tempo2):
				for j in range(10):
					if inp[self.xcordinate+i-10][self.ycordinate+j+10]=='/' or inp[self.xcordinate+i-10][self.ycordinate+j+10]=='\\' or inp[self.xcordinate+i-10][self.ycordinate+j+10] =='|' or inp[self.xcordinate+i-10][self.ycordinate+j+10] == '-':
						inp[self.xcordinate+i-10][self.ycordinate+j+10]=' '
						self.life_flag=1

		for i in range(tempo):
			for j in range(10):
				if inp[self.xcordinate+i][self.ycordinate+j+10]=='/' or inp[self.xcordinate+i][self.ycordinate+j+10]=='\\' or inp[self.xcordinate+i][self.ycordinate+j+10] =='|' or inp[self.xcordinate+i][self.ycordinate+j+10] == '-':
					inp[self.xcordinate+i][self.ycordinate+j+10]=" "
					self.life_flag=1

		for i in range(tempo2):
				for j in range(10):
					if inp[self.xcordinate+i-10][self.ycordinate+j-10]=='/' or inp[self.xcordinate+i-10][self.ycordinate+j-10]=='\\' or inp[self.xcordinate+i-10][self.ycordinate+j-10] =='|' or inp[self.xcordinate+i-10][self.ycordinate+j-10] == '-':
						inp[self.xcordinate+i-10][self.ycordinate+j-10]=' '
						self.life_flag=1


	def destroy_inpath(self):
		for i in range(self.jump):
			if inp[self.xcordinate][self.ycordinate+i]=='\\' or inp[self.xcordinate][self.ycordinate+i]=='/' or inp[self.xcordinate][self.ycordinate+i]=='|' or inp[self.xcordinate][self.ycordinate+i]=='-':
				self.destroy()













