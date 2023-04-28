import math
import re

#Create a function
def highestgwa():
    #Open file of list of students with their GWA
    with open("gwalist.txt", "r") as input_file:
        lines = input_file.readlines()
        final = math.inf
        #Recognize all floats within the file
        for line in lines:
            gwas = list(map(float, re.findall("\d+\.\d+", line)))
            #Find the highest GWA in the file
            for i in gwas:
                final = min(final, i)
        #Convert float to string
        for line in lines:
            finalstr = str(final)
        #Locate the line where the highest GWA is located
            if finalstr in line:
                return line
#Print the student's name and their GWA
print("The student with the highest GWA is", highestgwa())
