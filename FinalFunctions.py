from __future__ import division
import re
import collections

file_name = ("Vet ACE Patient Data Sept 1 10.txt")
#file_name = open("Vet ACE Patient Data Jan 3 07.txt").readlines()
#Do not need open here, as I specify to open the file in the recList function below
newfile =  open("newfile.txt", "w")
#Creates a new file which will be same as original except each record will be numbered



#DIVIDES THE RECORDS IN EACH FILE

count = 0 

def recList(file_path):  #Creates a function recList that runs on the file in parentheses
#later, I use this in a for loop on the file specifiled above, by calling "for record in recList(file_name): "
    with open(file_path) as f:  #opens the file of interest
        chunk = []   #starts an empty chunk
        for line in f:  #for each line in the file of interest
            if 'PRINTED' in line:  #if printed is in the line (ie top of record)
                if chunk:
                    yield "".join(chunk)
                chunk = [line]
            else:
                chunk.append(line) 
        if chunk:
            yield "".join(chunk)
            #Appends each line as a chunk from 1 "PRINTED" to next, ie for one record



xx = recList(file_name)   #Assigns the output of above function (on main file) to variable xx
yy = list(xx)   #Takes the above, formats output as a list of records (used to specify record #s later)
zz = str(xx)    #Same as above but makes it a string- not used here, but it is an additional option 


#Below creates a new file, same as original but with record number at the top of each record
for record in recList(file_name):
    count = count + 1
    newfile.write('--' + " " + str(count) + " " +  "--" + " ")
    newfile.write(''.join(record))
    #print str(count)   #Optional: will print string of record #s as it moves through file






pdict= {}

pdict = {
"Access": r"(ACCESSION:\s+)(\d+)",
"ID": r"(PATIENT ID:\s*)(\w+\s{0,1}\-{0,1}\w+)",
"Name": r"(NAME:\s+)(\w+.*)(\s+AGE:)",
"Date": r"(D/T DRAWN:\s)(\d..\d\d.\d\d)",
"Sex": r"(SEX: )([MF])(\s*L)",
"BUN": r"(BUN\s*)(\d{1,4}.{0,1}\d{0,3})(\s+)([A-Z]{0,1}[A-Z]{0,1})(\s+)(\d+. - \d+.\d{0,2})",
"BUNREF": r"(BUN\s*\d{1,4}.{0,1}\d{0,3}\s+[A-Z]{0,1}[A-Z]{0,1}\s+)(\d+. - \d+.\d{0,2})",
"CREAT": r"(CREAT\s*)(\d{1,4}.{0,1}\d{0,3})(\s+)([A-Z]{0,1}[A-Z]{0,1})(\s+)(\d+.. - \d+.\d{0,2})",
"CREATREF": r"(CREAT\s*\d{1,4}.{0,1}\d{0,3}\s+[A-Z]{0,1}[A-Z]{0,1}\s+)(\d+.. - \d+.\d{0,2})",
"PHOS": r"(PHOS\s*)(\d{1,4}.{0,1}\d{0,3})(\s+)([A-Z]{0,1}[A-Z]{0,1})(\s+)(\d+.. - \d+.\d{0,2})",
"PHOSREF": r"(PHOS\s*\d{1,4}.{0,1}\d{0,3}\s+[A-Z]{0,1}[A-Z]{0,1}\s+)(\d+.. - \d+.\d{0,2})",
}




#GET ALL THE PARAMETERS FOR EACH RECORD: 

def paramGetter(pattern, record):  
    #This function searches each record for the patterns specified above. 
    seeker = re.search(pattern, record)
    if seeker:   #If there is match
        return (seeker.group(2))   #The second group in parentheses with be returned (if not, return nothing)
    else:
        return None








#CREATING DICTIONARIES FOR EACH VALUES IN EACH RECORD & AN INDEX FOR ALL OF THESE IN THE OVERALL FILE


rec_params = {}   #Creates a new dictionary that will hold parameters present in each record
masterDict = {}   #Creates a master dictionary that will hold all the above dictionaries


