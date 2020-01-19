import numpy as np
import colorama
from colorama import Fore,Back,Style
import os
import random
from background import *
from characters import *
from functionality import *


for i in range(20000):
	obj1=On_screen(row,i,(col+i),inp)
	obj1.sky('@')
#	print(type(inp))
	obj1.ground('$')
	x_obj=random.randint(0,5)
#	print(x_obj)
	if (x_obj==0):
#		print(type(inp))
		temp=np.full((10,10),' ')
		obj2=Slant(10,temp,"left")
		temp=obj2.Straight()
		x_rows=random.randint(6,row-13)
		y_rows=random.randrange(col-10+i,col*60,5)
		obj3=render(x_rows,y_rows,10,temp,inp)
		obj3.placement()
	elif (x_obj==1):
		temp=np.full((10,10),' ')
		obj2=Slant(10,temp,"left")
		temp=obj2.Horizontal()
		x_rows=random.randint(6,row-13)
		y_rows=random.randrange(col-10+i,col*60,5)
		obj3=render(x_rows,y_rows,10,temp,inp)
		obj3.placement()
	elif (x_obj==2):
		temp=np.full((10,10),' ')
		obj2=Slant(10,temp,"left")
		temp=obj2.make_slant()
		x_rows=random.randint(6,row-13)
		y_rows=random.randrange(col-10+i,col*60,5)
		obj3=render(x_rows,y_rows,10,temp,inp)
		obj3.placement()
	else:
		temp=np.full((10,10),' ')
		obj2=Slant(10,temp,"right")
		temp=obj2.make_slant()
		x_rows=random.randint(6,row-13)
		y_rows=random.randrange(col-10+i,col*60,5)
		obj3=render(x_rows,y_rows,10,temp,inp)
		obj3.placement()


	obj1.printsky()
	obj1.printbody()
	obj1.printground()
	print('\033[H',end="",flush='True')	
	time.sleep(0.05)






