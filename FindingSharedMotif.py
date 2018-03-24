
#reading file
file = open('lcsm.txt', 'r')
#print (file.read());

#arrays
dnaLabelList = {} #goes with dNAList keeps track of each DNA string name.
dnaList = [] #DNA list

#varibales.
currentDNA = ""
greaterThan = ">"
numOfDNA = 0
labelCount = 0

#contains() function ~ check is the string has ">" sybmol.
#returns true if has the sybmol otherwise false.
def containsSymbol(a):
    for i in a:
        if(greaterThan == i):
            return True;
    return False;

#-----Reading FASTA file line by line-------#
for line in file:
    if(containsSymbol(line) == False):
        currentDNA += line; #adding each line for single DNA string.
        #print(line);  #print tests for DNA string.
    elif(containsSymbol(line)):
        #takes out the symbol and just adds the name/label of DNA string.
        dnaLabelList[labelCount] = line[1:len(line)-1]
        if labelCount >= 1:
            dnaList.append(currentDNA); 
            currentDNA = ""
            numOfDNA += 1
        labelCount += 1
        #print(line); #print tests for labels
#adds last dna string
dnaList.append(currentDNA)
numOfDNA += 1
#------End of reading file ----------------#

#**TEST**checking lists and variables
#print("Number of DNA strings:", numOfDNA);
#for i in range(numOfDNA):
    #print("DNA Label:", dnaLabelList[i]);
    #print("string DNA:", dnaList[i]);
    
#----finding longest common substring list----#
    
#variables
def longestCommonString():
    currentLCS = ""
    dna1 = dnaList[0]
    dna2 = dnaList[1:]; #lists of all dna's read one by one.
    #print("DNA1:" , dna1, "DNA2:",  dna2);
    for i in range(len(dna1)): #going to run the total number of DNA strings there are.
        for j in range(i, len(dna1)):
            #print(i, j);
            motif1 = dna1[i:j+1]
            isCommonString = False
            for motif2 in dna2:
                if motif1 in motif2:
                    #print(dna1);
                    #print("motif1:", motif1, "motif2", motif2);
                    isCommonString = True
                else:
                    isCommonString = False
                    break
            if isCommonString:
                if len(currentLCS) <= len(motif1):
                    print(motif1)
                    currentLCS = motif1
                
    return currentLCS
#OFFICAL PRINT INFO

print("LCS:", longestCommonString())
        
