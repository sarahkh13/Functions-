
from __future__ import division
#Must include since terminal is python 2, not 3

import re

file1 = open("Vet ACE Patient Data Jan 3 07.txt").readlines()
newfile =  open("newfile.txt", "w")


sealions = {}
sealion_count = 0

with open('newfile.txt', "w") as newfile:
	for line in file1: 
		if re.search(r"DRAWN", line):
			aa1 = line
			patterna = r"(D/T DRAWN:\s)(\d..\d\d.\d\d)"
			aa2 = re.search(patterna, str(aa1), re.I)
			aa = aa2.group(2)
			newfile.write("DATE: " + str.strip(aa))   #Could just delete the date portion if dont want it
			newfile.write('\t')	
		if re.search(r"PATIENT ID:\s*[A-Z]{0,10}\s{0,1}[A-Z]{0,10}\d{0,10}\s{5,6}", line): 
			bb1 = line
			patternb = r"(PATIENT ID:\s*)([A-Z]{0,10}\s{0,1}[A-Z]{0,10}\d{0,10})(\s{5,6})"
			bb2 = re.search(patternb, str(bb1), re.I)
			bb = bb2.group(2)
			newfile.write("ID: " + str.strip(bb))
			newfile.write('\t')	
		if re.search(r"NAME: \w{0,20}\s+SPC", line):
			cc1 = line
			patternc = r"(NAME:)([A-Z]{0,20}\s{0,3}[A-Z]{0,20})(\s+SPC)"
			cc2 = re.search(patternc, str(cc1), re.I)
			cc = cc2.group(2)
			newfile.write("NAME: " + str.strip(cc))
			newfile.write('\t')
		if re.search(r"SEX:\s+[MF]", line):
			dd1 = line
			patternd = r"(SEX: )([MF])(\s*L)"  ##(SEX:.)(\w)(\s*L)" 
			dd2 = re.search(patternd, str(dd1), re.I)
			dd = dd2.group(2)
			newfile.write("SEX: " + str.strip(dd))
			newfile.write('\t')	
		if re.search(r"BUN", line):
			ee1 = line
			patterne = r"(BUN\s*)(\d{1,4}.{0,1}\d{0,3})(\s+)([A-Z]{0,1}[A-Z]{0,1})(\s+)(\d+. - \d+.\d{0,2})"
			ee2 = re.search(patterne, str(ee1), re.I)
			ee = ee2.group(2)
			eeb = ee2.group(4)
			eec = ee2.group(6)
			newfile.write("BUN: " + str.strip(ee) + str.strip(eeb) + str.strip(eec))
			newfile.write('\t')	
		if re.search(r"CREAT", line):
			ff1 = line
			patternf = r"(CREAT\s*)(\d{1,4}.{0,1}\d{0,3})(\s+)([A-Z]{0,1}[A-Z]{0,1})(\s+)(\d+.. - \d+.\d{0,2})"
			ff2 = re.search(patternf, str(ff1), re.I)
			ff = ff2.group(2)
			ffb = ff2.group(4)
			ffc = ff2.group(6)
			newfile.write("CREAT: " + str.strip(ff + ffb + ffc))
			newfile.write('\t')	
		if re.search(r"PHOS", line):
			gg1 = line
			patterng = r"(PHOS\s*)(\d{1,4}.{0,1}\d{0,3})(\s+)([A-Z]{0,1}[A-Z]{0,1})(\s+)(\d+.. - \d+.\d{0,2})"
			gg2 = re.search(patterng, str(gg1), re.I)
			gg = gg2.group(2)
			ggb = gg2.group(4)
			ggc = gg2.group(6)
			newfile.write("PHOS: " + str.strip(gg + ggb + ggc))
			newfile.write('\t')	
				
		if re.search(r"THE MARINE MAMMAL CENTER", line):
			sealion_count = sealion_count + 1
			print sealion_count
			newfile.write(str(sealion_count))
			newfile.write('\n')
			
#print str(line)
#print str.lstrip()

#newfile.close()
#DONT NEED TO CLOSE FILE when open with 'with'

print "Finished"
#Create a counter, every time after add 
