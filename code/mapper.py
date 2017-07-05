#!/usr/bin/python

from __future__ import division
from PIL import Image
import numpy as np
import os
import sys
import StringIO


def calculate_tpm2_iphone_jpegread(img2Darray):

	#Get dimension of img2Darray
	e = img2Darray.shape
	
	smaller = 0
	bigger = 0
	equal = 0

	smaller2 = 0
	bigger2 = 0
	equal2 = 0

	smaller3 = 0
	bigger3 = 0
	equal3 = 0

	smaller4 = 0
	bigger4 = 0
	equal4 = 0

	smaller5 = 0
	bigger5 = 0
	equal5 = 0

	smaller6 = 0
	bigger6 = 0
	equal6 = 0

	smaller7 = 0
	bigger7 = 0
	equal7 = 0

	smaller8 = 0
	bigger8 = 0
	equal8 = 0

	##############################

	smaller_plus = 0
	smaller_minus = 0
	smaller_static = 0

	bigger_plus = 0
	bigger_minus = 0
	bigger_static = 0

	equal_plus = 0
	equal_minus = 0
	equal_static = 0

	###############################

	smaller_plus2 = 0
	smaller_minus2 = 0
	smaller_static2 = 0

	bigger_plus2 = 0
	bigger_minus2 = 0
	bigger_static2 = 0

	equal_plus2 = 0
	equal_minus2 = 0
	equal_static2 = 0

	###########################

	smaller_plus3 = 0
	smaller_minus3 = 0
	smaller_static3 = 0

	bigger_plus3 = 0
	bigger_minus3 = 0
	bigger_static3 = 0

	equal_plus3 = 0
	equal_minus3 = 0
	equal_static3 = 0

	########################

	for length in range(0, e[0]-7, 8):
		for wide in range(0, e[1]-8, 8):
			
			z = img2Darray[length:length+9, wide:wide+9]
			
			#horizontal
			row = 0
			col = 1

			if (z[row,col] < z[row,col+1]):
				smaller = smaller+1
				if z[row,col+2] > z[row,col+1]:
					smaller_plus = smaller_plus+1
				elif z[row,col+2] < z[row,col+1]:
					smaller_minus = smaller_minus +1
				elif z[row,col+2] == z[row,col+1]:
					smaller_static = smaller_static +1
			
					   
			elif (z[row,col] > z[row,col+1]):
				bigger = bigger+1          
				if z[row,col+2] > z[row,col+1]:
					bigger_plus = bigger_plus+1
				elif z[row,col+2] < z[row,col+1]:
					bigger_minus = bigger_minus +1
				elif z[row,col+2] == z[row,col+1]:
					bigger_static = bigger_static +1
			
			elif (z[row,col] == z[row,col+1]):
				equal = equal+1      
				if z[row,col+2] > z[row,col+1]:
					equal_plus = equal_plus+1
				elif z[row,col+2] < z[row,col+1]:
					equal_minus = equal_minus +1
				elif z[row,col+2] == z[row,col+1]:
					equal_static = equal_static +1

			#vertical
			row = 1
			col = 0

			if (z[row,col] < z[row+1,col]):
				smaller2 = smaller2+1  
				
				if z[row+2,col] > z[row+1,col]:
					smaller_plus2 = smaller_plus2+1
				elif z[row+2,col] < z[row+1,col]:
					smaller_minus2 = smaller_minus2 +1
				elif z[row+2,col] == z[row+1,col]:
					smaller_static2 = smaller_static2 +1

			elif (z[row,col] > z[row+1,col]):
				bigger2 = bigger2+1

				if z[row + 2,col] > z[row+1,col]:
					bigger_plus2 = bigger_plus2+1
				elif z[row + 2,col] < z[row+1,col]:
					bigger_minus2 = bigger_minus2 +1
				elif z[row + 2,col] == z[row+1,col]:
					bigger_static2 = bigger_static2 +1

			elif (z[row,col] == z[row+1,col]):
				equal2 = equal2+1

				if z[row + 2,col] > z[row+1,col]:
					equal_plus2 = equal_plus2+1
				elif z[row+2,col] < z[row+1,col]:
					equal_minus2 = equal_minus2 +1
				elif z[row+2,col] == z[row+1,col]:
					equal_static2 = equal_static2 +1 

			#diagonal
			row = 1
			col = 1

			if (z[row,col] < z[row+1,col+1]):
				smaller3 = smaller3+1

				if z[row+2,col+2] > z[row+1,col+1]:
					smaller_plus3 = smaller_plus3+1
				elif z[row+2,col+2] < z[row+1,col+1]:
					smaller_minus3 = smaller_minus3 +1
				elif z[row+2,col+2] == z[row+1,col+1]:
					smaller_static3 = smaller_static3 +1

			elif (z[row,col] > z[row+1,col+1]):
				bigger3 = bigger3+1

				if z[row+2,col+2] > z[row+1,col+1]:
					bigger_plus3 = bigger_plus3+1
				elif z[row+2,col+2] < z[row+1,col+1]:
					bigger_minus3 = bigger_minus3 +1
				elif z[row+2,col+2] == z[row+1,col+1]:
					bigger_static3 = bigger_static3 +1

			elif (z[row,col] == z[row+1,col+1]):
				equal3 = equal3+1

				if z[row+2,col+2] > z[row+1,col+1]:
					equal_plus3 = equal_plus3+1
				elif z[row+2,col+2] < z[row+1,col+1]:
					equal_minus3 = equal_minus3 +1
				elif z[row+2,col+2] == z[row+1,col+1]:
					equal_static3 = equal_static3 +1

	
	total = bigger + smaller + equal
	total2 = bigger2 + smaller2 + equal2
	total3 = bigger3 + smaller3 + equal3
	
	mat = np.array([smaller_plus, smaller_minus, smaller_static, bigger_plus, bigger_minus, bigger_static, equal_plus, equal_minus, equal_static])
	mat2 = np.array([smaller_plus2, smaller_minus2, smaller_static2, bigger_plus2, bigger_minus2, bigger_static2, equal_plus2, equal_minus2, equal_static2])
	mat3 = np.array([smaller_plus3, smaller_minus3, smaller_static3, bigger_plus3, bigger_minus3, bigger_static3, equal_plus3, equal_minus3, equal_static3])

	np.set_printoptions(precision=6)
	if total > 0:
		mat = mat / total

	if total2 > 0:
		mat2 = mat2 / total2

	if total3 > 0:
		mat3 = mat3 / total3

	stat_final = np.concatenate((mat,mat2))
	stat_final = np.concatenate((stat_final,mat3))
	stat_update = stat_final

	return stat_update	


image = StringIO.StringIO(sys.stdin.read())
#Read image as 2D gray-scale
image.seek(0)
img = Image.open(image).convert('L')
img = np.array(img)

cover_stat = calculate_tpm2_iphone_jpegread(img)

index = 1
for j in cover_stat:
	if j != 0:
		print('%d:%f ' % (index, j))	
	index = index + 1
