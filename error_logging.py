import os
from datetime import datetime

class LogFile:

    def __init__(self):
        filename = 'error_log.txt'

        if os.path.isfile(filename):
            with open(filename, 'a') as myfile:
                myfile.write('\n')
                myfile.write('\n')

        if os.path.isfile(filename) == False:
            with open(filename, 'w+') as myfile:
                myfile.write("Error log for kids clock"+'\n\n')

    def logComment(self, commentString):
        with open('error_log.txt', 'a') as myfile:
            myfile.write(commentString + " " + str(datetime.today()) + "\n")

