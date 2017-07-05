from scipy.misc import imread
import cv2
import numpy as np
import glob, time
import os
from utilities import calculate_tpm2_iphone_jpegread

# def countfile(iterator):
# 	return sum(1 for i in iterator)

start_time = time.time()

imagedirectory = '/Volumes/My Passport/UM-MDCR&I DATABASE/IMAGE DATABASE/Samsung Galaxy Note Series/Samsung Galaxy Note 4/Samsung Galaxy Note 4-1/Indoor'
imagefiles = glob.iglob(imagedirectory+'/*.jpg')

# totalfile = countfile(imagefiles)
count = 1

with open(imagedirectory+'/cp_features.txt', 'w') as fidout:
	for currentfilename in imagefiles:
 		#Read image as 2D gray-scale
		#img = np.around(imread(currentfilename, flatten=True)).astype(int)
		img = np.transpose(cv2.imread(currentfilename, 0)) 

		cover_stat = calculate_tpm2_iphone_jpegread(img)

		index = 1
		for j in cover_stat:
			if j != 0:
				fidout.write('%d:%f ' % (index, j))	
			index = index + 1	
		fidout.write('\n')
		print('Completed %d image(s)' % (count))
		count = count + 1		

# your code
elapsed_time = time.time() - start_time
print elapsed_time		
			