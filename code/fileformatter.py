import glob
import re
import sys, getopt

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","format="])
		for opt, arg in opts:
			if opt == '-h':
				print 'fileformatter.py -i <inputfile> -o <outputfile> -f <format>'
				sys.exit()
			elif opt in ("-i", "--ifile"):
				inputfile = arg
			elif opt in ("-o", "--ofile"):
				outputfile = arg
			elif opt in ("-f", "--format"):
				format = arg	

		feature_file = glob.iglob(inputfile)
		
		for f in feature_file:
			print f
		# 	version = re.search(r'(?<=\w)\s?\d\w?', f)
			subversion = re.search(r'\w\d?-\d+', f)
			with open(f) as dataset:
				with open('/Volumes/Normal-Hard-Disk/Users/mfaizmzaki/mahout-image-classification/Sony/' + outputfile + subversion.group() + '-outdoor-edited.csv', 'a+') as newdataset:
					for line in dataset:
						formatted = re.sub(r'\d+:', "", line)
						formatted = re.sub(r' ', ",", formatted)
						if format == 'weka':
							formatted = re.sub(r'$', subversion.group() + "\n", formatted.rstrip())	 #Uncomment if formatting for each subversion of the same model	
							# formatted = re.sub(r'$', version.group() + "\n", formatted.rstrip())	 #Uncomment if formatting for each model as a whole
							# formatted = re.sub(r'$', "\n", formatted.rstrip())
						elif format == 'mahout':
							formatted = re.sub(r'^',  subversion.group() + ',', formatted) 	#Uncomment if formatting for each subversion of the same model	
							# formatted = re.sub(r'^',  version.group() + ',', formatted)	  #Uncomment if formatting for each model as a whole
							formatted = re.sub(r',$', "\n", formatted.rstrip())
						newdataset.write(formatted)
			print 'All good to go!'

	except (getopt.GetoptError, IOError) as e:
		print 'fileformatter.py -i <inputfile> -o <outputfile> -f <format>'
		sys.exit(2)

if __name__ == "__main__":
	main(sys.argv[1:])