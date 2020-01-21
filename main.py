import numpy as np
import colorama
from colorama import Fore,Back,Style
import os
import random
from background import *
from characters import *
from functionality import *
from player import *


#object for the player
obj4=Player("Mando",24,30,10)
#this is the loop for obstacles
for i in range(10,col*99,55):
	seed=random.randint(0,3)
#	print(seed)
#		print(type(inp))
	if (seed==0):
		obs=np.full((10,10),' ')
		obj2=Slant(10,obs,"left")
		obs=obj2.Straight()
		x_obs=random.randint(6,row-13)
		x_coin=random.randint(6,row-13)
		y_obs=random.randrange(i,i+30)
		y_coin=random.randrange(i,i+30)
		obj3=render(x_obs,y_obs,10,obs,inp)
		obj3.placement()
		obj2.Cleaner()
		obj6=coins(5,'$')
		obj6.make_coin(x_coin,y_coin)
	elif (seed==1):
		obs=np.full((10,10),' ')
		obj2=Slant(10,obs,"left")
		obs=obj2.Horizontal()
		x_obs=random.randint(6,row-13)
		x_coin=random.randint(6,row-13)
		y_obs=random.randrange(i,i+30)
		y_coin=random.randrange(i,i+30)
		obj3=render(x_obs,y_obs,10,obs,inp)
		obj3.placement()
		obj2.Cleaner()
		obj6=coins(5,'$')
		obj6.make_coin(x_coin,y_coin)
	elif (seed==2):
		obs=np.full((10,10),' ')
		obj2=Slant(10,obs,"left")
		obs=obj2.make_slant()
		x_obs=random.randint(6,row-13)
		x_coin=random.randint(6,row-13)
		y_obs=random.randrange(i,i+30)
		y_coin=random.randrange(i,i+30)
		obj3=render(x_obs,y_obs,10,obs,inp)
		obj3.placement()
		obj2.Cleaner()
		obj6=coins(5,'$')
		obj6.make_coin(x_coin,y_coin)
	else:
		obs=np.full((10,10),' ')
		obj2=Slant(10,obs,"right")
		obs=obj2.make_slant()
		x_obs=random.randint(6,row-13)
		x_coin=random.randint(6,row-13)
		y_obs=random.randrange(i,i+30)
		y_coin=random.randrange(i,i+30)
		obj3=render(x_obs,y_obs,10,obs,inp)
		obj3.placement()
		obj2.Cleaner()
		obj6=coins(5,'$')
		obj6.make_coin(x_coin,y_coin)

for i in range(20000):
	obj1=On_screen(row,i,(col+i),inp)
	obj1.sky('@')
#	print(type(inp))
	obj1.ground('!')
	obj4.render_player()
	obj4.move_player(i,(col+i))
	obj1.printsky()
	obj1.printbody()
	obj1.printground()
	print('\033[H',end="",flush='True')	
#	time.sleep(0.05)






