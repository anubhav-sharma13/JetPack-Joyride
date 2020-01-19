import numpy as np
import colorama
from colorama import Fore,Back,Style
import os

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
		for i in range(self.size):
			for j in range(self.size):
				self.inp[i][j]=" "
	def Printarr (self):
		for i in range(self.size):
			for j in range(self.size):
				print(self.temp[i][j],end="")
			print()
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

#obj.make_slant()
#temp=obj3.Straight()
#obj.Horizontal()
#obj.Printarr()









