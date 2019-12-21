import os as os
from shutil import move
import click

# fall19 = ['CS 2214', 'CS 2413', 'CS 3083', 'MA 2034', 'STS 2264']
# spring20 = ['CSCI 4', 'CS 3314', 'CS 4513', 'CS 3224', 'CS 3913']

my_courses = {"CS 2214": "Fall 2019", "CS 2413": "Fall 2019", "CS 3083": "Fall 2019", "MA 2034": "Fall 2019", "STS 2264": "Fall 2019", 'CSCI 4': "Spring 2020", 'CS 3314': "Spring 2020", 'CS 4513': "Spring 2020", 'CS 3224': "Spring 2020", 'CS 3913': "Spring 2020"}

src = "/Users/abidrais/Desktop/"
destDir = "/Users/abidrais/Desktop/NYUTandon/"



@click.command() 
def fileMover(): 
    move_bool = False 

    for file in os.listdir(src): 
        fileSplit = file.split()

        try: 
            course = fileSplit[0] + " " + fileSplit[1]
        except: 
            course = ""
        
        if course in my_courses: 

            semester = my_courses[course]
            fileRem = " ".join(fileSplit[2:])

            # Move File
            fileSrc = src + file
            destFinal = destDir + semester + "/" + course
            move(fileSrc, destFinal)

            # Print Success 
            click.echo("Moved "+fileRem+" to "+ course + " in "+ semester)
            move_bool = True
    
    if move_bool == False: 
        click.echo("No files have been moved")

if __name__ == '__main__': 
    fileMover()