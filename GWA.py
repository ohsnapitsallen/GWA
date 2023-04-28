import math
import re

#Create a function
def highestgwa():
    #Open file of list of students with their GWA
    with open("gwalist.txt", "r") as input_file:
        lines = input_file.readlines()
        final = math.inf
#Open file of list of students with their GWA
#Recognize all floats within the file
#Find the highest GWA in the file
#Convert float to string
#Locate the line where the highest GWA is located
#Print the student's name and their GWA
