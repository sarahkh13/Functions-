from __future__ import division
import re

file1 = open("Vet ACE Patient Data Jan 3 07.txt").readlines()
newfile =  open("newfile.txt", "w")



SLDict = {}

def SeaLionGrep(file):
    #make an empty parameter dictionary 
    ParamDict = {}
    #populate the parameter dictionary
    ParamDict = {
    	"ID" = r"(PATIENT ID:\s*)([A-Z]{0,10}\s{0,1}[A-Z]{0,10}\d{0,10})(\s{5,6})"
    	"Sex" = r"(SEX: )([MF])(\s*L)"
    	"Name" = r"(NAME:)([A-Z]{0,20}\s{0,3}[A-Z]{0,20})(\s+SPC)"
    	"Date" = r"(D/T DRAWN:\s)(\d..\d\d.\d\d)"
    	"BUN"= r"(BUN\s*)(\d{1,4}.{0,1}\d{0,3})(\s+)([A-Z]{0,1}[A-Z]{0,1})(\s+)(\d+. - \d+.\d{0,2})"
    	"CRE" = r"(CREAT\s*)(\d{1,4}.{0,1}\d{0,3})(\s+)([A-Z]{0,1}[A-Z]{0,1})(\s+)(\d+.. - \d+.\d{0,2})"
    	"PHOS"= r"(PHOS\s*)(\d{1,4}.{0,1}\d{0,3})(\s+)([A-Z]{0,1}[A-Z]{0,1})(\s+)(\d+.. - \d+.\d{0,2})"
    	}
    #make a unique id
    SLID = str("ID"-"Date")
    #return parameter dictionary, uniqueid
    return(SLID, ParamDict)



for line in ff.readlines():
	if re.search(r"THE MARINE MAMMAL CENTER", line):
		newrecord = ""
		while not linelstrip().startswith("PRINTED"):
			newrecord = newrecord + line and newrecord>0
		#test that newrecord is longer than 0
		#pd, uid = processRecord(newrecord)
		ParamDict, SLID = SeaLionGrep(newrecord)
		#recorddict[uid] = pd   ~~this will populate the 1st dict line
		SLDict[SLID] = ParamDict




for key in SLDict.keys(): 
	line = "record # is {} and parameters are {}"
	xx = SLDict[key].keys()
	name = SLDict[key]
	ParamDict = xx 
	line = line.format(SLID, ParamDict)
	



print "Finished"