for record in recList(file_name):
    for key in pdict.keys():
        res =  paramGetter(pdict[key], yy[4])
        if res:
            rec_params[key] = res
        #print rec_params    (putting this here would print out the rec params for each as it goes - here for record yy[4])
    #SLID = str(rec_params["ID"] + "-" + rec_params["Date"])
    SLID = rec_params["Access"] 
    masterDict[SLID] = rec_params






#Above for loop did it for the 4th record. In order to do it for all, I needed to add a counter (below).
#The next section modifies the above in order to go through dictionary for each record, not just one (above- just #4): 


rec_paramsII = {}   
#Creates an empty dictionary to hold the parameter values for each individual record
masterDictII = {}   
#Creates a master dictionary to hold all individual records (dictionaries above) in the file 





number = 0  
#Counter for the record number- must start at zero (the first record it processes is #0 to python, though I labeled it #1)



#For loop below creates individual dictionaries, and then appends these to the master dictionary as it moves through the file
for record in recList(file_name):   #for each individual record as broken up by initial function: 
    for key in pdict.keys():  #for each value of interest (key) in the dictionary of parameters I want: 
        res =  paramGetter(pdict[key], yy[number])   #yy is the string of values from recList(file_name), specified earlier
        #res = the parameter value in individual record number, starting with first one (0, specified above)
        if res:
            rec_paramsII[key] = res   #the results of the parameter search for that record fill the rec_paramsII dictionary
    SLID = rec_paramsII["Access"]   #the Accession number is designated as a unique ID number for that record
    masterDictII[SLID] = rec_paramsII  
    #this adds each individual record to master dictionary (each individual one given as a dictionary)
    #The accession number is then used as the key, with the values of the record in rec_paramsII as the associated values
    rec_paramsII = {}  #clears rec_paramsII so that it is fresh for the next one
    number = number + 1        #adds one to the counter so that the next time the loop runs, it moves to next record
        


#masterDictII['479']  
#This prints out the dictionary value for file with access # 479, so you can confirm its working properly
#LEARN PYTHON THE HARD WAY- Good website tutorials (NOTE TO SELF)






#CREATE A NEW FILE of the results for each record as rows of tab delimted values

numII = 0
#Must start the counter at zero, otherwise you end up with the error below when it tries to run: 
#--> 156 res =  paramGetter(pdict[key], yy[numII])   
#IndexError: list index out of range
#To address this, when listing the numbers


out_file = open("out_test_file.txt", "w")  #creates the new file

out_file.write("Rec_of_" + str(count) + "\t" + "Name" + "\t" + "Accession #" + "\t" + "CREAT Ref" + "\t" "ID" + "\t" + "BUN Ref" + "\t" + "PHOS" + "\t" + "CREAT" + "\t" + "PHOS Ref" + "\t" + "Sex" + "\t" + "BUN" + "\t" + "Date" + "\n")

#Alternate headers without counter if removed below: out_file.write("Name" + "\t" + "Accession #" + "\t" + "CREAT Ref" + "\t" "ID" + "\t" + "BUN Ref" + "\t" + "PHOS" + "\t" + "CREAT" + "\t" + "PHOS Ref" + "\t" + "Sex" + "\t" + "BUN" + "\t" + "Date" + "\t" + "\n")
#Creates a row that labels the column values at the top of the file (headers), then \n moves down to next line
#Count is taken from initial function, as it counts the records as it moves through master file


#For loop below goes through and fills the columns with values of interest for each record
for record in recList(file_name):
    aarec = str(numII + 1) + "\t"   #record number is printed below; start at 0+1
    out_file.write(aarec)   #writes this value to beginning of each row (that individual record listing)
    for key in pdict.keys():
        res =  paramGetter(pdict[key], yy[numII])
        if res:
            eachrecord = str(res) + "\t"  #prints each record parameter in the individual record & tab
            out_file.write(eachrecord)  #writes this to the record listing (row) after the record number
        else:
            NAenter = "NA" + "\t"  #if value not present, print's NA and a tab
            out_file.write(NAenter)  #writes this to file
    out_file.write("\n")   #goes to next line at end of record
    numII = numII + 1  #adds one to the counter so that it goes on to next record





print "Finished"
#Hazaa!

