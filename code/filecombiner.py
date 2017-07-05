import glob

try:
	inputfile = '/Volumes/Normal-Hard-Disk/Users/mfaizmzaki/mahout-image-classification/Samsung/*-edited.csv'
	tempfiles = glob.iglob(inputfile)
	for files in tempfiles:
		with open(files) as dataset:
			print files
			with open('/Volumes/Normal-Hard-Disk/Users/mfaizmzaki/mahout-image-classification/Samsung/note-complete.csv', 'a+') as newdataset:
				for line in dataset:
					newdataset.write(line)
	print 'All done!'

except IOError as e:
	print e.error()